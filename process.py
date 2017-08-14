# coding: utf-8
import clean as c
from nltk import ngrams
from nltk import FreqDist
import shutil
import os
from shutil import copy
import pandas as pd
import numpy as np
#copyfile(src, dst)
import numpy as np
import matplotlib.pyplot as plt
import operator
import sys
#print(sys.version_info)
from collections import Counter
from bs4 import BeautifulSoup, NavigableString
import os, errno
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
# Reading file

df = pd.read_csv("datafinal.csv",index_col = None)
#for i in df["Tag"]:
#    #print i
#    for w in str(i).replace(':',' ').split():
#        if w == 'Breach':
#            #print df['Tag'].index.tolist()
#            print df.loc[df['Tag'].index.tolist(), 'Name']

Tags = ['Breach','PHIDBR2018','Misuse','Autocode-Test','Physical','Malware','Defacement','DOS','Hacking','pinboardimport','HOF-2014','Social','Mining','POS','Error','Outage','Update']
def Tag_filter(x):
    Tag_list = []
    for j in range(0,4215):
        #print df.iloc[j,0]
        #print df.iloc[j,0].replace(':',' ').split()
        try:
            if df.iloc[j,0].replace(':',' ').split()[0] == x or df.iloc[j,0].replace(':',' ').split()[1] == x or ordf.iloc[j,0].replace(':',' ').split()[2] == x or df.iloc[j,0].replace(':',' ').split()[3] == x:
                Tag_list.append(df.iloc[j,1])
        except:pass
    return Tag_list

for w in Tags:
    newpath = '222/'+str(w)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for i in Tag_filter(w):
        print str(i)
        src = '222/'+str(i)
        dst = '222/'+str(w)+'/'
        print dst
        try: copy(src, dst)#print prevname
        except: pass
    os.system("cd /Users/jansherkhan/Desktop/Fold2/222/"+str(w)+"/;cat *.txt > Alltext.txt")
    f = open('/Users/jansherkhan/Desktop/Fold2/222/'+str(w)+'/Alltext.txt', 'r')
    f = f.read()
    f = c.clean(f)
    line = ""
    k = []
    for val in f:
        #val.replace('*','')
        line += val
    text = line.split()
    for n in range(1,11):
        j=[]
        #k=[]
        trigrams = ngrams(text, n)
        for grams in trigrams:
            j.append(grams)
        fdist = FreqDist(c.append_elements(j))
        fdist = fdist.most_common(10)
        for q in j:
            del q
        for g in fdist:
            k.append(g[0])
    print k
    file111 = open('222/'+str(w)+'/'+str(w)+'_Grams.txt','w')
    file111.write(str(k))
    file111.close()
#=============================================
#=============================================
print 'khan'
for z in Tags:
    newpath1 = '2/'+str(z)
    if not os.path.exists(newpath1):
        os.makedirs(newpath1)
    for d in Tag_filter(z):
        print str(d)
        src1 = '2/'+str(d)
        dst1 = '2/'+str(z)+'/'
        print dst1
        try:copy(src1, dst1)#print prevname
        except:pass
for z in Tags:
    os.system("cd /Users/jansherkhan/Desktop/Fold2/2/"+str(z)+"/;ls *.txt > list.txt")
#    for d in Tag_filter(z):
    list = open('2/'+str(z)+'/list.txt', 'r')
    list = list.read()
    list = list.split()
    for x in list:
        file = open('2/'+str(z)+'/'+str(x), 'r')
        file = file.read()
        file = c.clean(file)
        line1 = ""
        k1 = []
        for val1 in file:
            #val.replace('*','')
            line1 += val1
        text1 = line1.split()
        length = len(text1)
        for number1 in range(1,11):
            j1=[]
            #k=[]
            trigrams1 = ngrams(text1, number1)
            for grams1 in trigrams1:
                j1.append(grams1)
            fdist1 = FreqDist(c.append_elements(j1))
            fdist1 = fdist1.most_common(10)
            for t in j1:
                del t
            for h in fdist1:
                k1.append(h[0])
        print k1
        for a in Tags:
            comp = open('222/'+str(a)+'/'+str(a)+'_Grams.txt', 'r')
            comp = comp.read()
            number = 0
            common = []
            for phrase in k1:
                if phrase in comp:
                    common.append(phrase)
                    number += 1

            print (x+','+z+','+'compared-with= percent'+','+str(number) +','+'GroundTag'+','+a)
            d = x+','+z+','+'compared-with= percent'+','+str(number) +','+'GroundTag'+','+a
            print d
            
            with open('datatest333.csv','a') as scorefile:#======== CSV writer
                scorefilewriter = csv.writer(scorefile)
                scorefilewriter.writerow([x,z,'compared-with= percent',number,a,length])
                scorefile.close()


#        file1 = open('1/'+str(z)+'/'+str(d)+'_Grams.txt','w')
#        file1.write(str(k1))
#        file1.close()



#    number = 0
#    common = []
#    for phrase in k1:
#        if phrase in k:
#            common.append(phrase)
#            number += 1
#    print (d+','+w+','+'compared-with= percent'+','+str(number) +','+'GroundTag'+','+a)
#    d = w+','+i+','+'compared-with= percent'+','+str(number) +','+'GroundTag'+','+a
#    print d
#            
#    with open('datatesting.csv','a') as scorefile:#======== CSV writer
#        scorefilewriter = csv.writer(scorefile)
#        scorefilewriter.writerow([w,i,'compared-with= percent',number,a])
#        scorefile.close()


