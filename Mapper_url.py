#!/usr/bin/env python
"""mapper.py"""

import sys
import csv
count=0


cols = 'reviewerID,asin,reviewerName,helpful,reviewText,overall,summary,unixReviewTime,reviewTime'.split(',')
# input comes from STDIN (standard input)
for line in sys.stdin:
        row = dict(zip(cols, [ a.strip() for a in next(csv.reader([line]))]))
        if(int(row['overall'])  == 5 ):
            print (row['reviewerID'] + "\t" + row['reviewerName'] +  "\t"  + row['overall'] + "\t" + row['reviewTime'])
