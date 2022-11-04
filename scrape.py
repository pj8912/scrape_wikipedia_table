import requests
from bs4 import BeautifulSoup
import time
import sys

def download_image(url, file_name):
  
    response = requests.get(url)

    try:
        if response.status_code == 200:
            with open(file_name, "wb") as f:
                f.write(response.content)
                print(file_name," downloaded!")
    except KeyboardInterrupt:
        sys.exit()

BASE_URL = 'https://no.wikipedia.org'
url = 'https://no.wikipedia.org/wiki/Norges_kommuner'
soup = BeautifulSoup(requests.get(url).text ,  "xml")

try:

    for tag in soup.select("td:nth-of-type(8) img"):
        
        #attributes = tag.attrs get attributes of the tag
        
        image_url  = "https:"+tag["src"]
    
        alt = tag["alt"]
    
        filename = alt.split(' ')[0]+".png"
    
        download_image(image_url, filename)

     
except KeyboardInterrupt:
    sys.exit()
