a=[int(x) for x in input().split()]
print(a)
import csv
file  = open('Samp.csv', "r")
read = csv.reader(file)
rank = []
st3 = []
eft = []
tab = []
tab.append(["Effective lecturer","Clear Presentations","stimulated student interest","Effectively used time","Available and Helpful","Grading was prompt","Teaching","Clearing doubts","Interaction","Communication"])
for ii in range(8):
        k = q1 = q2 = q3 = q4 = q5 = q6 = q7 = q8 = q9 = q10 = 0
        for row in read:
                if k != 0:
                        if k%2==0:
                                q1=q1+int(row[16+ii*10])
                                q2=q2+int(row[17+ii*10])
                                q3=q3+int(row[18+ii*10])
                                q4=q4+int(row[19+ii*10])
                                q5=q5+int(row[20+ii*10])
                                q6=q6+int(row[21+ii*10])
                                q7=q7+int(row[22+ii*10])
                                q8=q8+int(row[23+ii*10])
                                q9=q9+int(row[24+ii*10])
                                q10=q10+int(row[25+ii*10])
                k = k + 1
        file.seek(0)
        tab.append([q1,q2,q3,q4,q5,q6,q7,q8,q9,q10])
for ii in range(7):
	rnk = l = s3 = gp = 0
	for row in read:
		if l != 0:
			if l%2==0:
				rk=(int(row[2+ii])*(int(row[16+ii*10])*.6+int(row[17+ii*10])*.6+int(row[18+ii*10])*.2+int(row[19+ii*10])*.2+int(row[20+ii*10])*.2+int(row[21+ii*10])*.2+int(row[22+ii*10])*.6+int(row[23+ii*10])*.6+int(row[24+ii*10])*.4+int(row[25+ii*10])*.4))
				rnk=rnk+rk
				s3=s3+int(row[18+ii*10])
				gp=gp+float(row[16+ii*10])
		l = l + 1
	file.seek(0)
	rank.append(rnk/72)
	st3.append(tab[3][ii])
	eft.append(gp)
print("The aggregative marks based on the students gpa and student's opinion about teachers are...")
for k in range(len(rank)):
        print("Teacher ",k+1," :  ",rank[k])
input()
from beautifultable import BeautifulTable
table = BeautifulTable()
tab[0].insert(0,"Teacher")
table.column_headers = tab[0]
for j in range(1,len(tab)):
        tab[j].insert(0,j)
        table.append_row(tab[j])
        tab[j].pop(0)
tab[0].pop(0)
print("\n\n\n\n",table)
input()
def pearsonr(x,y):
	n = len(x)
	sum_x = float(sum(x))
	sum_y = float(sum(y))
	sum_x_sq = sum(map(lambda x: pow(x, 2), x))
	sum_y_sq = sum(map(lambda x: pow(x, 2), y))
	psum =sum(map(lambda x, y: x * y, x, y))
	num = (n*psum) - (sum_x * sum_y)
	den = pow(((n*sum_x_sq) - pow(sum_x, 2)) * ((n*sum_y_sq) - pow(sum_y, 2)), 0.5)
	if den == 0:
		return 0
	else:
		return num/den
def interpret(c):
        if c<0:
                print("There exists a strong negative association between them")
        elif c>0:
                 print("There exists a strong positive association between them")
        else:
                print("There exists a no association between them")

def mult(list1,list2):
	ab = []
	for i in range(0, len(list1)):
		ab.append(list1[i]*list2[i])
	return ab
def estimate_coef(x, y):
	n = len(x)
	a=mult(x,y)
	b=mult(x,x)
	c=mult(y,y)
	num = n*(sum(a))-(sum(x)*sum(y))
	den = n*sum(b)-(sum(x)*sum(x))
	if den == 0:
		return 0
	else:
		b=num/den
		a=(sum(y)-b*sum(x))/n
		return (a,b)
sb2=[]
sb8=[]
for ii in range(10):
	s2=0
	s8=0
	l=0
	file.seek(0)
	for row in read:
		if l != 0:
			if l%2==0:
				s2=s2+int(row[16+ii])
				s8=s8+int(row[88+ii])
		l=l+1
	sb2.append(s2)
	sb8.append(s8)
def hypo(x,y,r):
    n=len(x)
    tnum=pow(r*(n-2),0.5)
    tden=pow((1-(r*r)),0.5)
    #tden=round(tden,2)
    t=tnum/tden
    return t
