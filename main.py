"""
In this module we are going to make an greeting module using time module and by using of if else conditions for the Greertings;

Such as:



"""
# Importing the Local Time Functions
import time
ct=time.localtime() # Taking Current Time from Local Machine
formatted_Hour = int(time.strftime("%H", ct))
formatted_Min = int(time.strftime("%M", ct))
formatted_Sec = int(time.strftime("%S", ct))
print("current time is:- " + str(formatted_Hour) + ":"+  str(formatted_Min) + ":" + str(formatted_Sec) )

# Let's get the condiotional Check:
# Morning Check
if(formatted_Hour <=12):
    if(formatted_Hour>=0):
        print("Good Morning Sir! May Allah Bless Your Day")
elif(formatted_Hour==12):
    print("Good Noon Sir, Its now Noon Take your Shower Soon!!")
          
# Noon Check
elif(formatted_Hour>12 and formatted_Hour<=17):
    if(formatted_Hour<17):
        print("Good Afternoon Sir!")
    else:
        print("Its Still Noon Sir! Take Proper Rest Sir!")

# Night Check
else:
    print("Good Night Sir!")


