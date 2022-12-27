
from machine import Pin
led=Pin(10,Pin.OUT)
led1= Pin(13,Pin.OUT)#create LED object from pin13,Set Pin13 to output


led.value(0)            #Set led turn on
led1.value(0)
  
  
email = "qwer@gmail.com"
pswd = "1234"

einput = input("enter your email : ")

if einput == email :
    pinput = input("Enter your pswd : ")
    if pinput == pswd :
        print("Login Successful")
        led.value(1)
        led1.value(0)
    else :
        print("Wrong password!!")
        led.value(0)
        led1.value(1)
else : 
    print("Login failed!!")
    led.value(0)
    led1.value(1)
    

             
