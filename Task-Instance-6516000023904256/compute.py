import numpy as np, numba
from datetime import datetime as dt
from matplotlib import pyplot as plt

# @numba.jit -- Uncomment to boost Iterative solution's speed
def genMatrix(n):
	a=[]; b=[]
	for i in range(n):
		t1=[]; t2=[]
		for j in range(n):
			t1.append(np.random.randint(0,500))
			t2.append(np.random.randint(0,500))
		a.append(t1); b.append(t2)
	return a,b

# @numba.jit -- Uncomment to boost Iterative solution's speed
def multiplyMatrix(a,b,n,result):
	for i in range(n):
		for j in range(n):
			for k in range(n):
				result[i][j] += a[i][k] * b[k][j]
	return result

def plotGraph(itr1,nmpy1,itr2,nmpy2):
	plt.title("Matrix-Multiplication (All Versions Comparison)",color='red')
	plt.plot(itr1[0],itr1[1],label="Iterative")
	plt.plot(nmpy1[0],nmpy1[1],label="Numpy")
	plt.plot(itr2[0],itr2[1],label="Iterative+JIT")
	plt.plot(nmpy2[0],nmpy2[1],label="Numpy+JIT(Code)")
	plt.xlabel('Input Size of (NxN) Matrices',color='blue')
	plt.ylabel('Time Taken (in seconds)',color='blue')
	plt.legend()
	plt.show()
	
def main():
	run=[10,50,100,150,200,250,300,350,400,450,500]

	# This is the data computed for Iterative version and Numpy version
	itr1=[run, [0.000774, 0.184463, 1.290416, 4.415173, 11.824319, 22.024403, 36.79975, 63.423021, 88.217722, 131.088186, 223.86272]]
	nmpy1=[run, [0.000118, 0.001342, 0.051214, 0.016997, 0.046807, 0.086633, 0.182305, 0.298953, 0.464965, 0.628617, 3.059303]]
	#plotGraph(itr1,nmpy1)
	
	# This is the data computed for the Improved Iterative version using Numba.JIT and Numpy version
	itr2=[run, [4.431335, 0.097624, 0.889914, 3.253325, 8.225882, 16.589311, 28.113434, 47.214586, 66.141524, 86.484509, 118.903617]]
	nmpy2=[run, [0.000162, 0.000959, 0.006077, 0.01615, 0.065154, 0.105772,0.199723, 0.322044, 0.360032, 0.536672, 0.610496]]
	#plotGraph(itr2,nmpy2)
	
	# A graph plot to show differences between all versions:-
	plotGraph(itr1,nmpy1,itr2,nmpy2)
	"""
	for N in run:
		# Generate Input Matrices
		A,B = genMatrix(N)
		
		# Iterative-Matrix-Multiplication
		res = [[0 for i in range(N)] for j in range(N)]
		TIME=dt.now()
		res = multiplyMatrix(A,B,N,res)
		tme = str(dt.now()-TIME)
		itr1[1].append(sum(x*float(t) for x,t in zip([3600,60,1],tme.split(":"))))
		
		# Matrix-Multiplication using Numpy
		TIME=dt.now()
		res = np.dot(A,B)
		nmpy1[1].append(sum(x*float(t) for x,t in zip([3600,60,1],str(dt.now()-TIME).split(":"))))
		
		# Printing Details
		print("Iterative: %d => %s		|		Numpy: %d => %s\n"%(N,tme,N,str(dt.now()-TIME)))
	"""
	
if __name__ == "__main__":
	main()
