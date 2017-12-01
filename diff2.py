#!/usr/bin/python

import json
from pprint import pprint

lwb_data = json.load(open('lww.json'))

#pprint(lwb_data)
#print(lwb_data["facets"]["customers"]["buckets"])

lwb_records = lwb_data["facets"]["customers"]["buckets"]

lwb_hash = {}
lwb_customer_count = 0
for lwb_record in lwb_records:
  lwb_customer_count +=1
  lwb_hash[lwb_record["val"]] = lwb_record["orderCount"]
  

# check if input into has was successful
#for key in lwb_hash.keys():
#  print "key: " + str(key) + " value: " + str(lwb_hash[key]) + "\n"

# testing for existence of key
#if 7401 in lwb_hash.keys():
#  print "key exists and it's value is: " + str(lwb_hash[7401])
#else:
#  print "doesn't exist"

lww_data = json.load(open('lwb.json'))

lww_records = lww_data["facets"]["customers"]["buckets"]
lww_not_in_lwb = {}
matches = 0
lww_customer_count = 0
for lww_record in lww_records:
  lww_customer_count+=1
  if lww_record['val'] in lwb_hash.keys():
    matches+=1
  else:
    lww_not_in_lwb[lww_record['val']] = lww_record["orderCount"]

print "lww customer count: " + str(lwb_customer_count)
print "lwb customer count: " + str(lww_customer_count)
print "There were " + str(matches) + " matches\n"

print "lwb customers not in lww:"
for key in lww_not_in_lwb.keys():
  print "customer: " + str(key) + " orderCount: " + str(lww_not_in_lwb[key]) + "\n"
