def checkgrade(g):
	grade=["O","A+","A","B+","B"]
	pts=["5","4","3","2","1","0"]
	for i in range(4):
		if g is grade[i]:
			return pts[i]
	return pts[i+1]
def checkgpa(pp):
	p=float(pp)
	gpa=[9,8,7,6]
	pts=[5,4,3,2,1,0]
	for i in range(4):
		if p>=gpa[i]:
			return pts[i]
	return pts[5]
def checkstr1(s):
	str1=["Poor","Satisfactory","Fair","Excellent","Very good"]
	pts=[1,2,3,4,5]
	for i in range(4):
		if len(s) is len(str1[i]):
			return pts[i]
def checkstr2(s):
	str2=["Strongly disagree","disagree","Neutral","agree","Strongly agree"]
	pts=[1,2,3,4,5]
	if len(s) is 14:
		return 5
	for i in range(4):
		if len(s) is len(str2[i]):
			return pts[i]
import csv
file1  = open('Course Evaluation.csv',"r")
read = csv.reader(file1)
file2  = open('Samp.csv',"w")
writer=csv.writer(file2)
nrl=[]
l=0
for row in read :
	if l is not 0:
		nr=[row[0],row[1],checkgrade(row[2]),checkgrade(row[3]),checkgrade(row[4]),checkgrade(row[5]),checkgrade(row[6]),checkgrade(row[7]),checkgrade(row[8]),checkgrade(row[9]),checkgpa(row[10]),checkstr1(row[11]),checkstr1(row[12]),checkstr1(row[13]),checkstr1(row[14]),checkstr1(row[15]),checkstr2(row[16]),checkstr2(row[17]),checkstr2(row[18]),checkstr2(row[19]),checkstr2(row[20]),checkstr2(row[21]),checkstr1(row[22]),checkstr1(row[23]),checkstr1(row[24]),checkstr1(row[25]),checkstr2(row[26]),checkstr2(row[27]),checkstr2(row[28]),checkstr2(row[29]),checkstr2(row[30]),checkstr2(row[31]),checkstr1(row[32]),checkstr1(row[33]),checkstr1(row[34]),checkstr1(row[35]),checkstr2(row[36]),checkstr2(row[37]),checkstr2(row[38]),checkstr2(row[39]),checkstr2(row[40]),checkstr2(row[41]),checkstr1(row[42]),checkstr1(row[43]),checkstr1(row[44]),checkstr1(row[45]),checkstr2(row[46]),checkstr2(row[47]),checkstr2(row[48]),checkstr2(row[49]),checkstr2(row[50]),checkstr2(row[51]),checkstr1(row[52]),checkstr1(row[53]),checkstr1(row[54]),checkstr1(row[55]),checkstr2(row[56]),checkstr2(row[57]),checkstr2(row[58]),checkstr2(row[59]),checkstr2(row[60]),checkstr2(row[61]),checkstr1(row[62]),checkstr1(row[63]),checkstr1(row[64]),checkstr1(row[65]),checkstr2(row[66]),checkstr2(row[67]),checkstr2(row[68]),checkstr2(row[69]),checkstr2(row[70]),checkstr2(row[71]),checkstr1(row[72]),checkstr1(row[73]),checkstr1(row[74]),checkstr1(row[75]),checkstr2(row[76]),checkstr2(row[77]),checkstr2(row[78]),checkstr2(row[79]),checkstr2(row[80]),checkstr2(row[81]),checkstr1(row[82]),checkstr1(row[83]),checkstr1(row[84]),checkstr1(row[85]),checkstr2(row[86]),checkstr2(row[87]),checkstr2(row[88]),checkstr2(row[89]),checkstr2(row[90]),checkstr2(row[91]),checkstr1(row[92]),checkstr1(row[93]),checkstr1(row[94]),checkstr1(row[95]),checkstr2(row[96]),checkstr2(row[97]),checkstr2(row[98]),checkstr2(row[99]),row[100],row[101]]
		nrl.append(nr)
		print(nr)
	else:
		nrl.append(row)
	l=l+1
writer.writerows(nrl)
