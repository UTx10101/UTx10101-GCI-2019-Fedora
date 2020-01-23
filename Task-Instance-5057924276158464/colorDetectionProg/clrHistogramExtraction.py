import os, cv2, numpy as np

def clrHistogramOfImage(img):
	channels = cv2.split(img)
	colors = ('b', 'g', 'r')
	features = []
	feature_data = ""
	ctr = 0
	for (channel, color) in zip(channels, colors):
		ctr += 1
		histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
		features.extend(histogram)
		
		prev = None
		l = []
		ii=0
		while(ii<50):
			if(prev!=None):
				elem = np.argmax(histogram)
				if(abs(prev-elem)>=2):
					l.append(elem)
					prev=elem; histogram[elem] = [-200]
					ii+=1
				else:
					histogram[elem] = [-200]
			else:
				l.append(np.argmax(histogram))
				prev=l[-1]; histogram[l[-1]] = [-200]
				ii+=1

		if(ctr==1):
			blue = l
		elif(ctr==2):
			green = l
		elif(ctr==3):
			red = l
			for i in range(50):
				feature_data += "{},{},{}\n".format(red[i],green[i],blue[i])
			feature_data = feature_data.strip()
	
	with open("colorDetectionProg/img_clr_data.csv", 'w') as F:
		F.write(feature_data)

def clrHistogramForTrainingImage(img):
	dataSRC = img.split("/")[-2]
	image = cv2.imread(img)

	channels = cv2.split(image)
	colors = ('b', 'g', 'r')
	features = []
	feature_data = ''
	ctr = 0
	for (channel, color) in zip(channels, colors):
		ctr += 1
		histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
		features.extend(histogram)

		elem = np.argmax(histogram)
		
		if(ctr==1):
			blue = elem
		elif(ctr==2):
			green = elem
		elif(ctr==3):
			red = elem
			feature_data = "{},{},{},{}\n".format(red,green,blue,dataSRC)

	with open("colorDetectionProg/training_clr_data.csv", 'a') as F:
		F.write(feature_data)


def Training():
	path=os.getcwd()+"/trainingSet"
	for root,_,files in os.walk(path):
		for f in files:
			clrHistogramForTrainingImage(root+"/"+f)
