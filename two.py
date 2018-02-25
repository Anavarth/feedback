class feedback():
    import csv
    file = None
    read = None
    tstr = None
    sstr = None
    qstr = None
    tab = []
    wt = []
    def readfile(self):
        import csv
        self.file = open('Samp.csv', "r")
        self.read = csv.reader(self.file)
        self.qstr = ["Effective lecturer","Clear Presentations","stimulated student interest","Effectively used time","Available and Helpful","Grading was prompt","Teaching","Clearing doubts","Interaction","Communication"]
        self.sstr = ["Sub 1","Sub 2","Sub 3","Sub 4","Sub 5","Sub 6","Sub 7","Sub 8"]
        self.tstr = ["T1","T2","T3","T4","T5","T6","T7","T8"]
    def create_table(self,a):
        self.file.seek(0)
        self.wt = a
        if len(self.wt)!=10:
            self.wt = [4,4,4,4,3.6,3.6,3,3,3,3]
        self.tab.append(self.qstr)
        for ii in range(8):
            k = q1 = q2 = q3 = q4 = q5 = q6 = q7 = q8 = q9 = q10 = 0
            for row in self.read:
                if k != 0:
                    if k%2 == 0:
                        q1=q1+int(row[16+ii*10])/self.wt[0]
                        q2=q2+int(row[17+ii*10])/self.wt[1]
                        q3=q3+int(row[18+ii*10])/self.wt[2]
                        q4=q4+int(row[19+ii*10])/self.wt[3]
                        q5=q5+int(row[20+ii*10])/self.wt[4]
                        q6=q6+int(row[21+ii*10])/self.wt[5]
                        q7=q7+int(row[22+ii*10])/self.wt[6]
                        q8=q8+int(row[23+ii*10])/self.wt[7]
                        q9=q9+int(row[24+ii*10])/self.wt[8]
                        q10=q10+int(row[25+ii*10])/self.wt[9]
                k = k + 1
            self.file.seek(0)
            self.tab.append([q1,q2,q3,q4,q5,q6,q7,q8,q9,q10])
        self.tab[0].append("Rank")
        for i in range(1,len(self.tab)):
            self.tab[i].append(sum(self.tab[i])/10)
    def display_table(self):
        from beautifultable import BeautifulTable
        table = BeautifulTable()
        table.column_headers = ["Question","1","2","3","4","5","6","7","8","9","10","Rank"]
        for j in range(1,len(self.tab)):
            self.tab[j].insert(0,self.sstr[j-1]+" "+self.tstr[j-1])
            table.append_row(self.tab[j])
            self.tab[j].pop(0)
        print("\n\n\n\n")
        print(table)
        print("\nWhere Questions and Weightages are ")
        for i in range(10):
            print(i+1,". ",self.qstr[i]," - ",self.wt[i])
    def correlation(self,q1):
        import numpy
        c=numpy.corrcoef([self.tab[1][10],self.tab[2][10],self.tab[3][10],self.tab[4][10],self.tab[5][10],self.tab[6][10],self.tab[7][10],self.tab[8][10]],[self.tab[1][q1-1],self.tab[2][q1-1],self.tab[3][q1-1],self.tab[4][q1-1],self.tab[5][q1-1],self.tab[6][q1-1],self.tab[7][q1-1],self.tab[8][q1-1]])
        return round(c[1][0],4)
    def interpret(self,a):
        c = []
        h = []
        for i in range(len(a)):
            c.append(self.correlation(a[i]))
            print("\n\n",self.qstr[a[i]-1]," has the correlation to the rank is ",c[i])
            h.append(self.hypo([self.tab[1][10],self.tab[2][10],self.tab[3][10],self.tab[4][10],self.tab[5][10],self.tab[6][10],self.tab[7][10],self.tab[8][10]],[self.tab[1][a[i]-1],self.tab[2][a[i]-1],self.tab[3][a[i]-1],self.tab[4][a[i]-1],self.tab[5][a[i]-1],self.tab[6][a[i]-1],self.tab[7][a[i]-1],self.tab[8][a[i]-1]],c[i]))
            if ((float(h[i])>= -1.96) and (float(h[i])<=1.96)):
                print(" The null hypothesis is accepted")
                print(" Therefore the test statistic value(pearson correlation coefficient)is significant at 0.05 level")
            else:
                print(" Reject the null hypothesis")
                print(" Therefore the test statistic value(pearson correlation coefficient)is not significant at 0.05 level")
        print("\n\n",self.qstr[a[c.index(max(c))]-1]," correlates more among the given questions...")
    def mult(self,list1,list2):
        ab = []
        for i in range(0, len(list1)):
            ab.append(list1[i]*list2[i])
        return ab
    def estimate_coef(self,x,y):
            n = len(y)
            a = self.mult(x,y)
            b = self.mult(x,x)
            c = self.mult(y,y)
            num = n*(sum(a))-(sum(x)*sum(y))
            den = n*sum(b)-(sum(x)*sum(x))
            if den == 0:
                return 0
            else:
                b=num/den
                a=(sum(y)-b*sum(x))/n
                return (a,b)
    def hypo(self,x,y,r):
        n=len(x)
        if pow((1-(r*r)),0.5)==0:
            return 0
        h = r*(pow((n-2),0.5)) / pow((1-(r*r)),0.5)
        return h
    def graph(self,a):
        import matplotlib.pyplot as plt;
        plt.rcdefaults()
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        plt.bar([1,2,3,4,5,6,7,8],[self.tab[1][a],self.tab[2][a],self.tab[3][a],self.tab[4][a],self.tab[5][a],self.tab[6][a],self.tab[7][a],self.tab[8][a]])
        plt.xlabel("Teacher")
        plt.ylabel("Aggregrate")
        plt.title(self.qstr[a])
        plt.show()
    def scatter_plot(self,a,b):
        import matplotlib.pyplot as plt;
        plt.rcdefaults()
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        x = []
        y = []
        for i in range(1,20):
                x.append(i)
                y.append(a+i*b)
        plt.scatter(x,y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Regression")
        plt.show()
    def report(self,a):
        n = int(input("\n\nEnter a Minimum Aggregate : "))
        for i in range(len(a)):
            cc = []
            c = 0
            print("\nThe Teacher ",self.tstr[a[i]-1]," should improve in ")
            for ii in range(10):
                if self.tab[a[i]][ii] <= n:
                    print(self.qstr[ii])
                    c = 1
            if c == 0:
                print("Nothing to Show!!!")
    def menu(self):
        n = 0
        self.readfile()
        self.create_table([1,2])
        print("\n\n\n\t\tSTUDENT FEEDBACK ANALYSIS\nMENU:")
        while n != 5:
            n = int(input("\n1.Table\n2.Correlation, Hypothesis & Graph\n3.Regression\n4.Report\n5.Exit\nEnter your choice...  "))
            if n == 1:
                n1 = 0
                while n1 != 3:
                    n1 = int(input("\n\n\n1.View\n2.Give weightage\n3.return\nEnter your choice..."))
                    if n1 == 1:
                        self.display_table()
                        input("\n\nPress Enter....")
                    elif n1 == 2:
                        a = []
                        for i in range(10):
                            a.append(int(input("Enter weightage for "+self.qstr[i]+" :  ")))
                        self.tab=[]
                        self.qstr.pop()
                        self.create_table(a)
                        self.display_table()
                        input("\n\nPress Enter....")
                    elif n1 == 3:
                        break
                    else:
                        input("\n\nEnter a valid Choice\n\nPress Enter....")
            elif n == 2:
                print("\n\n\n\nQuestions:")
                for i in range(10):
                    print(i+1,"."+self.qstr[i])
                print("\n\nEnter the Number(s)...")
                a = [int(x) for x in input().split()]
                self.interpret(a)
                for i in range(len(a)):
                    self.graph(a[i]-1)
                input("\n\nPress Enter....")
            elif n == 3:
                print("\n\n\n\nQuestions:")
                for i in range(10):
                    print(i+1,"."+self.qstr[i])
                iv = int(input("\n\nEnter Independant Question"))
                print("\nEnter the Dependant Question(s)...")
                a = [int(x) for x in input().split()]
                ra = []
                rb = []
                for i in range(len(a)):
                    (aa,b)=self.estimate_coef([self.tab[1][iv-1],self.tab[2][iv-1],self.tab[3][iv-1],self.tab[4][iv-1],self.tab[5][iv-1],self.tab[6][iv-1],self.tab[7][iv-1],self.tab[8][iv-1]],[self.tab[1][a[i]-1],self.tab[2][a[i]-1],self.tab[3][a[i]-1],self.tab[4][a[i]-1],self.tab[5][a[i]-1],self.tab[6][a[i]-1],self.tab[7][a[i]-1],self.tab[8][a[i]-1]])
                    print("\nThe dependency of ",self.qstr[a[i]-1]," towards ",self.qstr[iv-1]," is :  ",round(aa,4))
                    self.scatter_plot(aa,b)
                    ra.append(aa)
                    rb.append(b)
                print(ra.index(max(ra)))
                print("\n\n",self.qstr[a[ra.index(max(ra))]-1]," depends more on ",self.qstr[iv-1]," among the selection")
                input("\n\nPress Enter....")
            elif n == 4:
                print("\n\n\n\nTeachers:")
                for i in range(len(self.tstr)):
                    print(i+1,"."+self.tstr[i])
                print("\n\nEnter the Number(s)...")
                a = [int(x) for x in input().split()]
                self.report(a)
            elif n == 5:
               exit()
            else:
                input("\n\nEnter a valid Choice\n\nPress Enter....")
X=feedback()
X.menu()
