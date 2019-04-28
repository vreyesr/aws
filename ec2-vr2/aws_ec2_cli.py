#!/usr/bin/python
'''
    NAME
        aws_ec2_cli.py - For EC2 utility at AWS

    AUTHOR
        Valentin Reyes
'''

__version__ = '20190417.1'

import boto3
import json
import os

client = boto3.client('s3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
)


def aws_list_instances():
    ec2 = boto3.client('ec2')
    response=ec2
    #print  json.dumps(response.describe_instances()['Reservations'])
    for instances in response.describe_instances()['Reservations'][0]['Instances']:
        for keys in instances.keys():
            print "%s : %s" %( keys, instances[keys])

aws_list_instances()
