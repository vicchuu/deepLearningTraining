#
#
# op = "dcsf3dfrsd3df432asdfcg423"
#
# digit=0
# maxDigit = 0
# num = dict()
# strElem =""
# newElem = ""
# for a in op:
#     if a.isdigit():
#         if maxDigit < (digit):
#             maxDigit = digit
#             newElem = strElem
#         if a in num:
#             num[a]+=1
#         else:
#             num[a]=1
#         strElem = ""
#         digit=0
#
#
#     else:
#         digit+=1
#         strElem+=a
#
# sorted(num.items(),key= lambda  x :x[1],reverse=True)
# print(list(num.keys())[0],"".join(sorted(newElem,reverse=False)))