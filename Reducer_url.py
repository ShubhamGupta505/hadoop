#!/usr/bin/env python
"""reducer.py"""

#from operator import itemgetter
import sys

current_reviewerID = None
current_count = 0
reviewerID= None
count=0
dict_rec = {}

# input comes from STDIN
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()

    

    # parse the input we got from mapper.py
    data= line.split('\t') 
   
    #reviewerID =  data[0]
    #reviewerName = data[1]
    dict_rec [data[0]] = data[2] # all the required values are taken into dictionary
'''    count = 1

    if current_reviewerID == reviewerID:
        current_count += count
        
    else:
        if current_reviewerID:
            # write result to STDOUT
            print ('%s\t%s' % (reviewerName, current_count ))
        current_count = count
        current_reviewerID = reviewerID

'''

#loop for getting maximum of the whole column
#print(dict_rec)	
max_v = 0
count_item = 0
sum_items = 0
for i in dict_rec.values():
     sum_items += int(i)
     count_item+=1
average = sum_items / count_item
print("average" , average)


#to print only those who have overall equal to or greater than average
for k , v in dict_rec.items():
    if (int(v) >= average):
        print(k , v)  
