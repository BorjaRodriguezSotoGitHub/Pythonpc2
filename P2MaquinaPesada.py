import sys
import os

os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')


os.system('pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt')

os.environ['GROUP_NAME'] = 'Grupo 35'
titlename = os.environ['GROUP_NAME']
print(titlename)




os.system('cp practica_creativa2/bookinfo/src/productpage/templates/productpage.html practica_creativa2/bookinfo/src/productpage/templates/productpage2.html')

fin = open('practica_creativa2/bookinfo/src/productpage/templates/productpage.html', 'r') # in file 

fout = open('practica_creativa2/bookinfo/src/productpage/templates/productpage2.html', 'w') # out file 
        
for line in fin:
	if '{% block title %}Simple Bookstore App{% endblock %}' in line : 
		fout.write('{% block title %}'+str(titlename)+'{% endblock %}')   

	else: 
		fout.write(line) 

fin.close() 
fout.close()


os.system('rm practica_creativa2/bookinfo/src/productpage/templates/productpage.html')
os.system('cp practica_creativa2/bookinfo/src/productpage/templates/productpage2.html practica_creativa2/bookinfo/src/productpage/templates/productpage.html')
os.system('rm practica_creativa2/bookinfo/src/productpage/templates/productpage2.html')

os.system('python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080')
