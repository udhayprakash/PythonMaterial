#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 15:16:35 2016

@author: upethakamsetty

BOTO 3 practice
"""
__author__ = "Udhay Prakash"
__version__ = 1.0

import logging

import boto3
import botocore

# Getting connection to amazon s3
s3 = boto3.resource("s3")
print(("\n\n\n s3 connection created -> " + str(s3)))

"""
print "\n dir(s3)"
for i in dir(s3):
    print "dir(s3)", i

# Print Out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
# ? How to get the number of buckets in s3
# totalBuckets = s3.buckets.all()
# print "Total Number of buckets is ", len(totalBuckets)

# Creating a new s3 bucket
try:
    s3.create_bucket(Bucket='mybucket')
    s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-1'})
except botocore.exceptions.ClientError,e:
    print "\n You have attempted to create more buckets than allowed"
    print e



# Storing data in an s3 bucket
s3.Object('myOrg-hyd-appdata-us-east-1', 'communicaton ports.png').put(Body=open('C:\\Users\\upethakamsetty\Pictures\communicaton ports.png', 'rb'))
# Common Gotcha.. should not place the complete url -
#     'https://s3.amazonaws.com/myOrg-hyd-appdata-us-east-1'

"""

# Accessing a Bucket
# Existence of a bucket is NOT automatically VALIDATED in s3
bucket = s3.Bucket("myOrg-hyd-appdata-us-east-1")
exists = True
try:
    s3.meta.client.head_bucket(Bucket="myOrg-hyd-appdata-us-east-1")
except botocore.exceptions.ClientError as e:
    # If a client error is thrown, then check that it was a 404 error.
    # If it was a 404 error, then the bucket does not exist.
    error_code = int(e.response["Error"]["Code"])
    if error_code == 404:
        exists = False

for index, key in enumerate(bucket.objects.all()):
    print(key)
print(("Total Number of keys in this bucket is ", index))

# Iteration of Buckets and Keys
for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        print((key.key))

# Access Controls
bucket.Acl().put(ACL="public-read")
obj.Acl().put(ACL="public-read")

# retrieving policy grant myOrgmation
acl = bucket.Acl()
for grant in acl.grants:
    print((grant["Grantee"]["DisplayName"], grant["Permission"]))

# Adding Grantees
bucket.Acl.put(GrantRead="emailAddress=user@domain.tld")
# setting metadata
key.put(Metadata={"meta1": "This is my metadata value"})
print((key.metadata["meta1"]))