def datgra(sb2,ra2,rb2):
        x=[]
        y=[]
        for i in range(1,20):
                x.append(i)
                y.append(ra2+i*rb2)
        return (x,y)
import matplotlib.pyplot as plt;
plt.rcdefaults()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
n=0
c=np.corrcoef(rank,st3)
print(c[1][0])
while n!=3:
        n=int(input("\n\n\n\n1.Default\n2.Dynamic\n3.Exit\nEnter your choice...  "))
        if n==1:
                c2=pearsonr(rank,st3)
                c2=round(c2, 4)
                c3=pearsonr(rank,eft)
                c3=round(c3,4)
                print("\n\n\n\nThe correlation coefficient for finding the realtion between instructor's rank and student who stimulates interest is:",c2)
                interpret(c2)
                print("The correlation coefficient for finding the relation between instructor's rank and the instructor who effectively demonstrates lectures:",c3)
                interpret(c3)
                if c3>c2:
                        print("Hence the instructor who effectively demonstrartes lectures are ranked better than instructor who stimulates student interest")
                else:
                        print("Hence the instructor who stimulates student interest are ranked better than instructor who effectively demonstrartes lectures")
                input()
                (ra2,rb2)=estimate_coef(sb2,sb8)
                ra2=round(ra2,4)
                rb2=round(rb2,4)
                print("\n\n\n\nThe regression coefficient is:",ra2)
                print("The intercept is:",rb2)
                print("Hence the equation is:y=",ra2,"+",rb2,"x")
                input()
                h=hypo(rank,st3,c2)
                h=h*h
                h=round(abs(h)**0.5,4)
                p=0.05
                los=1.96
                print("\n\n\n\n")
                if ((float(h)>= -los) and (float(h)<=los)):
                        print("The null hypothesis is accepted")
                        print("Therefore the test statistic value(pearson correlation coefficient)is significant at 0.05 level")
                else:
                        print("Reject the null hypothesis")
                        print("Therefore the test statistic value(pearson correlation coefficient)is not significant at 0.05 level")
                print("The hypothesis test statistic value:",h)
                input()
                [x,y]=datgra(sb2,ra2,rb2)
                plt.scatter(x,y)
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title("Regression")
                plt.show()
                plt.bar([1,2,3,4,5,6,7],rank)
                plt.xlabel('Teacher')
                plt.ylabel('Rank')
                plt.title("Ranks")
                plt.show()
        elif n==2:
                a=int(input("\n\n\n\nEnter Ques no "))
                b=int(input("Enter Ques no "))
                c1=round(pearsonr(rank,tab[a][1:8]),4)
                c2=round(pearsonr(rank,tab[b][1:8]),4)
                print("\n\n\n\nThe correlation coefficient for finding the realtion between instructor's rank and student who stimulates interest is:",c1)
                interpret(c1)
                print("The correlation coefficient for finding the relation between instructor's rank and the instructor who effectively demonstrates lectures:",c2)
                interpret(c2)
                if c2>c1:
                        print("Hence the instructor who ",tab[0][a-1]," are ranked better than instructor who ",tab[0][b-1])
                else:
                        print("Hence the instructor who ",tab[0][b-1]," are ranked better than instructor who ",tab[0][a-1])
                input()
                bg=0
                while bg!=3:
                        bg=int(input("\n\n\n\nDoes the graph should be based on \n1.Teacher\n2.Question\n3.Return\nEnter your choice..."))
                        if bg==1:
                                bk=int(input("Enter Teacher no "))
                                plt.bar([1,2,3,4,5,6,7,8,9,10],tab[bk])
                                plt.xlabel("Question")
                                plt.ylabel("Aggregrate")
                                plt.title("Teacher "+str(bk))
                                plt.show()
                        elif bg==2:
                                bk=int(input("Enter Question no "))
                                plt.bar([1,2,3,4,5,6,7,8],[tab[1][bk],tab[2][bk],tab[3][bk],tab[4][bk],tab[5][bk],tab[6][bk],tab[7][bk],tab[8][bk]])
                                plt.xlabel("Teacher")
                                plt.ylabel("Aggregrate")
                                plt.title("Question "+str(bk))
                                plt.show()
                        elif bg==3:
                                break
                        else:
                                print("\n\n\n\nEnter a Valid choice")
                                input()
        elif n==3:
                exit()
        else:
                print("\n\n\n\nEnter a Valid choice")
                input()
