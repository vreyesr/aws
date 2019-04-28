#!/usr/bin/python
'''
    NAME
        manage_ec2.py - For EC2 utility at AWS

    AUTHOR
        Valentin Reyes
'''

__version__ = '20190427.1'

import boto3
import json


def get_ec2_client():
    ec2 = boto3.client('ec2')
    """:type pyboto3:ec2 """
    return ec2
def get_ec2_resource():
    ec2 = boto3.resource('ec2')
    """:type : pyboto3.ec2"""
    return ec2

def get_rds_client():
    rds = boto3.client('rds')
    """:type : pyboto3.rds """
    return rds
"""
print dir(get_ec2_client())
print type(get_ec2_client())
print get_ec2_client()
print get_ec2_client().describe_instances()
print get_ec2_client().describe_instances()['Reservations'][0]['Instances']
print type( get_ec2_client().describe_instances())
"""

print type(get_rds_client())

print get_rds_client().describe_db_instances()
