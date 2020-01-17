import eel, random as rdm

eel.init('GUI')

quests={
	1: [[{"Q": "Value of: 1 + 1", "S": 5, "CA": "2", "OPT": ["10","2","11","None of These"], "T": 10},
		{"Q": "Value of: 10 × 5 + 20 ÷ 10 - 20 × 2", "S": 5, "CA": "3", "OPT": ["10","16","12","18"], "T": 15},
		{"Q": "Value of: [(4 ÷ 2)20 ÷ 10 + 2]", "S": 5, "CA": "4", "OPT": ["10","8","4","6"], "T": 15}],3],
	2: [[{"Q": "Add: (1/2)+(2/4)", "S": 5, "CA": "1", "OPT": ["1","2","4","None of These"], "T": 10},
		{"Q": "Subtract: (2/3) from (5/4)", "S": 5, "CA": "3", "OPT": ["0","(1/4)","(7/12)","None of These"], "T": 10}],2],
	3: [[{"Q": "Solve for x: x + 4 = 2", "S": 10, "CA": "4", "OPT": ["0","2","4","None of These"], "T": 10},
		{"Q": "Solve for k: 5k + 10 = 5", "S": 10, "CA": "1", "OPT": ["-1","0","-5","(1/5)"], "T": 15}],2],
	4: [[{"Q": "Solve for α: (α/2) + (2α/4) = 1", "S": 10, "CA": "3", "OPT": ["2","0","1","None of These"], "T": 15},
		{"Q": "What percentage of 20 is (2/5) ?", "S": 10, "CA": "4", "OPT": ["1%","5%","20%","None of These"], "T": 20}],2],
	5: [[{"Q": "Solve for (x,y): Given x + 2y = 4 and 2y - x = 4", "S": 15, "CA": "1", "OPT": ["(0,2)","(2,0)","(4,4)","None of These"], "T": 20},
		{"Q": "Solve for x: (x+1/x-1) = 5", "S": 15, "CA": "2", "OPT": ["1.0","(3/2)","2.5","Cannot be determined"], "T": 20}],2],
	6: [[{"Q": "Find value of: (x^3) + 8(y^3) + 27(z^3) if x + 2y + 3z = 0", "S": 20, "CA": "4", "OPT": ["xyz","x+y+z","(x^2)y(z^2)","18xyz"], "T": 20},
		{"Q": "Find: (x^8)+[1/(x^8)] when (x^2) - [1/(x^2)] = 0", "S": 10, "CA": "2", "OPT": ["4","2","0","10"], "T": 20}],2],
	7: [[{"Q": "Find no. of solutions of: (x^2) + (y^2) = 25 and (x^4) + (y^4) = 625", "S": 30, "CA": "4", "OPT": ["Only One","Only Two","Real Solutions","Complex Solutions"], "T": 60},
		{"Q": "Find range of expression: (y^2) = 4(x^2) + 6x + 1", "S": 30, "CA": "3", "OPT": ["y ∈ (-1,1)U(2,∞)","y ∈ (-∞,0]","y ∈ [0,∞)","None of These"], "T": 60}],2],
	8: [[{"Q": "Find value of: ∑ (1/i)di where i goes from 1 to e", "S": 40, "CA": "1", "OPT": ["1","0","-1","None of These"], "T": 30},
		{"Q": "Find solution to DE: (y^2) = [(d^2)y/dx]", "S": 40, "CA": "4", "OPT": ["ln x + C","ln xy + C","arctan(x+(y^2))","None of These"], "T": 60}],2],
	9: [[{"Q": "Let f(x) be a quintic polynomial such that f(1)=1, f(2)=1, f(3)=2 f(4)=3, f(5)=5, f(6)=8  Find f(7) ?", "S": 50, "CA": "1", "OPT": ["8","12","13","None of These"], "T": 120},
		{"Q": "If the region in the first quadrant bounded by the curve y=(e^x) and x=1 is rotated about the x-axis, what is the volume of the resulting solid ?", "S": 50, "CA": "3", "OPT": ["[(e^3)-1 / 3]","[1-(e^2) / 2]","[(e^2)-1 / 2]","None of These"], "T": 90}],2],
	10: [[{"Q": "A line y=mx+1 intersects the circle (x-3)^2 + (y+2)^2 = 25 at the points P and Q. If the midpoint of the line segment PQ has x-coordinate -(3/5), then correct option is ?", "S": 50, "CA": "2", "OPT": ["6 ≤ m < 8","2 ≤ m < 4","4 ≤ m < 6","-3 ≤ m < -1"], "T": 60},
		{"Q": "The polynomial f(z)=a(z^2018)+b(z^2017)+c(z^2016) has real coefficients not exceeding 2019 and f([1+(3i^{1/2}) / 2]=2015+2019(3i^{1/2}). Find the remainder when f(1) is divided by 1000.", "S": 50, "CA": "2", "OPT": ["47","53","42","None of These"], "T": 600}],2]
}

