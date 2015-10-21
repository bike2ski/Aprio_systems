# This file will kick off the entire aprio systems system

from Crawler import Crawler


class Aprio():

	sources = ['washPost_crawler.json', 'bbc_crawler.json', 'huffPost_crawler.json', 'sunTimes_crawler.json']
	
	def __init__(self, name, version):
		name = name
		version = version

	myCrawler = Crawler()
	print sources
	for source in sources:
		myCrawler.addCrawler(source)
	myCrawler.startCrawler()