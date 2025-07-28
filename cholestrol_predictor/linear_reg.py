import numpy as np
f=open("C:/python/cholesterol_data.csv")
h=f.readline()
lines=f.readlines()
age=[]
gender=[]
bmi=[]
smoking=[]
activity=[]
fatintake=[]
alcohol=[]
familyhistory=[]
diabetes=[]
cholestrol=[]


for line in lines:
    w=line.split(',')
    a=int(w[0])
    ge=int(w[1])
    bm=float(w[2])
    sm=int(w[3])
    ac=int(w[4])
    fa=float(w[5])
    al=float(w[6])
    fam=int(w[7])
    dia=float(w[8])
    chol=float(w[-1].strip())
    age.append(a)
    gender.append(ge)
    bmi.append(bm)
    smoking.append(sm)
    activity.append(ac)
    fatintake.append(fa)
    alcohol.append(al)
    familyhistory.append(fam)
    diabetes.append(dia)
    cholestrol.append(chol)

#print(cholestrol)
ones=np.ones(len(lines))
x=np.c_[ones,age,gender,bmi,smoking,activity,fatintake,alcohol,familyhistory,diabetes]
y=np.array(cholestrol).reshape(len(lines),1)


from numpy.linalg import inv
xt=x.transpose()
xtx=np.dot(xt,x)
xtxinv=inv(xtx)
xty=np.dot(xt,y)
print(xtxinv.shape," ",xty.shape,'\n',y)
beta=xtxinv.dot(xty)
b0=beta[0,0]
b1=beta[1,0]
b2=beta[2,0]
b3=beta[3,0]
b4=beta[4,0]
b5=beta[5,0]
b6=beta[6,0]
b7=beta[7,0]
b8=beta[8,0]
b9=beta[9,0]

#to check prediction accuracy
ycap=[]
for v in x:
    age=v[1]
    gender=v[2]
    bmi=v[3]
    smoking=v[4]
    activity=v[5]
    fatintake=v[6]
    alcohol=v[7]
    familyhistory=v[8]
    diabetes=v[9]
    pred=b0+(b1*age)+(b2*gender)+(b3*bmi)+(b4*smoking)+(b5*activity)+(b6*fatintake)+(b7*alcohol)+(b8*familyhistory)+(b9*diabetes)
    ycap.append(pred)

tests=np.c_[cholestrol,ycap]
pcnt=0
for v in tests:
    y=v[0]
    ycap=v[1]
    d=((y-ycap)*100)/y
    if d>=-10 and d<=10:
        pcnt+=1

n=len(tests)
acc=(pcnt*100)/n

#print(f"the accuracy of the model:{acc}")
from sklearn.metrics import accuracy_score
#print("accuracy:",accuracy_score(cholestrol, ycap))  #work for categorical data 




