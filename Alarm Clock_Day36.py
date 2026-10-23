#Alarm Clock:
print('='*30)
print('*****Alarm Clock*****')
print('='*30)

import time
Alarm_Hour      = int(input('Enter the Alarm Time in Hours (00 - 23):'))
Alarm_Minutes   = int(input('Enter the Alarm Time in Minutes (00 - 59):'))
Alarm_Seconds   = int(input('Enter the Alarm Time in Seconds (00 - 59):'))

def Alarm():

    print('The Alarm is set for: ' , Alarm_Hour, 'Hours', Alarm_Minutes, 'Minutes',Alarm_Seconds , 'Seconds' )
    
    while True:
        t = time.localtime()
        Current_time    = t
        Current_hour    = t.tm_hour
        Current_minute  = t.tm_min
        Current_second  = t.tm_sec

        print('\nThe Current Time is: ', Current_hour,'Hour', Current_minute,'Minutes', Current_second , 'Seconds' )
       
        if Current_hour == Alarm_Hour and Current_minute == Alarm_Minutes and Current_second == Alarm_Seconds :
            print('TIME UP....')
            break        
            
        else:
            print('Not Time up')
Alarm()
