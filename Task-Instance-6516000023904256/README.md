# Time Bound Computation
It is a research based task performed by UTx10101 to complete a GCI-2019 task published by Fedora: [Here](https://codein.withgoogle.com/dashboard/task-instances/6516000023904256/)
## Task Theme:-
To bring out performance difference between normal python code and numpy functions.
## Reference-Code:-
There's only one single file `compute.py` which contains all the code used to compute data and plot charts shown below.
## Dependencies:
1. `datetime` - Module to compute time elapsed
2. `matplotlib` - Module to plot charts
3. `numpy` - Module to get faster functions
4. `numba` - Module to improve normal python code's speed by enabling JIT
## Results of Research:
1. As my laptop was too slow to compute the time taken for functions to run I have used `Repl.it` to run the script online and generate the data to plot which is as shown below:-
### Iterative-vs-Numpy
![Iterative-vs-Numpy](https://github.com/UTx10101/UTx10101-GCI-2019-Fedora/blob/master/Task-Instance-6516000023904256/Images/Iterative-vs-Numpy.png)
### Iterative+Numba-vs-Numpy
![Iterative+Numba-vs-Numpy](https://github.com/UTx10101/UTx10101-GCI-2019-Fedora/blob/master/Task-Instance-6516000023904256/Images/Iterative+Numba-vs-Numpy.png)
2. Following Time V/S Input Graphs were observed:-
### Time-vs-Input-Graph-1
![Time-vs-Input-Graph-1](https://github.com/UTx10101/UTx10101-GCI-2019-Fedora/blob/master/Task-Instance-6516000023904256/Images/Time-vs-Input-Graph-1.png)
### Time-vs-Input-Graph-2
![Time-vs-Input-Graph-2](https://github.com/UTx10101/UTx10101-GCI-2019-Fedora/blob/master/Task-Instance-6516000023904256/Images/Time-vs-Input-Graph-2.png)
3. This is the final result observed when above two graphs were plotted together:-
### Final-Comparison
![Final-Comparison](https://github.com/UTx10101/UTx10101-GCI-2019-Fedora/blob/master/Task-Instance-6516000023904256/Images/Final-Comparison.png)
## Clearly Numpy outperforms the other alternatives - But Why ?
The very first reason could be its written mostly in `C` language which provides higher speeds at low level code and instructions.<br>
The second reason is Numpy `Operations` take advantage of parallelism due to which is can operate on `Multiple Data` within a single `Operation`.<br>
The third reason is the `Data Structures` it provides i.e. Numpy `Arrays` which are densely packed with arrays of `homogeneous` numerical data types. 

### By:- UTx10101
