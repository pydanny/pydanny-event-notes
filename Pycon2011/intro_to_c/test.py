#!/usr/bin/env python
import cgi
import sys

params = cgi.parse_qs(sys.stdin.read())
print 'Hello %s!'%(params['name'][0])
