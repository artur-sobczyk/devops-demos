// dependencies

const AWS = require('aws-sdk');
const util = require('util');

exports.handler = async (event, context, callback) => {
	console.log("Reading input from event:\n", util.inspect(event, { depth: 5 }));
	const id = event.objectID
	let extractedMetadata = event.extractedMetadata;
	const fullsize = {
		key: event.s3Key,
		width: extractedMetadata.dimensions.width,
		height: extractedMetadata.dimensions.height
	}

	const updateInput = {
		id,
		fullsize,
		format: extractedMetadata.format,
		exifMake: extractedMetadata.exifMake || null,
		exitModel: extractedMetadata.exifModel || null,
		ProcessingStatus: "SUCCEEDED"

	}
	const thumbnailInfo = event.parallelResults[1];

	if (thumbnailInfo) {
		updateInput['thumbnail'] = {
			key: thumbnailInfo.s3key,
			width: Math.round(thumbnailInfo.width),
			height: Math.round(thumbnailInfo.height)
		}
	}

	if (event.parallelResults[0]) {
		const labels = event.parallelResults[0];
		let tags = []
		for (let i in labels) {
			tags.push(labels[i]["Name"])
		}
		updateInput["objectDetected"] = tags
	}


	if (event.extractedMetadata.geo) {
		updateInput['geoLocation'] = {
			Latitude: event.extractedMetadata.geo.latitude,
			Longtitude: event.extractedMetadata.geo.longitude
		}
	}

	console.log(JSON.stringify(updateInput, null, 2));

	return { "Status": "Success" }
}
