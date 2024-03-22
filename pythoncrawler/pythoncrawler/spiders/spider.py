import scrapy
import requests
from bs4 import BeautifulSoup


class Spider(scrapy.Spider):
    name = "example"
    start_urls = ['https://www.cnnindonesia.com/']

    def parse(self, response):
        url = response.url
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        file = open('cnn.html', 'w', encoding="utf-8")
        # GET LINK ON WEBSITES
        for link in soup.find_all('a'):
            data = link.get('href')
            file.write(data)
            file.write("\n")
        # GET ALL HTML
        file.write(response.text)
        file.close()
