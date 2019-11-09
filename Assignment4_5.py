import functools as f
import NumberOperation_Module as NOM

def ForMap(n):
    return n*2;

def ForReduce(n,m):
    if(n>m):
        return n
    else:
        return m

def main():
    #arr=NOM.AcceptList()
    #or use below list
    arr=[2,70,11,10,17,23,31,77]

    filteredlist=list(filter(NOM.ChkPrime,arr));

    modifiedlist=list(map(ForMap,filteredlist));

    res=f.reduce(ForReduce,modifiedlist)

    print("Result is=",res)


if __name__=='__main__':
    main();
