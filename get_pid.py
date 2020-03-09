#!/usr/bin/env python

import os
searchstring="get-iplayer --type radio --listformat='<name> <episode> <channel>\\<desc>| <pid>' \".*\""

fil=os.popen(searchstring)
ff=fil.readlines()
d={}
for ix in ff:
    if ( ix.find('Radio 4')>0 or ix.find('Radio 3') >0) \
    and not ix.startswith('Added'):
       pid=ix[-9:-1]
       txt=ix.split('|')[0]
       print txt,pid
       d[txt]=pid
#
l=sorted(d) # sorted dictionary keys in a list

tempfile=open("/tmp/tst2",mode='w',buffering=0) # a separate temp file
#
for k in d:
     tempfile.write(k+"\t"+d[k]+'\n') 
     if k.startswith('Prayer for the') or k.startswith('Today')\
        or k.startswith('News') or  k.startswith('Tweet of the') \
        or k.startswith('The Archers') \
        or k.startswith('Shipping Forecast')\
        or k.startswith('Yesterday in Parliament') \
        or k.startswith('World at One') \
        or k.startswith('Home Front -') \
        or k.startswith('Farming Today') \
        or k.startswith('Midnight News') \
        or k.startswith('PM - ') \
        or k.startswith('Daily Service ') \
        or k.startswith("Six O'Clock News") \
        or k.startswith('The World Tonight ') \
        or k.startswith("Woman's Hour") \
        or k.startswith('Afternoon on 3: BBC') \
        or k.startswith('Breakfast - ') \
        or k.startswith('Essential Classics') \
        or k.startswith('In Tune - ') \
        or k.startswith('Late Junction - ') :
         del k
tempfile.flush()
tempfile.close()

print "List written on", tempfile.name
print 80*'=','\n\n'
"""
Now go through the dictionary and select

"""
pids=[] # list of pids
l=sorted(d) # sorted dictionary keys in a list AGAIN as the list is now shorter
for key in l:
    yn=raw_input(key+" Y/N? ")
    if yn=="Y" or yn=="y" or yn=="1" :  #  blank line or anything else- ignore
        pids.append(d[key])
    else:
        del key
print "Selected"
for i in l :     # all selected values
    print i
"""
    Output line
"""
print 80*'=','\n\n'


pidlist=",".join(pids)
print pidlist

runstring="get-iplayer --type radio --get  --pid %s" %(pidlist)

print runstring

runit=raw_input("Shall I run it Y/N?")
if runit=="Y" or runit =="y" or runit=="1":
    os.system(runstring)
