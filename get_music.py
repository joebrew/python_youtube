import urllib2
import re
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import re
import sys
import urllib
import urlparse
import httplib2
import pafy
import os

#####
# SET WORKING DIRECTORIES
#####
code_dir = '/home/joebrew/Documents/python_youtube'
download_dir = '/home/joebrew/Music/downloaded_mp4s'
output_dir = '/home/joebrew/Music/converted_mp4s'
os.chdir(download_dir)

#####
# SEARCH STRING
#####
search_string = ['cheikh lo flavia coelho', 'king ayisoba buffalo soldier']
# Make this loopable

#####
# GET LINK
# Adapted from http://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
#####
for search_text in search_string:
	query_string = urllib.urlencode({"search_query" : search_text})
	r = requests.get("http://www.youtube.com/results?" + query_string)
	soup = BeautifulSoup(r.content)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', r.content)

	link = "http://www.youtube.com/watch?v=" + search_results[0]

	#####
	# GET VIDEO
	##### 
	video = pafy.new(link)

	# Examine options
	streams = video.streams
	for s in streams:
		print s
		print s.url

	# Get best
	best = video.getbest(preftype = 'mp4')
	best_url = best.url

	# Download
	f = best.download(quiet=False,
		filepath = download_dir)

# Script for converting to mp3
os.chdir(code_dir)
execfile('convert_mp4_to_mp3.py')

# Convert to mp3
convert_mp4_to_mp3(indir = download_dir, outdir = output_dir)
