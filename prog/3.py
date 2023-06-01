import os
os.system('cls')
import re
from functools import reduce
def f(pr,el):
    rez=[]
    if pr[len(pr)-1][0]<el[0]:
        pr.append(el)
    return pr
with open('news.txt','r+') as file:
    news=[[int(re.split(r' ',a,1)[0]),re.split(r' ',a,1)[1]] for a in file]
    [print(a[1]) for a in reduce(f,news,[[0,'']])]