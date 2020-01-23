import cv2, operator, csv

def loadData(fname,fname2,TFvector=[[],0],testFvector=[]):
	with open(fname) as csvF:
		lines = csv.reader(csvF)
		data = list(lines)
		for x in range(len(data)):
			for y in range(3):
				data[x][y] = float(data[x][y])
			TFvector[0].append(data[x])
			TFvector[1]+=1

	with open(fname2) as csvF:
		lines = csv.reader(csvF)
		data = list(lines)
		for x in range(len(data)):
			for y in range(3):
				data[x][y] = float(data[x][y])
			testFvector.append(data[x])

def EuclideanDist(a, b, l):
	dist = 0
	for x in range(l):
		dist += pow(a[x]-b[x],2)
	
	return pow(dist,0.5)
	
def NearestNeighbours(TFvector, testInstance, k):
	dists = []
	l = len(testInstance)
	for x in range(TFvector[1]):
		dist = EuclideanDist(testInstance, TFvector[0][x], l)
		dists.append((TFvector[0][x], dist))
	dists.sort(key=operator.itemgetter(1))
	neighbours = [[],0]
	for x in range(k):
		neighbours[0].append(dists[x][0])
		neighbours[1]+=1
	
	return neighbours

def responseOfNeighbours(neighbours):
	possible_neighbours = {}
	for x in range(neighbours[1]):
		res = neighbours[0][x][-1]
		try:
			possible_neighbours[res] += 1
		except:
			possible_neighbours[res] = 1
	votes = sorted(possible_neighbours.items(), key=operator.itemgetter(1), reverse=True)
	
	return [x[0] for x in votes]

def classifier(tData, testData):
	TFvector = [[],0]
	testFvector = []
	loadData(tData, testData, TFvector, testFvector)
	predictions = []
	k = 3  # K value of k nearest neighbor
	for x in range(TFvector[1]):
		neighbours = NearestNeighbours(TFvector, testFvector[x], k)
		res = responseOfNeighbours(neighbours)
		predictions += res

	return set(predictions)
