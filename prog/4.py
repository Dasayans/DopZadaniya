import os
os.system('cls')
import pandas as pd
import re
with open("4t.txt",'r+') as file:
    st=list(file)[:57]
df = pd.read_csv("4t.txt", sep="\t",skiprows=57,header=None)
adr=df[7].tolist()
for a in range(len(adr)):
    s=[re.split(r'\d{1,10}',adr[a]),re.findall(r'\d{1,10}',adr[a])]
    if len(s[1])==3:
        adr[a]='DB'+str(int(s[1][1])*2+(1 if int(s[1][0])>8 else 0))+s[0][2]+s[1][2]+'.'+str(int(s[1][0])%8)
    else:
        adr[a] = s[0][0]+s[1][0]+s[0][1][:2]+'B'+s[0][1][2]+str(int(s[1][1])*2)
df[7]=pd.Series(adr)
with open("4tn.txt",'w+') as file:
    file.writelines(st)
df.to_csv('4tn.txt',sep="\t",header=None,mode='a')