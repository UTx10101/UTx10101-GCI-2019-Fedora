import cv2, os
from colorDetectionProg import clrHistogramExtraction, knnTrainer

print("\n{:8s}###########################################\n{:8s}||      Color Detector By UTx10101       ||\n{:8s}###########################################\n".format("","","",""))

opt = input("{:4s}Do you want to train the script first ? (Yy/Nn): ".format(""))
if(opt in ["Y","y"]):
	print("{:4s}Training started...".format(""))
	open("colorDetectionProg/training_clr_data.csv", 'w')
	clrHistogramExtraction.Training()
	print("{:4s}Training data has been updated...[:-)]".format(""))

img = input("{:4s}Enter Image Name or Path (if not in same directory as DetectorMain.py): ".format(""))
src_image=cv2.imread(img)
prediction = "Cannot Recognize"

tData = os.getcwd()+"/colorDetectionProg/training_clr_data.csv"

if(os.path.isfile(tData) and os.access(tData, os.R_OK)):
	print("{:4s}Training Data is ready...".format(""))
else:
	print("{:4s}Generating Training data...".format(""))
	open("colorDetectionProg/training_clr_data.csv", 'w')
	clrHistogramExtraction.Training()
	print("{:4s}Training data is ready...".format(""))

clrHistogramExtraction.clrHistogramOfImage(src_image)
prediction = ", ".join(knnTrainer.classifier(tData, os.getcwd()+"/colorDetectionProg/img_clr_data.csv"))

print('\n{:4s}Detected colors are: {}'.format("",prediction))
res = input("\n{:4s}Do you want to preview the image ? (Yy/Nn): ".format(""))

if(res in ["Y","y"]):
	print("\n{:8s}Press Any Key to Exit (Don't Close Image Window Directly)...".format(""))
	cv2.putText(src_image,'Prediction: ' + prediction,(15, 50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
	cv2.imshow(img, src_image)
	cv2.waitKey()
	cv2.destroyAllWindows()

print("\n{:4s}Thank You".format(""))
