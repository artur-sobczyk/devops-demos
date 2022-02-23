import json


def color(json_data):
    return json.dumps(json_data, default=str, sort_keys=True)


def lambda_handler(event, context):

    data = json.dumps(
        {
            "event": json.loads(json.dumps(event).replace("null", '"null"')),
            "context": {
                "function_name": context.function_name,
                "function_version": context.function_version,
                "invoked_function_arn": context.invoked_function_arn,
                "memory_limit_in_mb": context.memory_limit_in_mb,
                "aws_request_id": context.aws_request_id,
                "log_group_name": context.log_group_name,
                "log_stream_name": context.log_stream_name,
                "remining_timeout": context.get_remaining_time_in_millis(),
            },
        }
    )

    print(data)

    return {
        "statusCode": 200,
        "body": data,
        "headers": {"Content-Type": "application/json"},
    }
