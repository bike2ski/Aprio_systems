from Crawler import Crawler

myCrawler = Crawler()

crawlLocation="bbc_crawler.json"

myCrawler.addCrawler(crawlLocation)

myCrawler.startCrawler()
