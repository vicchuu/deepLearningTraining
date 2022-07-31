# import nltk
# import numpy as np
# import torch
# import torch.nn as nn
# from itertools import groupby
# import ssl
#
# # try:
# #     _create_unverified_https_context = ssl._create_unverified_context
# # except AttributeError:
# #     pass
# # else:
# #     ssl._create_default_https_context = _create_unverified_https_context
# #
# # nltk.download()
# from nltk.stem.porter import PorterStemmer
#
# stemmer=PorterStemmer()
# def tokenise(sentence):
#     return nltk.word_tokenize(sentence)
#
# def stem(word):
#     return stemmer.stem(word.lower())
#
# def bagofwords(word,bagofwords):
#     bag=np.zeros(len(bagofwords),dtype=np.float32)
#     tokenizesentence=[stem(w) for w in word]
#
#     for word in  (tokenizesentence):
#         #print(word )
#         if word in bagofwords:
#             #print(word)
#             indx=bagofwords.index(word)
#             #print("index ",indx)
#             bag[indx]=1
#     return bag
# # pdf=[23,24,25,2,3]
# # lis1 =[5,4,3,4,2,1]  #list
# # lis2=(5,4,3,4,2,1)  #tuple
# # lis3={5,4,3,4,2,1}  # Set
# # lis4 = {9,8,7,6,5,4,3,2}
# #
# # lisy = lambda x : x<10
# #
# # for a in pdf:
# #     print(lisy(a))
# #
# # newin = groupby(lis3, key=lambda x: x < 3)
# #
# # for key,value  in newin:
# #     print(key,set(value))
# #
# # from functools import reduce
# # plm = [1,2,3,4,5]
# #
# # print(reduce(lambda x,y : x<4,plm))
# #
# #
# # class valuelow(Exception):
# #     def __init__(self,message,value):
# #         self.message=message
# #         self.value=value
# #
# # def raiseError(x):
# #     if x<10:
# #         raise valuelow("too low buddy ",x)
# #
# # try:
# #     raiseError(1)
# # except valuelow as e:
# #     print("looop" ,e.message, e.value)
# #
# #
# # try:
# #     a= 50
# #     b = a + 10.0
# # except TypeError as t:
# #     print(t)
# #
# # #rint(lis4.update(lis3))
# # print(lis2)
# # print(lis3)
# # print(lis4)
#
#
# # def traceCall(func):
# #
# #     def wrapper():
# #         print("inside")
# #         func()
# #         print("Outside")
# #     return wrapper
# # @traceCall
# # def printout( ):
# #     print("Vishnu")
# #
# # #obj = traceCall(printout("sweeet"),"swet")
# #
# # printout( )
#
#
#
# word=["this" , "is", "hero","me  "]
# bagOfWord=["my","name" ,"is","vishnu","do","you","know","me"]
# d=bagofwords(word,bagOfWord)
# print(d)
#
# avail = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#
# print(avail)