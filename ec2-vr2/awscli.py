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


def aws_list_instances():
    ec2 = boto3.client('ec2')
    response=ec2
    #print  json.dumps(response.describe_instances()['Reservations'])
    for instances in response.describe_instances()['Reservations'][0]['Instances']:
        for keys in instances.keys():
            print "%s : %s" %( keys, instances[keys])


def aws_s3_list():
    s3 = boto3.client('s3')
    print s3.list_buckets()['Buckets'][0]['Name']

aws_list_instances()
aws_s3_list()
