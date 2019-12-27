import random as rdm, sys
from imports import model

notes=["**Note:- 1. Number Of Teachers must be less than 10.",
                "2. For Subject enter only one of these (maths, physics, chemistry, biology, programming).",
                "3. For Amount of Periods per month enter a multiple of 4."]

def printBanner():
    banner=["   | Welcome To Timetable Generator by UTx10101 |","   ##############################################"]
    print("\n%s\n%s\n"%(banner[1],'\n'.join(banner)))
########
### Data-Input Vars
availableClasses=[[],0]
teachers=[[],0]
keyTeachers=[]
periods=[["P1","P2","P3","P4"],4]
wwds=[["Monday","Tuesday","Wednesday","Thursday","Friday"],5]
studs=[["Class-1","Class-2","Class-3","Class-4","Class-5","Class-6"],6]
sub_id=[{"maths":0,"physics":1,"chemistry":2,"biology":3,"programming":4},5]
keySubjects={ k: k[:2].capitalize() for k in sub_id[0].keys() }
subjects={
    "maths": { "periods":0, "teachers":[] },
    "physics": { "periods":0, "teachers":[] },
    "chemistry": { "periods":0, "teachers":[] },
    "biology": { "periods":0, "teachers":[] },
    "programming": { "periods":0, "teachers":[] }
}
########
### Input Tools
def getTeacherAndSub(x,det):
    trig=1 if len(det)==0 else 0
    X=input("Enter Teacher-"+str(x)+"\'s Details(NAME | SUBJECT | AMOUNTOFPERIODS): ") if trig else str(det.pop())
    X=X.split("|")
    name,sub=X[0].strip(),X[1].strip().lower()
    flg=[0,1][sub not in sub_id[0].keys()]
    while(flg):
        print("!! Invalid Subject in `{}` !!".format("".join(X)))
        sub=str(input("Enter a valid Subject(See Note): ")).strip().lower()
        flg=[0,1][sub not in sub_id[0].keys()]
    amt=int(X[2].strip())
    while(amt%4!=0):
        print("!! Invalid Amount of Periods per month in `{}` !!".format("".join(X)))
        amt=int(input("Enter amount of periods as per NOTE: ").strip())
    amt=amt//4
    model.Subject().addSubject(sub,sub_id,subjects,x,amt)
    teachers[0].append(model.Teacher(x,name,sub,amt))
    teachers[1]+=1
    return model.Class(name,sub,amt)

def getInput():
    print("\n%s\n"%('\n         '.join(notes)))
    while(True):
        fname=input("Enter Input FileName(With `.txt` extension) or 'M' to Enter Manually: ")
        if(fname!='M'):
            if(".txt" in fname):
                break
            else:
                print("!! Invalid Extension !!")
        else:
            print("!! Invalid Input !!")
    details=[]
    if(fname!='M'):
        with open(fname, 'r') as Data:
            for l in Data.readlines():
                l=l.strip()
                if(l!=''):
                    details.append(l)
    details.reverse()
    nuTeachers=int(input("Enter Number of Teachers: ")) if fname=="M" else int(details.pop())
    while(nuTeachers>10):
        print("!! {} Teachers Not Supported !!".format(nuTeachers))
        nuTeachers=int(input("Enter Number of Teachers(See Note): "))
        details=[]
    for i in range(1,nuTeachers+1):
        cLass=getTeacherAndSub(i,details)
        availableClasses[0].append(cLass)
        availableClasses[1]+=1

def validateInput():
    for sub,val in subjects.items():
        su=0
        if(len(val["teachers"])<=1):
            return False
        for t_ID in val["teachers"]:
            if(sub=="maths" or sub=="physics"):
                if(teachers[0][t_ID-1].periods%4!=0 or teachers[0][t_ID-1].periods>16):
                    return False
            teachers[0][t_ID-1].periods//=4
            su+=teachers[0][t_ID-1].periods
        if(su!=studs[1]):
            return False
    keyTeachers.append({ t.name: t.name[:4 if len(t.name)>4 else len(t.name)].capitalize() for t in teachers[0] })
    return True
########
### Timetable Tools
def findY(day,per):
    p=day*periods[1]
    for y in range(p,(day+1)*periods[1]):
        if(y%periods[1]==per):
            p=y
            break
    return p

def randomizedFiller(tMatrix,D,P,subj):
    d=D;p=P;ptr1=ptr2=0
    for t_ID in subjects[subj]["teachers"]:
        ptr2+=teachers[0][t_ID-1].periods
        while(ptr1<ptr2):
            tMatrix[findY(d,p)][ptr1]=keySubjects[subj]+" by "+keyTeachers[0][teachers[0][t_ID-1].name]
            p+=1;p%=periods[1]
            ptr1+=1

