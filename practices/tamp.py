# import subprocess
#
# file = open("file.txt","w")
# file.write("Hello world")
# file.close()
#
# subprocess.Popen(['start','file.txt'], shell=True)

import requests
from bs4 import BeautifulSoup
import threading
import subprocess

def scrape(year):
    url = "https://www.ultratop.be/nl/annual.asp?year="+str(year)

    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    div_tags = soup.find_all('div',{'class':'chart_title'})

    file = open("files/charts_" + str(year)+".txt","w", encoding="utf-8")
    for tag in div_tags:
        file.write(tag.get_text().strip())
    file.close


start = int(input("Start year"))
end = int(input("End year"))

for year in range(start,end+1):
    thread = threading.Thread(target=scrape(year))
    thread.start()


scrape(1999)