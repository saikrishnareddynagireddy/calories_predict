def varsamp(x):
    mean=sum(x)/len(x)
    num=sum([(i-mean)**2 for i in x])
    den=len(x)-1
    return num/den

def stdev(x):
    return (varsamp(x))**0.5

def gmean(x):
    m=1
    for i in x:
        m*=i
        n=len(x)
    return m**(1/n)

def hmean(x):
    n=len(x)
    d=sum([1/i for i in x])
    return n/d

def means(x):
    am=sum(x)/len(x)
    gm=gmean(x)
    hm=hmean(x)
    return (am,gm,hm)

def covar(x,y):
    mx=sum(x)/len(x)
    my=sum(y)/len(y)
    dx=[i-mx for i in x]
    dy=[i-my for i in y]
    d=sum([a*b for a,b in list(zip(x,y))])
    n=len(x)-1
    return d/n

def correlation(x,y):
    n=len(x)
    nl=(n *(sum([a*b for a,b in list(zip(x,y))])))
    nr=sum(x)*sum(y)
    dl=(n*sum([i**2 for i in x]))-sum(x)**2
    dr=(n*sum([i**2 for i in y]))-sum(y)**2
    num=nl-nr
    den=(dl*dr)**0.5
    return num/den
temp=[10,20,30,40]
cs=[45,98,135,170]
ss=[90,50,23,10]

mean_temp=means(temp)
print(mean_temp)

k=covar(temp,cs)
j=correlation(temp,cs)
print(k,'\n',j)

a=[10,20,30,40,50]
b=varsamp(a)
print(b)