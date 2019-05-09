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

j=get_ec2_client().describe_instances()
i=get_ec2_client().describe_instances()['Reservations']
ec2_l=[]
for c in range(len(i)):
    for d in i:
        #ec2_l.append(d['Instances'][c]#['PublicDnsName'])
        ec2_l.append(d['Instances'][c]['PublicDnsName'])
        ec2_l.append(d['Instances'][c]['State']['Name'])
        ec2_l.append(d['Instances'][c]['PublicIpAddress'])
        ec2_l.append(d['Instances'][c]['PrivateIpAddress'])
        ec2_l.append(d['Instances'][c]['InstanceId'])
        ec2_l.append(d['Instances'][c]['ImageId'])
        print ec2_l

"""

r=get_ec2_client().describe_regions()
print r.get('Regions')
#help (dict.iterkeys)
#print type(r['Regions'])
l=[]
for c in r.iterkeys():    # dict
    for i in r['Regions']: #list
        #print type(i)      # dict
        #print " {:39} : {} ".format(i.get('Endpoint'),i.get('RegionName'))
        l.append(i['Endpoint'])
        l.append(i['RegionName'])

print l.sort()

        #kl.append((i.get('Endpoint'),i.get('RegionName'))
        #print i.get('Endpoint')
        #print i.get('RegionName')
        #print i['Endpoint'],i['RegionName']           # dict
"""