import json
import boto3

rekognition = boto3.client("rekognition")

def lambda_handler(event, context):
    try:
        bucket_name = event["bucket_name"]
        image_key = event["image_key"]

        response = rekognition.detect_text(
            Image={"S3Object": {"Bucket": bucket_name, "Name": image_key}}
        )

        extracted_text = " ".join(
            [d["DetectedText"] for d in response["TextDetections"]]
        )

        return {"statusCode": 200, "extracted_text": extracted_text}

    except Exception as e:
        return {"statusCode": 500, "error": str(e)}
