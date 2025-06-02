# SDM: This program will take in user input in the
# format of HH:MM where the digits can represent any
# valid 12 hour clock time, so for example, 01:59
# would be 01:59 AM or PM. After taking in a time,
# 1 more user input will be a positive integer which
# ticks the clock forward that many minutes & display
# the new time. Program will politely & clearly ask
# the user to put in the required info

# get user input  for start  time and add time
user_time = input("Welcome to Clock Tick, please enter a set time in HH:MM format: ")
add_time = int(input("Please enter how  much  time you would like to  add: "))
# split the hours and minutes to create HH:MM format
h,  m =  user_time.split(":")
h  = int(h)
m = int(m)
# this adds the new min to start min
m  =  m  + add_time
# this  creates the  minute loop  as  well as changing the hour
if m >= 60:
    h = h + (m // 60)
    m = m % 60
# this creates the 12 hour time loop
if h > 12:
    h = h // 12
# print the new time
print(f"In {add_time} minutes, it will be : {h:02}:{m:02}")











