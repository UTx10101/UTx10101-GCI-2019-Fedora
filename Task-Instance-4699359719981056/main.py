from imports import tools as T

def main():
    T.printBanner()
    T.getInput()
    res=T.validateInput()
    if(res==False):
        print("\n{:30s}{}\n{:30s}|{} |\n{:30s}{}\n".format("","#"*30,""," Time Table is Not Possible","","#"*30))
        exit(1)
    arr = T.setUpMatrix()
    T.processTimeTable(arr)

if __name__ == "__main__":
    main()
