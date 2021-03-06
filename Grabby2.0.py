import os 
import requests  
import re
import subprocess
import urllib2
import json
from bs4 import BeautifulSoup
from signal import signal, SIGPIPE, SIG_DFL
from zipfile import ZipFile

def choice(maxep, llist, dlist, flist):

	media = ['Movie','TV']
	language = ["English","Chinese","Arabian","French","Spanish","Danish","German","Vietnamese"]
	rangelist = xrange(1, int(maxep)+1)
	episodes = [('E' + str(s).zfill(2)) for s in rangelist]
	res = ["480p","720p","1080p","OTHER"]
	dictFilter = {}
	finallist = []
	keyDict = {'media':media,'language':language,'episodes':episodes,'res':res}
	def Choicy(typezz):
		print
		if typezz == 'media':
			msg1 = 'Media Type > '
			msg2 = 'Please select movie or tv only!'
		elif typezz == 'language':
			msg1 = 'Language > '
			msg2 = 'Please select a right language!'
		elif typezz == 'episodes':
			msg1 = 'Episode > '
			msg2 = 'Please select a correct episode number!'
		elif typezz == 'res':
			msg1 = 'Resolution > '
			msg2 = 'Please select a correct resolution!'		
		reflist = keyDict[str(typezz)]
		while True:
			countmedia = 0
			for x, i in enumerate(reflist):
				print x+1, i 
				countmedia += 1
			dictFilter[typezz] = raw_input(msg1)
			try:
					val = int(dictFilter[typezz])
			except ValueError:
		   		print "Please enter the correct selection!"
			if (val <= 0 or val > countmedia): 
				print msg2
			else: 
				final = val - 1 
				dictFilter[typezz] = reflist[final]
				break
	for i in keyDict:
		Choicy(i)
	la = zip(llist,dlist,flist)
	for i in la:
		a, b, c = i 
		if dictFilter['media'] == 'TV':
			if dictFilter['language'] in a: 
				if dictFilter['res'] != 'OTHER': 
					if dictFilter['episodes'] in b and dictFilter['res'] in b: 
						finallist.append((b,c))
				else:
					if dictFilter['episodes'] in b: 
						finallist.append((b,c))
		elif dictFilter['media'] == 'Movie':
			if dictFilter['language'] in a: 
				if dictFilter['res'] != 'OTHER':
					if dictFilter['res'] in b: 
						finallist.append((b,c))
				else: 
					finallist.append((b,c))
		
	finaldict = {}	
	print
	for i,x in enumerate(finallist):
		a, b = x 
		c = i + 1
		finaldict[c] = b
		print c, a

	while True: 
		choice = raw_input("Pick one: ")
		if not choice: 
			print "Please enter something first!" 
			continue
		try:
			val = int(choice)
		except ValueError:
		   print "Please enter the correct selection!" 
		if int(choice) < 1 or int(choice) > len(finallist): 
			print "Please enter the correct choice!"
		else: 
			print "Ok, downloading.... "
			baseurl = 'http://subscene.com/'
			url = baseurl + finaldict[int(choice)]
			subl = requests.get(url).text
			finalsoup = BeautifulSoup(subl,'html.parser')
			for link in finalsoup.find_all('a'):
				i = link.get('href')
				if '/subtitle/download' in i: 
					finallink = baseurl + i 
			basefile = 'sub' + '.zip'
			here = requests.get(finallink)
			g = open(basefile, 'wb')
			g.write(here.content)
			g.close()
			with ZipFile(basefile,'r') as zippy: 
				zippy.extractall()
			zippy.close()
			print "All done!"
			os.remove('htmlr.html')
			os.remove('choice.json')
			os.remove(basefile)
			break

def query(req):
	
	base_link = 'http://subscene.com/subtitles/title?q='
	link = base_link + req
	htmll = requests.get(link).text
	soup = BeautifulSoup(htmll,'html.parser')
	links = [i.get('href') for i in [x for x in soup.find_all('a')]]
	print 'Which one again?' 
	count = 1
	dic_count = {}
	for selection in links: 
		if ('http' not in selection and len(selection) > 2 and 'legal-information'
		 not in selection and '/site/contact' not in selection): 
			print count, selection
			dic_count[count] = selection
			count += 1
	choiced = ""		
	while True: 
		choice = raw_input("Pick one: ")
		if not choice: 
			print "Please enter something first!" 
			continue
		try:
   			val = int(choice)
		except ValueError:
		   print "Please enter the correct selection!" 
		if int(choice) < 1 or int(choice) > count: 
			print "Please enter the correct choice!" 
		else: 
			print 'Hold on, doing some funky stuffs....'
			choiced = dic_count[int(choice)]
			break
	grabjson(choiced)
	while True:
		try:
			maxep, llist, dlist, flist = readjson()
		except Exception as timeout: 
			continue
		break
	return (str(maxep), llist, dlist, flist)

def grabjson(urlz):

	baseurl = 'http://www.subscene.com/'
	urll = baseurl+urlz
	headers = { 'User-Agent' : 'Mozilla/5.0' }
	req = urllib2.Request(urll, None, headers)
	file("htmlr.html", "w").write(urllib2.urlopen(req).read())
	cmd = '''cat ./htmlr.html | pup 'tr td[class="a1"] a json{}' > choice.json '''
	cmdd = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True, preexec_fn = lambda: signal(SIGPIPE, SIG_DFL))

def readjson():
	with open('choice.json') as datafile:
		js = json.load(datafile)

	i = 0
	llist = [] 
	dlist = [] 
	flist = []
	while i < len(js):
		x = js[i]
		for xx in x:
			if xx == 'children':
				z = x[xx]
				a, b = z 
				llist.append(a['text'])
				try:
					dlist.append(str(b['text']))
				except Exception as e:
					dlist.append('Error')
					continue 		
		i+=1

	x = 0
	while x < len(js): 
		c = js[x]
		for cc in c: 
			if cc == 'href':
				flist.append(c[cc])
		x += 1 
	
	dmd = '''cat choice.json | grep -oE 'E[[:digit:]][[:digit:]]' | tr -d 'E' | sort -nr | head -n 1'''
	dmdd = subprocess.Popen(dmd,stdout=subprocess.PIPE,shell=True, preexec_fn = lambda: signal(SIGPIPE, SIG_DFL))
	maxep = dmdd.stdout.read()
	if not maxep: 
		maxep = 1
	return (str(maxep),llist,dlist,flist)

def _main_():
	reqMov = raw_input('What are you watching? : ')
	movie = ""
	for i in reqMov.split():
		movie += (i + '+')
	maxep, llist, dlist, flist = query(movie)
	returndict = choice(str(maxep), llist, dlist, flist)
_main_()
