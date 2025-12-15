
import requests
import mrich
from mrich import print
import re
from requests_html import HTMLSession

AUDI_URL = "https://www.cazoo.co.uk/cars/audi/a3/?postcode=GU22+7TQ"

def scrape(url):

	print(url)

	session = HTMLSession()
	headers = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
	                  "AppleWebKit/537.36 (KHTML, like Gecko) "
	                  "Chrome/122.0.0.0 Safari/537.36"
	}

	response = session.get(url, headers=headers)
	response.html.render(timeout=30)  # renders JavaScript
	
	print(response)
	# print(response.html.html[:1000])  # view first 1000 chars

	with open("test.html", "wt") as f:
		f.write(response.html.html)

	# mrich.var("url", url)

	# response = requests.get(url)

	
def main():
	scrape(AUDI_URL)

if __name__ == '__main__':
	main()