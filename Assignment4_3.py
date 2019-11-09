import functools as f
import NumberOperation_Module as NOM
def ForFilter(n):
    return (n>=70 and n<=90);

def ForMap(n):
    return n+10;

def ForReduce(n,m):
    return n*m;

def main():
    # arr=NOM.AcceptList()
    #or use below list
    arr=[4,34,36,76,68,24,89,23,86,90,45,70]

    filteredlist=list(filter(ForFilter,arr));

    modifiedlist=list(map(ForMap,filteredlist));

    res=f.reduce(ForReduce,modifiedlist)

    print("Result is=",res)


if __name__=='__main__':
    main();