def setUpMatrix():
    w,h=studs[1], wwds[1]*periods[1]
    free=[]
    tableMatrix=[[free.append((y,x)) for x in range(w)] for y in range(h)]
    d=0
    while(d<((wwds[1]*periods[1])//sub_id[1])):
        p=ptr1=ptr2=0
        for t_ID in subjects["maths"]["teachers"]:
            ptr2+=teachers[0][t_ID-1].periods
            while(ptr1<ptr2):
                tableMatrix[findY(d,p)][ptr1]=keySubjects["maths"]+" by "+keyTeachers[0][teachers[0][t_ID-1].name]
                p+=1;p%=periods[1]
                ptr1+=1
        d+=1
    d=1
    while(d<((wwds[1]*periods[1])//sub_id[1])+1):
        p=1;ptr1=ptr2=0
        for t_ID in subjects["physics"]["teachers"]:
            ptr2+=teachers[0][t_ID-1].periods
            while(ptr1<ptr2):
                tableMatrix[findY(d,p)][ptr1]=keySubjects["physics"]+" by "+keyTeachers[0][teachers[0][t_ID-1].name]
                p+=1;p%=periods[1]
                ptr1+=1
        d+=1
    ##Generating Values for randomizedFiller():
    subjsPlaced={ key: 0 if key=="maths" or key=="physics" else ((wwds[1]*periods[1])//sub_id[1]) for key in sub_id[0].keys()}
    subjs=[x for x in sub_id[0].keys()];subjs.remove("maths");subjs.remove("physics")
    while(len(subjs)>0):
        subj=rdm.choice(subjs)
        choice_d=[x for x in range(wwds[1])]
        while(len(choice_d)>wwds[1]-((wwds[1]*periods[1])//sub_id[1])):
            d=rdm.choice(choice_d)
            p=None
            for i in range(0,periods[1]):
                if(tableMatrix[findY(d,i)][0]==None):
                    p=i
                    break
            if(p!=None):
                randomizedFiller(tableMatrix,d,p,subj)
                subjsPlaced[subj]-=1
            choice_d.remove(d)
        subjs.remove(subj)
        mx=max(subjsPlaced.values())
        if(mx!=0):
            for k in subjsPlaced.keys():
                if(subjsPlaced[k]==mx):
                    if(k not in subjs):
                        subjs.append(k)
    return tableMatrix

def saveToFile(tableMatrix):
    fname=input("\nEnter FileName to save in: ")
    print("\nExporting TimeTable to  `%s`..."%(fname))
    orig_out= sys.stdout
    with open(fname, 'w') as F:
        sys.stdout=F
        print("\n{:1s}{:15s}{}".format('',"**Legend => ","Subjects > | "+" | ".join([value+": "+key for key,value in keySubjects.items()])+" |"))
        print("{:16s}{}".format('',"Teachers > | "+" | ".join([value+": "+key for key,value in keyTeachers[0].items()])+" |"))
        print("\n{:1s}{}".format('',"#"*111))
        for i in range(studs[1]):
            if(i==0):
                print("| {:10s}|| {:6s} || {:12s}|".format("   Days","Period"," "+studs[0][i]),end=['','\n'][i+1==studs[1]])
            else:
                print("| {:12s}|".format("  "+studs[0][i]),end=['','\n'][i+1==studs[1]])
        dCtr=0
        for i in range(wwds[1]*periods[1]):
            if(i%periods[1]==0):
                print("{:1s}{}\n| {:9s} || {:6s} |".format('',"#"*111,'',periods[0][i%periods[1]]),end='')
            elif(i%periods[1]==1):
                print("| {:9s} || {:6s} |".format(wwds[0][dCtr],periods[0][i%periods[1]]),end='')
                dCtr+=1
            else:
                print("| {:9s} || {:6s} |".format('',periods[0][i%periods[1]]),end='')
            for j in range(studs[1]):
                print("| {:12s}|".format(str(tableMatrix[i][j])),end=['','\n'][j+1==studs[1]])
        print("{:1s}{}\n".format('',"#"*111))
        sys.stdout=orig_out
        F.close()
    print("Successfully Exported :-) Exiting...\n")
    exit(1)

def processTimeTable(tableMatrix):
    print("\n{:1s}{:15s}{}".format('',"**Legend => ","Subjects > | "+" | ".join([value+": "+key for key,value in keySubjects.items()])+" |"))
    print("{:16s}{}".format('',"Teachers > | "+" | ".join([value+": "+key for key,value in keyTeachers[0].items()])+" |"))
    print("\n{:1s}{}".format('',"#"*111))
    for i in range(studs[1]):
        if(i==0):
            print("| {:10s}|| {:6s} || {:12s}|".format("   Days","Period"," "+studs[0][i]),end=['','\n'][i+1==studs[1]])
        else:
            print("| {:12s}|".format("  "+studs[0][i]),end=['','\n'][i+1==studs[1]])
    dCtr=0
    for i in range(wwds[1]*periods[1]):
        if(i%periods[1]==0):
            print("{:1s}{}\n| {:9s} || {:6s} |".format('',"#"*111,'',periods[0][i%periods[1]]),end='')
        elif(i%periods[1]==1):
            print("| {:9s} || {:6s} |".format(wwds[0][dCtr],periods[0][i%periods[1]]),end='')
            dCtr+=1
        else:
            print("| {:9s} || {:6s} |".format('',periods[0][i%periods[1]]),end='')
        for j in range(studs[1]):
            print("| {:12s}|".format(str(tableMatrix[i][j])),end=['','\n'][j+1==studs[1]])
    print("{:1s}{}\n".format('',"#"*111))

    while(True):
        choice=input("\n\nWould you like to `Save This` one or `Generate New` with same input or `Exit` ? (Ss/Nn/Ee): ")
        if(choice in ["E","e"]):
            exit(1)
        elif(choice in ["S","s"]):
            saveToFile(tableMatrix)
        elif(choice in ["N","n"]):
            break
        else:
            print("!! Invalid Option !!")
    tMatrix=setUpMatrix()
    processTimeTable(tMatrix)
