import json
from datetime import datetime, timedelta


def lambda_handler(event, context):
    entered_time = datetime.strptime(event['State']['EnteredTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
    today = entered_time.strftime('%Y-%m-%d')
    yesterday = (entered_time - timedelta(days=1)).strftime('%Y-%m-%d')

    return {
        "today": today,
        "yesterday": yesterday
    }

