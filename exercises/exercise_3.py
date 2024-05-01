# Exercise 3
# Your solution comes here
import math

hours = 0
minutes = 0

secs = int(input("Enter seconds: "))
hours = math.floor((secs / 3600) % 24)
secs = secs % 3600
print(secs)
if secs > 60:
        minutes = math.floor(secs / 60)
        secs = secs % 60

h = str(hours)
m = str(minutes)
if minutes < 10:
        m = "0" + m
s = str(secs)
if secs < 10:
        s = "0" + s
        
print(h + ":" + m + ":" + s)