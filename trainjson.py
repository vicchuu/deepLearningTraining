import json

from pybot import tokenise,stem , bagofwords

import numpy as np
#import nltk.w
from pybot import *

with open("intent.json", 'r') as f:
    intent=json.load(f)


tags=[]
patterns=[]
allwords=[]
xy=[]

for content in intent["intents"]:
    tag=content["tag"]
    tags.append(tag)
    for pattern in content["patterns"]:
        pat= tokenise(pattern)
        allwords.extend(pat)
        xy.append((pattern,tag))

print(len(allwords),allwords)
"""Remove puncuation"""
puncuations=[",",".","?","!","@","&","*","(",")"]
allwords=[stem(w) for w in allwords if w not in puncuations ]
allwords=sorted(set(allwords))
tags=sorted(set(tags))
print(len(allwords), allwords)

xtrain=[]
ytrain=[]

for (pattern ,tag) in xy:

    bag=bagofwords(pattern,allwords)
    xtrain.append(bag)
    label=tags.index(tag)
    ytrain.append(label)

xtrain= np.array(xtrain)
ytrain=np.array(ytrain)



 