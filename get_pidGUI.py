#!/usr/bin/env python
# -*- coding: utf-8 -*-'
import os
searchstring="get-iplayer --type radio --listformat='<name> <episode> <channel>\\<desc>| <pid>' \".*\" "

fil=os.popen(searchstring)
print "Opened file"
ff=fil.readlines()
print "Read file"
d={}
for ix in ff:
    if ( ix.find('Radio 4')>0 or ix.find('Radio 3') >0) \
    and not ix.startswith('Added'):
       pid=ix[-9:-1]
       txt=ix.split('|')[0]
       text2=txt.decode('ascii',errors='ignore') # fix for unicode
       print text2,pid #unicode
       d[text2]=pid   #see if it works
#
l=sorted(d) # sorted dictionary keys in a list

tempfile=open("/tmp/tst2",mode='w',buffering=0) # a separate temp file
#
for k in l:
     if k.startswith('Prayer for the') or k.startswith('Today')\
        or k.startswith('News ') or  k.startswith('Tweet of the') \
        or k.startswith('The Archers ') \
        or k.startswith('Shipping Forecast ')\
        or k.startswith('Yesterday in Parliament') \
        or k.startswith('Today in Parliament') \
        or k.startswith('World at One') \
        or k.startswith('Home Front -') \
        or k.startswith('Farming Today') \
        or k.startswith('Midnight News ') \
        or k.startswith('PM ') \
        or k.startswith('Daily Service ') \
        or k.startswith("Six O'Clock News ") \
        or k.startswith('Weather ') \
        or k.startswith('The World Tonight ') \
        or k.startswith("Woman's Hour") \
        or k.startswith('The Listening Project') \
        or k.startswith('You and Yours') \
        or k.startswith('Afternoon on 3 ') \
        or k.startswith('The Comedy Club') \
        or k.startswith('Breakfast  ') \
        or k.startswith('Essential Classics') \
        or k.startswith('In Tune ') \
        or k.startswith('Selection of BBC World') \
        or k.startswith('Essential Classics ') \
        or k.startswith('Inheritance Tracks ') \
        or k.startswith('Late Junction ') :
         del d[k]
     else:
         tempfile.write(k+"\t"+d[k]+'\n') 
tempfile.flush()
tempfile.close()

print "List written on", tempfile.name
print 80*'=','\n\n'
"""
Now go through the dictionary and select

"""
pids=[] # list of pids

l=sorted(d) # sorted dictionary keys in a list AGAIN as the list is now shorter

"""
for key in l:
    yn=raw_input(key+" Y/N? ")
    if yn=="Y" or yn=="y" or yn=="1" :  #  blank line or anything else- ignore
        pids.append(d[key])
    else:
        del key
"""
import easygui as eg

keylist=eg.multchoicebox(msg="Select programs",title="BBC radio",choices=l)
for k in keylist :
    pids.append(d[k])

pidlist=",".join(pids)

runstring="get-iplayer --type radio --get  --pid %s" %(pidlist)

print runstring
os.system(runstring)
