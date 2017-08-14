## coding: utf-8
import nltk
from nltk import ngrams
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import matplotlib.pyplot as plt
import operator
import sys
from collections import Counter

import os
import requests
import urllib2
import numpy
import itertools
import csv
import json
import time

from nltk.util import ngrams
from nltk.collocations import *


from shutil import copy
from nltk import ngrams
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import matplotlib.pyplot as plt
import operator
import sys
#print(sys.version_info)
from collections import Counter
from bs4 import BeautifulSoup, NavigableString
import os
import requests
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
# import lxml.html
from urllib import urlopen
from urlparse import urlparse
import numpy
import itertools
import csv
import json
import time
#===========================================================================
def clean(text_file):
    text_file = text_file.replace(',', '')
    text_file = text_file.replace('Join today and you can easily save your favourite articles join in the', '')
    text_file = text_file.replace('conversation and comment, plus select which news your want direct to your', '')
    text_file = text_file.replace('86\xc2\xb0', '')
    text_file = text_file.replace('Samsung\'s Bigger-Screen Galaxy Note 8 Smartphone Could Launch on August 23', '')
    text_file = text_file.replace('You Can Now Buy a Nokia 6 Android Smartphone in the United States via', '')
    text_file = text_file.replace('Apple Beats Microsoft as Siri Remains Top Digital Assistant Despite', '')
    text_file = text_file.replace('via Amazon', '')
    text_file = text_file.replace('Cortana Push', '')
    text_file = text_file.replace('Meet Noodle Pi, a Raspberry Pi-Based DIY Pocket Computer Powered by', '')
    text_file = text_file.replace('GNU/Linux Meet Noodle Pi, a Raspberry Pi-Based DIY Pocket Computer Powered', '')
    text_file = text_file.replace('by GNU/Linux', '')
    text_file = text_file.replace('Google\'s Backup and Sync App Is Here, Works with Google Drive and Google', '')
    text_file = text_file.replace('ASUS Launches Chromebook Flip C213 as Ultimate Future-Proof Education', '')
    text_file = text_file.replace('These are external links and will open in a new window', '')
    text_file = text_file.replace('-', '')
    text_file = text_file.replace('Download the Windows 7 SP1 KB4025341 and Windows 8.1 KB4025336', '')
    text_file = text_file.replace('This document may be found here', '')
    text_file = text_file.replace('* Terms of Use', '')
    text_file = text_file.replace('The document has moved here .', '')
    text_file = text_file.replace('* Back to Main Menu', '')
    text_file = text_file.replace('Share this with Facebook', '')
    text_file = text_file.replace('April 21, 2014', '')
    text_file = text_file.replace('February 5, 2014', '')
    text_file = text_file.replace('February 4, 2014', '')
    text_file = text_file.replace('Compliance', '')
    text_file = text_file.replace('\xe2\x80\xa2', '')
    text_file = text_file.replace('68\xc2\xb0', '')
    text_file = text_file.replace('86\xc2\xb0', '')
    text_file = text_file.replace('\xc2\xb7', '')
    text_file = text_file.replace('eu\xe2\x80\x99s', '')
    text_file = text_file.replace('moved permanently', '')
    text_file = text_file.replace('\xe2\x80\x99ll', '')
    text_file = text_file.replace('9 2017', '')
    text_file = text_file.replace('&', '')
    text_file = text_file.replace('* Share on Facebook', '')
    text_file = text_file.replace('* Politics', '')
    text_file = text_file.replace('* Business', '')
    text_file = text_file.replace('* Sports', '')
    text_file = text_file.replace('* Travel', '')
    text_file = text_file.replace('\xe2\x96\xba', '')
    text_file = text_file.replace('* HOME', '')
    text_file = text_file.replace('* News', '')
    text_file = text_file.replace('* Privacy Policy', '')
    text_file = text_file.replace('* Health', '')
    text_file = text_file.replace('* World', '')
    text_file = text_file.replace('* Contact Us', '')
    text_file = text_file.replace('* Opinion', '')
    text_file = text_file.replace('* Jobs', '')
    text_file = text_file.replace('* Videos', '')
    text_file = text_file.replace('* Music', '')
    text_file = text_file.replace('* Twitter', '')
    text_file = text_file.replace('* Weather', '')
    text_file = text_file.replace('* Education', '')
    text_file = text_file.replace('* Contact us', '')
    text_file = text_file.replace('* Events', '')
    text_file = text_file.replace('All Rights Reserved', '')
    text_file = text_file.replace('* National', '')
    text_file = text_file.replace('* Subscribe', '')
    text_file = text_file.replace('* News', '')
    text_file = text_file.replace('* Share on Twitter', '')
    text_file = text_file.replace('* Autos', '')
    text_file = text_file.replace('[ Submit ]', '')
    text_file = text_file.replace('[IMG]', '')
    text_file = text_file.replace('[ ]', '')
    text_file = text_file.replace('[ Save ]', '')
    text_file = text_file.replace('[ Subscribe ]', '')
    text_file = text_file.replace('[…]', '')
    text_file = text_file.replace('[ Search ]', '')
    text_file = text_file.replace('●', '')
    text_file = text_file.replace('[ Reblog Post ]', '')
    text_file = text_file.replace('The document has moved here .', '')
    text_file = text_file.replace('* Share on Twitter', '')
    text_file = text_file.replace('(Ubuntu)', '')
    text_file = text_file.replace('Link: canonical', '')
    text_file = text_file.replace('301 Moved Permanently', '')
    text_file = text_file.replace('nginx', '')
    text_file = text_file.replace('* Share this with Messenger', '')
    text_file = text_file.replace('Share this with Messenger', '')
    text_file = text_file.replace('Link: canonical', '')
    text_file = text_file.replace('0 obj < >stream', '')
    text_file = text_file.replace('Link: shortlink', '')
    text_file = text_file.replace('* Home', '')
    text_file = text_file.replace('* Entertainment', '')
    text_file = text_file.replace('* Sport', '')
    text_file = text_file.replace('* Facebook', '')
    text_file = text_file.replace('* Video', '')
    text_file = text_file.replace('All rights reserved.', '')
    text_file = text_file.replace('* November', '')
    text_file = text_file.replace('* Security', '')
    text_file = text_file.replace('* Contests', '')
    text_file = text_file.replace('* March', '')
    text_file = text_file.replace('* Share on', '')
    text_file = text_file.replace('* Arts', '')
    text_file = text_file.replace('* Local', '')
    text_file = text_file.replace('* Property', '')
    text_file = text_file.replace('* Classifieds', '')
    text_file = text_file.replace('* August', '')
    text_file = text_file.replace('* About', '')
    text_file = text_file.replace('* CBeebies', '')
    text_file = text_file.replace('?', '')
    text_file = text_file.replace('!', '')
    text_file = text_file.replace('@', '')
    text_file = text_file.replace('#', '')
    text_file = text_file.replace('$', '')
    text_file = text_file.replace('%', '')
    text_file = text_file.replace('^', '')
    text_file = text_file.replace('&', '')
    text_file = text_file.replace('*', '')
    text_file = text_file.replace('(', '')
    text_file = text_file.replace(')', '')
    text_file = text_file.replace('_', '')
    text_file = text_file.replace('+', '')
    text_file = text_file.replace('}', '')
    text_file = text_file.replace('{', '')
    text_file = text_file.replace('"', '')
    text_file = text_file.replace(':', '')
    text_file = text_file.replace('?', '')
    text_file = text_file.replace('>', '')
    text_file = text_file.replace('<', '')
    text_file = text_file.replace('|', '')
    text_file = text_file.replace(']', '')
    text_file = text_file.replace('[', '')
    text_file = text_file.replace(';', '')
    text_file = text_file.replace('/', '')
    text_file = text_file.replace('-', '')
    text_file = text_file.replace('=', '')
    text_file = text_file.replace('`', '')
    text_file = text_file.replace('~', '')
    text_file = text_file.replace('.', '')
    text_file = text_file.replace('?', '')
    text_file = text_file.replace('\:', '')
    text_file = text_file.replace('ï', '')
    text_file = text_file.replace('¿', '')
    text_file = text_file.replace('½', '')
    text_file = text_file.replace('Ø', '')
    text_file = text_file.replace('×', '')
    text_file = text_file.replace('¹', '')
    text_file = text_file.replace('Þ', '')
    text_file = text_file.replace('Å', '')
    text_file = text_file.replace('¥', '')
    text_file = text_file.replace('Ê', '')
    text_file = text_file.replace('Þ', '')
    text_file = text_file.replace('Ú', '')
    text_file = text_file.replace('Ñ', '')
    text_file = text_file.replace('Ë', '')
    text_file = text_file.replace('_', '')
    text_file = text_file.replace('è', '')
    return text_file

def compare(n_gram1, n_gram2):
#    n_gram1 = append_elements(n_gram1)
#    n_gram2 = append_elements(n_gram2)
    number = 0
    common = []
    for phrase in n_gram1:
        if phrase in n_gram2:
            common.append(phrase)
            number += 1
    if not common:
        return False
    # or you could print a message saying no commonality was found
    else:
        for i in common:
            print(i)
    return number
    print number
    g= [number]

def append_elements(n_gram):
    for element in range(len(n_gram)):
        phrase = ''
        for sub_element in n_gram[element]:
            phrase += sub_element+' '
        n_gram[element] = phrase.strip().lower()
    return n_gram












