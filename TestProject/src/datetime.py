'''
Created on Jul 8, 2017

@author: iyyam
'''
import time; # This is required to include time module.
#import calendar

ticks = time.gmtime()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

#cal = calendar
print ("Here is the calendar:")
#print (cal)