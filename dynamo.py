import boto3
import json_lines


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Smartphones')

smartphones = open('output/phones.jl', 'r')

for json in json_lines.reader(smartphones):
    print('inserting: ' + json['title'])

    with table.batch_writer() as batch:
        batch.put_item(Item=json)

smartphones.close()
