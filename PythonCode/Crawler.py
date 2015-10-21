# This file will kick off the crawlers
from array import array
from subprocess import call

class Crawler():


	def __init__(self):
		self.crawlers=[]

	def addCrawler(self, filename):
		self.crawlers.append(filename)

	def getCrawlers(self):
		print self.crawlers

	def startCrawler(self):
		print 'Starting Crawlers'
		for crawler in self.crawlers:
			function = '../../import.io -crawl ../crawlers/' + crawler + ' ../crawlers/crawl_auth.json'
			print function + ' here is function call'
			call(function, shell=True)
		#print commands
		#for cmd in commands:
		#	Popen(cmd, shell=True)
		#processes=[]
		#for cmd in commands:
		#	processes.append(Popen(cmd, shell=True))
		#	for p in processes: p.wait()