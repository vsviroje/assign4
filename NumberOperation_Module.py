import math;

def AcceptList():
    no = int(input("Enter number of element"));
    arr = list();

    for i in range(0, no, 1):
        n = int(input());
        arr.append(n);
    return arr;


#################################
def ChkPrime(n):
    if n>0 and n<4:
        res=True
    elif n==4:
        res=False
    else:
        c=math.ceil((n/2)+1);
        i=0
        for i in range(2,c,1):
            if n%i==0:
                break;
        if(i==(c-1)):
            res=True;
        else:
            res=False;
    return res;


