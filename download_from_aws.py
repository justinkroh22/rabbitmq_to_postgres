import boto3

s3 = boto3.client('s3')
s3.download_file('comp851-m1-f19', 'userdata2.csv', 'userdata2.csv')