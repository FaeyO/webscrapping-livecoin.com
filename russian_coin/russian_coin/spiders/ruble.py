import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class RubleSpider(scrapy.Spider):
    name = "ruble"
    allowed_domains = ["web.archive.org"]
    start_urls = ["https://web.archive.org/web/20200116052415/https://www.livecoin.net/en"]


    def __init__(self):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_path = which("chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1900, 1080)
        driver.get("https://web.archive.org/web/20200116052415/https://www.livecoin.net/en")

        rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        rur_tab[4].click()
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class,'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            pair = currency.xpath(".//div/div/text()").get()
            volume = currency.xpath(".//div[2]/span/text()").get()
            last_price = currency.xpath(".//div[3]/span/text()").get()
            change = currency.xpath(".//div[4]/span/span/text()").get()
            high = currency.xpath(".//div[5]/span/text()").get()
            low= currency.xpath(".//div[6]/span/text()").get()
            
            yield{
                'pair':pair,
                'volume' : volume,
                'last_price': last_price,
                'change' : change,
                'high': high,
                'low': low
            }
