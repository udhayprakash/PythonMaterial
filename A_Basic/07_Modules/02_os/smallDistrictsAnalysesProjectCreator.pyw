import os

ProjectName = 'smallDistrictsAnalysesProject'
if not os.path.dirname(ProjectName):
    os.mkdir(ProjectName)
os.chdir(ProjectName)

for i in range(1,11):
    os.mkdir('district'+str(i))
    
locationPath = os.getcwd()

for dp, d, f in os.walk('.'):
	for i in d:
		for num in range(1,11):
			with open(locationPath + os.path.sep + str(i) + os.path.sep +'opinion'+'-'+str(i)+'-'+ 'name'+'-'+str(num)+'.txt', 'wb') as t:
				t.write('This is opinion file of district: %s , Name: %s'%(i, num))
				t.close()