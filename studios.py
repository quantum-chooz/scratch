import requests
import time
import random
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

while True == True:
    
    # generates random studio code
    number = random.randint(0, 32000000)
    
    try:
        # opens webpage
        url = "https://api.scratch.mit.edu/studios/" + str(number)
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")

        for script in soup(["script", "style"]):
            script.extract()
    
        text = soup.get_text()
        
        # if the studio exists, it prints the studio number
        if str(text).startswith('{'):
        
            print(number)
        
    # exception handling for if the page doesn't exist
    except HTTPError:
        
        pass
    
    # sleepy sleep time to prevent overload
    time.sleep(1)
