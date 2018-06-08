from music21 import *
from random import randint
import json
import os

arquivos = []

coreCorpus = corpus.corpora.CoreCorpus()


for p in coreCorpus.getPaths():
	if "xml" in os.path.basename(str(p)):
		arquivos.append(os.path.basename(str(p)))

listanotas = []
listanotasP = []
listafim = []
listoitava = [0,7]
for file in arquivos:
	b = corpus.parse(file)
	d = b.parts[0]
	for item in d.recurse():
	    if ('notehead' in dir(item)) and ('name' in dir(item)):
	        listanotas.append(item.name)


for index in range(len(listanotas)-1):
	if listanotas[index+1][0] == "C":
		if listanotas[index][0] == "C":
			indexoitava = randint(0,1)
			listanotasP.append(listoitava[indexoitava])
		elif listanotas[index][0] == "B":
			listanotasP.append(1)
		elif listanotas[index][0] == "A":
			listanotasP.append(2)
		elif listanotas[index][0] == "G":
			listanotasP.append(3)
		elif listanotas[index][0] == "F":
			listanotasP.append(4)
		elif listanotas[index][0] == "E":
			listanotasP.append(5)
		elif listanotas[index][0] == "D":
			listanotasP.append(6)
	if listanotas[index+1][0] == "D":
		if listanotas[index][0] == "D":
			indexoitava = randint(0,1)
			listanotasP.append(listoitava[indexoitava])
		elif listanotas[index][0] == "C":
			listanotasP.append(1)
		elif listanotas[index][0] == "B":
			listanotasP.append(2)
		elif listanotas[index][0] == "A":
			listanotasP.append(3)
		elif listanotas[index][0] == "G":
			listanotasP.append(4)
		elif listanotas[index][0] == "F":
			listanotasP.append(5)
		elif listanotas[index][0] == "E":
			listanotasP.append(6)
	if listanotas[index+1][0] == "E":
		if listanotas[index][0] == "E":
			indexoitava = randint(0,1)			
			listanotasP.append(listoitava[indexoitava])
		elif listanotas[index][0] == "D":
			listanotasP.append(1)
		elif listanotas[index][0] == "C":
			listanotasP.append(2)
		elif listanotas[index][0] == "B":
			listanotasP.append(3)
		elif listanotas[index][0] == "A":
			listanotasP.append(4)
		elif listanotas[index][0] == "G":
			listanotasP.append(5)
		elif listanotas[index][0] == "F":
			listanotasP.append(6)
	if listanotas[index+1][0] == "F":
		if listanotas[index][0] == "F":
			indexoitava = randint(0,1)			
			listanotasP.append(listoitava[indexoitava])
		elif listanotas[index][0] == "E":
			listanotasP.append(1)
		elif listanotas[index][0] == "D":
			listanotasP.append(2)
		elif listanotas[index][0] == "C":
			listanotasP.append(3)
		elif listanotas[index][0] == "B":
			listanotasP.append(4)
		elif listanotas[index][0] == "A":
			listanotasP.append(5)
		elif listanotas[index][0] == "G":
			listanotasP.append(6)
	if listanotas[index+1][0] == "G":
		if listanotas[index][0] == "G":
			indexoitava = randint(0,1)			
			listanotasP.append(listoitava[indexoitava])
		elif listanotas[index][0] == "F":
			listanotasP.append(1)
		elif listanotas[index][0] == "E":
			listanotasP.append(2)
		elif listanotas[index][0] == "D":
			listanotasP.append(3)
		elif listanotas[index][0] == "C":
			listanotasP.append(4)
		elif listanotas[index][0] == "B":
			listanotasP.append(5)
		elif listanotas[index][0] == "A":
			listanotasP.append(6)
	if listanotas[index+1][0] == "A":
		if listanotas[index][0] == "A":
			indexoitava = randint(0,1)			
			listanotasP.append(listoitava[indexoitava])
		elif listanotas[index][0] == "B":
			listanotasP.append(1)
		elif listanotas[index][0] == "C":
			listanotasP.append(2)
		elif listanotas[index][0] == "D":
			listanotasP.append(3)
		elif listanotas[index][0] == "E":
			listanotasP.append(4)
		elif listanotas[index][0] == "F":
			listanotasP.append(5)
		elif listanotas[index][0] == "G":
			listanotasP.append(6)
	if listanotas[index+1][0] == "B":
		if listanotas[index][0] == "B":
			indexoitava = randint(0,1)			
			listanotasP.append(listoitava[indexoitava])
		elif listanotas[index][0] == "A":
			listanotasP.append(1)
		elif listanotas[index][0] == "G":
			listanotasP.append(2)
		elif listanotas[index][0] == "F":
			listanotasP.append(3)
		elif listanotas[index][0] == "E":
			listanotasP.append(4)
		elif listanotas[index][0] == "D":
			listanotasP.append(5)
		elif listanotas[index][0] == "C":
			listanotasP.append(6)
			
zero = listanotasP.count(0)
um = listanotasP.count(1)
dois = listanotasP.count(2)
tres = listanotasP.count(3)
quatro = listanotasP.count(4)
cinco = listanotasP.count(5)
seis = listanotasP.count(6)
sete = listanotasP.count(7)

zeroP = int(zero/len(listanotasP)*1000)
umP = int(um/len(listanotasP)*1000)
doisP = int(dois/len(listanotasP)*1000)
tresP = int(tres/len(listanotasP)*1000)
quatroP = int(quatro/len(listanotasP)*1000)
cincoP = int(cinco/len(listanotasP)*1000)
seisP = int(seis/len(listanotasP)*1000)
seteP = int(sete/len(listanotasP)*1000)

for i in range(zeroP):
	listafim.append(0)
for i in range(umP):
	listafim.append(1)
for i in range(doisP):
	listafim.append(2)
for i in range(tresP):
	listafim.append(3)
for i in range(quatroP):
	listafim.append(4)
for i in range(cincoP):
	listafim.append(5)
for i in range(seisP):
	listafim.append(6)
for i in range(seteP):
	listafim.append(7)


dados = {"notas" : listafim}
print(len(dados["notas"]))
with open('dadosprob.json', 'w') as fp:
    json.dump(dados, fp)