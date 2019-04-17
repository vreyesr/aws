#!/usr/bin/python
import boto3


def aws_list_instances():
    ec2 = boto3.client('ec2')
    response=ec2
    print response.describe_instances()


aws_list_instances()
