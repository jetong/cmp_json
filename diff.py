#!/usr/bin/python
# determine diff of two json files

import json

# open first json file and dump desired data into a hash
lwb_data = json.load(open('lwb.json'))
lwb_records = lwb_data["facets"]["customers"]["buckets"]
lwb_hash = {}
lwb_customer_count = 0
for lwb_record in lwb_records:
  lwb_customer_count +=1
  lwb_hash[lwb_record["val"]] = lwb_record["orderCount"]
  
# open second json file 
# while reading record, check if the record exists in the hash created from the first json file.
lww_data = json.load(open('lww.json'))
lww_records = lww_data["facets"]["customers"]["buckets"]
lww_not_in_lwb = {}
matches = 0
lww_customer_count = 0
order_count_mismatched = {}
for lww_record in lww_records:
  lww_customer_count+=1
  if lww_record['val'] in lwb_hash.keys():
    matches+=1
    if lww_record['orderCount'] != lwb_hash[lww_record['val']]:
      order_count_mismatched[lww_record['val']] = lww_record['orderCount'] 
  else:
    lww_not_in_lwb[lww_record['val']] = lww_record["orderCount"]

# display info
print "lwb customer count: " + str(lwb_customer_count)
print "lww customer count: " + str(lww_customer_count)
print "There were " + str(matches) + " matches\n"

print "lww customers not in lwb:"
for key in lww_not_in_lwb.keys():
  print "customer: " + str(key) + " orderCount: " + str(lww_not_in_lwb[key])

print "\nCustomers that exist in lww and lwb, but with different order counts: "
for key in order_count_mismatched.keys():
  print "customer: " + str(key) + " lww orderCount: " + str(order_count_mismatched[key]) + " lwb orderCount: " + str(lwb_hash[key]) + " difference: " + str(order_count_mismatched[key]-lwb_hash[key])
