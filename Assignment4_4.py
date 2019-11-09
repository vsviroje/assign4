import functools as f
import NumberOperation_Module as NOM
def ForFilter(n):
    return (n%2==0);

def ForMap(n):
    return n*n;

def ForReduce(n,m):
    return n+m;

def main():
    # arr=NOM.AcceptList()
    #or use below list
    arr=[5,2,3,4,3,4,1,2,8,10]

    filteredlist=list(filter(ForFilter,arr));

    modifiedlist=list(map(ForMap,filteredlist));

    res=f.reduce(ForReduce,modifiedlist)

    print("Result is=",res)


if __name__=='__main__':
    main();
