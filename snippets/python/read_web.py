import urllib2
response = urllib2.urlopen(sys.argv[1])
result = response.read()
print result
