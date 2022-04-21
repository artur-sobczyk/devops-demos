'use strict';

// Configuring the AWS SDK
var AWS = require('aws-sdk');

// Create DynamoDB service object
var dynamoDbClient = new AWS.DynamoDB({apiVersion: '2012-08-10'});

function getRandomSlotPromise() {
    
    // Define parameters JSON for retrieving slot pull data from the database
    var thisPullParams = {
        Key: {
            "slotPosition": {
                N: ""
            }
        },
        TableName: "SlotPositionTable"
    };
    
    // Set a random number 0-10 for the slot position
    thisPullParams.Key.slotPosition.N = Math.floor(Math.random()*16).toString();
    
    // Call DynamoDB to retrieve the image
    return dynamoDbClient.getItem(thisPullParams).promise().then(
        function(data) {
            return data.Item.imageFile.S
        },
        function(error) {
            console.log("Database read error on right wheel.")
            console.error(error)
        }
    );
}

exports.handler = (event, context, callback) => {

    // Define the object that will hold the data values returned
    var slotResults = {
        'isWinner' : false,
        'leftWheelImage' : {'file' : {S: ''}},
        'middleWheelImage' : {'file' : {S: ''}},
        'rightWheelImage' : {'file' : {S: ''}}
    };

    // get promises for random images 
    var myLeftPromise = getRandomSlotPromise();
    var myMiddlePromise = getRandomSlotPromise();
    var myRightPromise = getRandomSlotPromise();

    // wait for resolution and build response
    Promise.all([myLeftPromise, myMiddlePromise, myRightPromise]).then(
        function(values) {
            slotResults.leftWheelImage.file.S = values[0];
            slotResults.middleWheelImage.file.S = values[1];
            slotResults.rightWheelImage.file.S = values[2];
            
            // If all three values are identical, the spin is a winner
            if ((values[0] === values[1]) && (values[0] === values[2])) {
                slotResults.isWinner = true;
            }
            // Return the JSON result to the caller of the Lambda function
            callback(null, slotResults);
        }
    );
};
