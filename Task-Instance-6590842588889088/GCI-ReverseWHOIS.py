import requests as rq
from bs4 import BeautifulSoup, SoupStrainer
from datetime import datetime as dt

def tablePrinter(table):
    maxlen_cols = [(max([len(str(row[i])) for row in table]) + 3) for i in range(len(table[0]))]
    row_format = "|".join(["{:>" + str(maxlen_col) + "}" for maxlen_col in maxlen_cols])
    r2=["---------------","---------------","---------------"]
    stp=0
    flg=0
    fname=str(input("\n	Enter the File Name to Save the Results <Type `)None(` to skip>: "))
    if(fname!=")None("):
        flg=1
        f=open(fname,"a+")
    print("\n")
    for row in table:
        if(stp==1):
            if(flg):
                f.write("%s\r\n" %(row_format.format(*r2)))
            print(row_format.format(*r2))
        if(flg):
            f.write("%s\r\n" %(row_format.format(*row)))
        print(row_format.format(*row))
        stp+=1
    if(flg):
        f.close()

def dispData(info):
    dataArr=[]
    for row in info.findAll('tr'):
        arr=[]
        for col in row.findAll('td'):
            arr.append(col.text.strip())
        dataArr.append(arr)
    tablePrinter(dataArr)

def lookup(text):
    t=dt.now()
    total=0
    URL = "https://viewdns.info/reversewhois/?q="+'+'.join(text.split(" "))
    r=rq.Session()
    res = r.get(url=URL, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'})
    if res.ok:
        httext = BeautifulSoup(res.content,'html5lib')
        httext = httext.find('font',attrs={'size':'2','face':'Courier'})
        infotable = httext.find('table', attrs={'border':'1'})
        for s in httext.stripped_strings:
            if(s.startswith("There are")):
                total=s.split()[2]
        print("\n	%s Results Found for `%s`" %(total,text))
        print("	Total Time Taken: ",dt.now()-t,'\n')
        if(total=='0'):
            exit(1)
        flg=0
        while(flg==0):
            choice=str(input("\n	Do you Want to Display the Results? (y/n): "))
            if(choice in ['y','Y']):
                if(int(total.replace(",",""))>500):
                   print("\n	*Note:- Only First 500 Results for `%s` will be displayed and/or saved" %(text))
                dispData(infotable)
                flg=1
            elif(choice in ['n','N']):
                print("\n")
                exit(1)
        print("\n")
        exit(1)

txt=str(input("\n	Enter Registrant Name or Email Address for Reverse WHOIS Lookup: "))
lookup(txt)
