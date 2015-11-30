#!/usr/bin/env python
# __author__ = 'ruben'

#Import the modules
import requests
import json

# Get the feed
r = requests.get("http://en.wikipedia.org/w/api.php?format=json&action=query&titles=India&prop=revisions&rvprop=content&callback=?")
r.text

# Convert it to a Python dictionary
data = json.loads(r.text)

print (data)

# Loop through the result.
for item in data['data']['items']:
    print "Video Title: %s" % (item['title'])
    print "Video Category: %s" % (item['category'])
    print "Video ID: %s" % (item['id'])
    print "Video Rating: %f" % (item['rating'])
    print "Embed URL: %s" % (item['player']['default'])
    print
