import boto3
import yaml
from aws import cloudwatch
from datetime import datetime, timedelta
region = "us-east-1"

with open("../rules.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
for section in cfg:
    print(section)
    print(cfg[section])


class Janitor:

    today = datetime.now() + timedelta(days=1)  # today + 1 because we want all of today
    two_weeks = timedelta(days=31)
    start_date = today - two_weeks

    def __init__(self):
        print self

    def get_metrics(volume_id):
        """Get volume idle time on an individual volume over `start_date`
           to today"""
        metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/EBS',
            MetricName='VolumeIdleTime',
            Dimensions=[{'Name': 'VolumeId', 'Value': volume_id}],
            Period=3600,  # every hour
            StartTime=start_date,
            EndTime=today,
            Statistics=['Minimum'],
            Unit='Seconds'
        )
        return metrics['Datapoints']

