import boto3

def lambda_handler(event, context):
    iam = boto3.resource("iam")
    account_summary = iam.AccountSummary()
    response = {"result": account_summary}
    return response


