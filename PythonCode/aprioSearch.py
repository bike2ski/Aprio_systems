import csv
import json
from elasticsearch import Elasticsearch
import click
import math
from pprint import pprint

lst = []

@click.command()
@click.argument('query', required=True)
@click.option('--raw-result/--no-raw-result', default=False)
def search(query, raw_result):
	queryValue = 0
	totalHitValue = 0
	es = Elasticsearch()
	query = 'article_text:' + query
	matches = es.search('article', q=query)
	hits = matches['hits']['hits']
	lst = readInTonalDict()
	if not hits:
		click.echo('No matches found')
	else:
		if raw_result:
			click.echo(json.dumps(matches, indent=4))
		#for hit in hits:
			#totalHitValue += analyze(hit['_source']['results'][0], query, lst)
			#print totalHitValue
		totalHitValue = analyze(hits, query, lst)
		print findQueryValue(totalHitValue, len(hits))

def readInTonalDict():
	with open("fixed_tonal.csv", "rb") as my_file:
		reader = csv.reader(my_file)
		lst = list(reader)
		return lst

def findQueryValue(totalHitValue, numHits):
	final = totalHitValue/numHits
	print final
	if final > -2 and final < 2:
		return ' neutral'
	elif final > 1 and final < 8:
		return ' positive'
	elif final < -1 and final > -8:
		return ' negative'
	elif final > 7:
		return ' very positive'
	else:
		return ' very negative'

def analyze(hits, query, lst):
	initialValue = 0
	for hit in hits:
		hit = hit['_source']['results'][0]
		try:
			title = hit['title']
			text = hit['article_text']
		except KeyError:
			continue
		text = title + ' ' + text
		for word in text.split(" "):
			row = findElem(word, lst)
			#lst = readInTonalDict()
			if row != -1:
				#hitLength = len(text)
				#print text.index(query)
				#proximity = text.index(query) - text.index(word)
				#proximity = fabs(proximity)
				#weight = findWeight(hitLength, proximity)
				try:
					initialValue = initialValue + int(float(lst[row][4]))
				except ValueError:
					print "Value Exception " + lst[row][4] + ' \n'
					continue
	return initialValue


def findWeight(hitLength, proximity):
	return (hitLength/proximity)/hitLength


def findElem(elem, lst):
	#lst = readInTonalDict()
	for row, i in enumerate(lst):
		try:
			column = i.index(elem)
		except ValueError:
			continue
		return row
	return -1


def build_structure(data, d=[]):
    if 'children' in data:
		for c in data['children']:
			d.append({'title': c.get('title', 'No title'),
				'uri': c.get('uri', None)})
			build_structure(c, d)
			return d


if __name__ == '__main__':
	search()
