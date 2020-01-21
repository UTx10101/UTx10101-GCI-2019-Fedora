import os
from flask import Flask, render_template, request, redirect

app=Flask(__name__)
app.config["UPLOAD_DIR"] = os.getcwd()+"/uploads/"

def Ok(F):
	if("." in F.filename and F.mimetype=="text/plain"):
		if(F.filename.split(".")[-1]=="txt"):
			return 1
	return 0

def genFname(fname):
	fname=fname.strip().replace("."," ").replace("_"," ").split()
	if(fname[-1]=="txt"):
		fname.pop()
	fname='_'.join(fname)+".txt"
	i=1
	while(os.path.exists(os.path.join(app.config['UPLOAD_DIR'], fname))):
		name, ext = os.path.splitext(fname)
		fname = "{}_{}{}".format(name, str(i), ext)
		i+=1
	return fname

@app.route("/view/<string:filename>", methods=['GET'])
def viewer(filename):
	with open(app.config["UPLOAD_DIR"]+filename, 'r+') as F:
		content=F.readlines()
	return render_template("helper.html", text=[content,2])

@app.route("/delete/<string:filename>")
def delete(filename):
	fpath = os.path.join(app.config['UPLOAD_DIR'], filename)
	if(os.path.exists(fpath)):
		try:
			os.remove(fpath)
			return render_template("helper.html", text=[filename,1])
		except:
			return render_template("helper.html", text=[filename,0])

@app.route("/upload", methods=["GET", "POST"])
def uploadFile():
	if(request.method=="POST"):
		if(request.files):
			f=request.files["txtfile"]
			if(Ok(f)):
				fname=request.form['fname']
				fname=genFname(f.filename) if fname=="" else genFname(fname)
				f.save(os.path.join(app.config["UPLOAD_DIR"], fname))
			return redirect(request.url)

	return render_template("upload.html")

@app.route("/")
def index():
	FiLeS=[[],0]
	for _,_,files in os.walk(app.config["UPLOAD_DIR"]):
		for f in files:
			FiLeS[0].append(f)
			FiLeS[1]+=1
	tDatas={}
	if(FiLeS[1]==0):
		tDatas['N/A']=["Upload","Some","Files","Please"]
	else:
		for i in range(FiLeS[1]):
			size=os.path.getsize(os.path.join(app.config['UPLOAD_DIR'], FiLeS[0][i]))
			view="/view/"+FiLeS[0][i]
			delete="/delete/"+FiLeS[0][i]
			tDatas[i+1]=[FiLeS[0][i],size,view,delete]
	return render_template("index.html", data=tDatas)

if __name__=="__main__":
	app.run()
