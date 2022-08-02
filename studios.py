import requests
import time
import random

while True == True:
    
    # generates random studio code
    number = random.randint(0, 32000000)
    
    # gets the text from the selected studio
    info = requests.get("https://api.scratch.mit.edu/studios/"+ str(number))
    
    # if the studio exists, it prints the studio number
    if info != '{"code":"NotFound","message":""}':
        
        print(number)
    
    # sleepy sleep time to prevent overload
    time.sleep(3)