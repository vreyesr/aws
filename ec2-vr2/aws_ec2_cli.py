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

ec2 = boto3.client('ec2')

def stop_ec2():
    ec2.stop_instances(InstanceIds=['i-07a71a7dfcbf2001c'])

def start_ec2():
    ec2.start_instances(InstanceIds=['i-07a71a7dfcbf2001c'])
def aws_list_instances():
    compute=ec2.describe_instances()

#    print [(k, i[k]) for i in compute['Reservations'][0]['Instances'] for k in i.keys()]
    l=[(k,i[k]) for i in compute['Reservations'][0]['Instances'] for k in ['State','PublicIpAddress','PublicDnsName' ] if "PublicIpAddress" in i]
    for k in l:
        print (k[0],k[1])

aws_list_instances()
#stop_ec2()
#start_ec2()
aws_list_instances()