nmA=""; nmB=""
sA=0; sB=0;
scenes=["home","rules","arena","results","surprise"]
currActive=0
##    lvl,currQ,nQ,acs,cA,wA,cB,wB
stats=[1,None,0,0,0,0,0,0,0]

@eel.expose
def setupScenes():
	eel.show_hide_elems(scenes[1:],0)
	eel.show_hide_elems(scenes[:1],1)
	global currActive,nmA,nmB,sA,sB,stats
	nmA=""; nmB=""; sA=0; sB=0; currActive=0
	stats=[1,None,0,0,0,0,0,0,0]

@eel.expose
def updateGameReady(data,ID):
	global nmA, nmB
	As="&nbsp;SCORE: "+str(sA); Bs="&nbsp;SCORE: "+str(sB)
	data=data.strip()
	if(data=="" or "\n" in data):
		return -1
	else:
		if(ID=="nameA"):
			nmA=data
			eel.lock_unlock_elems([ID,"sub"+ID[-1]],1)
			if(nmB!=""):
				prevnext(1)
				eel.lock_unlock_elems(["nameA","subA","nameB","subB"],0)
				eel.setVal("A_name","&nbsp;TEAM: "+nmA,0)
				eel.setVal("B_name","&nbsp;TEAM: "+nmB,0)
				eel.setVal("A_score",As,0)
				eel.setVal("B_score",Bs,0)
		else:
			nmB=data
			eel.lock_unlock_elems([ID,"sub"+ID[-1]],1)
			if(nmA!=""):
				prevnext(1)
				eel.lock_unlock_elems(["nameA","subA","nameB","subB"],0)
				eel.setVal("A_name","&nbsp;TEAM: "+nmA,0)
				eel.setVal("B_name","&nbsp;TEAM: "+nmB,0)
				eel.setVal("A_score",As,0)
				eel.setVal("B_score",Bs,0)
		return 1

@eel.expose
def prevnext(flg):
	global currActive,nmA,nmB,sA,sB,stats
	if(flg==-1):
		if(currActive!=0):
			eel.show_hide_elems([scenes[currActive]],0)
			eel.show_hide_elems([scenes[currActive-[1,3][currActive==3]]],1)
			currActive-=[1,3][currActive==3]
			if(currActive==0):
				nmA=""; nmB=""; sA=0; sB=0
				stats=[1,None,0,0,0,0,0,0,0]
			if(currActive==2):
				putQuest()
	else:
		if(currActive==4):
			exit(1)
		eel.show_hide_elems([scenes[currActive]],0)
		eel.show_hide_elems([scenes[currActive+1]],1)
		currActive+=1
		if(currActive==0):
			nmA=""; nmB=""; sA=0; sB=0
			stats=[1,None,0,0,0,0,0,0,0]
		if(currActive==2):
				putQuest()

