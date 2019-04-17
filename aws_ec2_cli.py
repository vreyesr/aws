#!/usr/bin/python
import boto3
import json


def aws_list_instances():
    ec2 = boto3.client('ec2')
    response=ec2
    #print  json.dumps(response.describe_instances()['Reservations'])
    for instances in response.describe_instances()['Reservations'][0]['Instances']:
        for keys in instances.keys():
            print "%s : %s" %( keys, instances[keys])

aws_list_instances()
