import feedparser
import re
from django.shortcuts import render


def index(request): 
	#BASE index is Business
	url = 'https://www.wired.com/feed/category/business/latest/rss'
	#url = 'https://www.wired.com/feed/category/ideas/latest/rss'
	feed = feedparser.parse(url)
	return render(request, 'rss/reader.html', {
	'feed': feed
	})
	   
	"""
	llist = feed['items']
	for l in llist:
		print(l) 

	entry = feed.entries[1]
	print(type(entry))
	print(entry.keys())
	"""



