CC= g++
CFLAGS= -Wall -g
CPPTARGET= createData

PY= python3
PYTARGET= plot

all: dataGen plotData

dataGen: $(CPPTARGET).cpp
	$(CC) $(CFLAGS) -o $(CPPTARGET) $(CPPTARGET).cpp
	chmod +x $(CPPTARGET)
	./$(CPPTARGET)
	@echo ------------------------------------------------
	@echo [ Data Generation Successful Plotting Graph... ]
	@echo ------------------------------------------------

plotData: $(PYTARGET).py
	$(PY) $(PYTARGET).py

clean:
	rm -rf $(CPPTARGET) data.txt
