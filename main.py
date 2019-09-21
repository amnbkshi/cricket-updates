import bs4
import textme
import time
import datetime as dt
from selenium import webdriver

URL = 'https://www.cricbuzz.com/cricket-team/india/2/schedule'

options = webdriver.FirefoxOptions()
options.headless = True
browser = webdriver.Firefox(options=options)

#loop
browser.get(URL)
html = browser.page_source
soup = bs4.BeautifulSoup(html, "html.parser")

element = soup.find('div', 
            class_ = 'cb-col-100 cb-col cb-series-matches ng-scope')

date = dt.datetime.strptime(element.div.span.text, '%b %d, %a') #split by - for test matches
team = element.find('a', class_='text-hvr-underline').span.text.strip()
venue = element.find('div', class_="text-gray cb-ovr-flo").text

time = element.find('div', class_="cb-font-12 text-gray").select('span + span')[0].text.strip()
ti = dt.datetime.strptime(time, '%I:%M %p')

message = f"Don't miss out {team} today at {time}!"

curr_time = dt.datetime.now()
send_time = dt.datetime(dt.datetime.now().year, date.month, date.day,
                     ti.hour, ti.minute)

delta = dt.timedelta(hours=5)

if (send_time - curr_time) < delta:
    #send message
    
