from matplotlib import pyplot as plt

x=["0-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80","81-90","91-100"]
y=[0,0,0,0,0,0,0,0,0,0]

with open("data.txt", 'r') as Data:
	for l in Data.readlines():
		l=l.split(' ')
		for num in l:
			for k in x:
				K=k.split("-")
				if(num!='' and int(num)>=int(K[0]) and int(num)<=int(K[1])):
					y[int(k[0])]+=1

plt.title("Random Number Range - Plot",color='red')
plt.bar(x,y,color='green')
plt.xlabel('(Range Of Numbers)',color='blue')
plt.ylabel('(No. Of Numbers)',color='blue')
plt.show()
