import boto3
region = "us-east-1"

cloudwatch = boto3.client("cloudwatch", region_name=region)