#!/usr/bin/env python
import sys
import time
import datetime
# input comes from STDIN (standard input) 
for line in sys.stdin:
    # remove leading and trailing whitespace 
    line = line.strip()
    words = line.split('[')
    if len(words) > 1:
    	words = words[1].split(' -0400')
    	time = datetime.datetime.strptime(words[0], "%d/%b/%Y:%H:%M:%S")
    	print time.strftime('%Y,%m,%d,%H')+"\t1"