@eel.expose
def genResult(who=None):
	prevnext(1)
	global currActive,nmA,nmB,sA,sB,stats
	As="SCORE: "+str(sA); Bs="SCORE: "+str(sB)
	quitBy=[[nmA,nmB][who==2],None][who==None]
	if(quitBy==nmA):
		eel.setVal('winName',nmB,2)
		eel.setVal('winScore',Bs,2)
		out="<table align='center' style='min-width: 90vw; font-family: \"Kalam\", sans-serif; color: white; font-size: 25px'><tr><td style='min-width: 30vw;'>Total Questions: {}</td><td style='min-width: 30vw;'>Correct Answers: {}</td><td style='min-width: 30vw;'>Wrong Answers: {}</td></tr><tr><td style='min-width: 30vw;'>Skipped: {}</td><td style='min-width: 30vw;'></td><td style='min-width: 30vw;'>WonBy: {}</td></tr></table>".format(stats[8],stats[6],stats[7],stats[8]-stats[6]-stats[7],nmA+" Lost Hope")
		eel.setVal('stats',out,0)
	elif(quitBy==nmB):
		eel.setVal('winName',nmA,2)
		eel.setVal('winScore',As,2)
		out="<table align='center' style='min-width: 90vw; font-family: \"Kalam\", sans-serif; color: white; font-size: 25px'><tr><td style='min-width: 30vw;'>Total Questions: {}</td><td style='min-width: 30vw;'>Correct Answers: {}</td><td style='min-width: 30vw;'>Wrong Answers: {}</td></tr><tr><td style='min-width: 30vw;'>Skipped: {}</td><td style='min-width: 30vw;'></td><td style='min-width: 30vw;'>WonBy: {}</td></tr></table>".format(stats[8],stats[4],stats[5],stats[8]-stats[4]-stats[5],nmB+" Lost Hope")
		eel.setVal('stats',out,0)
	else:
		if(sA==sB):
			eel.setVal('winName',"both",2)
			eel.setVal('winScore',"It's a TIE",2)
			out="<table align='center' style='min-width: 90vw; font-family: \"Kalam\", sans-serif; color: white; font-size: 25px'><tr><td style='min-width: 30vw;'>Total Questions: {}</td><td style='min-width: 30vw;'>Max Correct: {}</td><td style='min-width: 30vw;'>Max Wrong: {}</td></tr><tr><td style='min-width: 30vw;'>Max Skipped: {}</td><td style='min-width: 30vw;'></td><td style='min-width: 30vw;'></td></tr></table>".format(stats[8],max(stats[4],stats[6]),max(stats[5],stats[7]),stats[8]-min(stats[4]+stats[5],stats[6]+stats[7]))
			eel.setVal('stats',out,0)
		else:
			win=[nmA,nmB][sB>sA]; winS=[As,Bs][sB>sA]
			eel.setVal('winName',win,2)
			eel.setVal('winScore',winS,2)
			out="<table align='center' style='min-width: 90vw; font-family: \"Kalam\", sans-serif; color: white; font-size: 25px'><tr><td style='min-width: 30vw;'>Total Questions: {}</td><td style='min-width: 30vw;'>Correct Answers: {}</td><td style='min-width: 30vw;'>Wrong Answers: {}</td></tr><tr><td style='min-width: 30vw;'>Skipped: {}</td><td style='min-width: 30vw;'></td><td style='min-width: 30vw;'>WonBy: {}</td></tr></table>".format(stats[8],stats[[4,6][sB>sA]],stats[[5,7][sB>sA]],stats[8]-stats[[4,6][sB>sA]]-stats[[5,7][sB>sA]],str(abs(sA-sB))+" Points")
			eel.setVal('stats',out,0)

@eel.expose
def putQuest():
	global stats
	if(stats[2]!=0 and stats[3]>=stats[2]/quests[stats[0]][1]):
		if(stats[0]==10):
			genResult()
			return
		stats[0]+=1; stats[1]=None; stats[2]=stats[3]=0
	stats[1]=rdm.randrange(0,quests[stats[0]][1])
	for i in range(1,5):
		AID="ansA"+str(i); BID="ansB"+str(i)
		eel.setVal(AID,quests[stats[0]][0][stats[1]]['OPT'][i-1],1)
		eel.setVal(BID,quests[stats[0]][0][stats[1]]['OPT'][i-1],1)
	LvL="Level - {}<br>({} Points)".format(stats[0],quests[stats[0]][0][stats[1]]['S'])
	eel.setVal('LVL',LvL,0)
	eel.setVal('ques',quests[stats[0]][0][stats[1]]['Q'],0)
	eel.initTimer('timer',quests[stats[0]][0][stats[1]]['T'])

@eel.expose
def validate(ans):
	global stats,sA,sB
	if(ans!=None):
		if(ans[1]==quests[stats[0]][0][stats[1]]['CA']):
			if(ans[0]=="A"):
				stats[4]+=1
				sA+=quests[stats[0]][0][stats[1]]['S']
			else:
				stats[6]+=1
				sB+=quests[stats[0]][0][stats[1]]['S']
			stats[3]+=1
		else:
			if(ans[0]=="A"):
				stats[5]+=1
				sA-=10
			else:
				stats[7]+=1
				sB-=10
	stats[2]+=1
	stats[8]+=1
	As="&nbsp;SCORE: "+str(sA); Bs="&nbsp;SCORE: "+str(sB)
	eel.setVal("A_score",As,0)
	eel.setVal("B_score",Bs,0)
	putQuest()

eel.start('index.html')#,mode="chrome-app",host="localhost",port=2120,cmdline_args=["--start-fullscreen", "--browser-startup-dialog"]) ## Uncomment this to run it in your chromium browser.
