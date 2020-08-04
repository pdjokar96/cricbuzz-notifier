import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# Live Score feed from Cricinfo
URL = "http://static.cricinfo.com/rss/livescores.xml"

# Fetch the contents of the feed.
response = requests.get(URL)

# Success/ Failure status
if response.status_code == 200:
	print('Successfully loaded the Cricinfo feed.')

else :
	print('Check Internet Connection')

# Take the User's input for the Country.
country = input('Which country\'s score do you want? : ')
toaster = ToastNotifier()

# Parse the xml.
bsoup = BeautifulSoup(response.content,'lxml')

count = 0
# Search for the country and notify the scores.
for score in bsoup.findAll('item'):
	match = score.find('title').getText()
	if country in match:
		count += 1
		toaster.show_toast(match)


if count == 0:
	toaster.show_toast('No live matches for ' + country)