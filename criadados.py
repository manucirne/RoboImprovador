from music21 import *
from random import randint
import json
import os
              
arquivos = []
#arquivosabc = []
              
coreCorpus = corpus.corpora.CoreCorpus()
              
              
for p in coreCorpus.getPaths():
	if "xml" in os.path.basename(str(p)):
		arquivos.append(os.path.basename(str(p)))
# for p in coreCorpus.getPaths():
# 	if "abc" in os.path.basename(str(p)):
# 		arquivosabc.append(os.path.basename(str(p)))
              
listanotas = []
listanotasP = []
listazero = []
listaum = []
listadois = []
listatres = []
listaquatro = []
listacinco = []
listaseis = []
listasete = []
              
listoitava = [0,7]
for file in arquivos:
	b = corpus.parse(file)
	d = b.parts[0]
	for item in d.recurse():
	    if ('notehead' in dir(item)) and ('name' in dir(item)):
	        listanotas.append(item.name)
# for file in arquivosabc:
# 	b = corpus.parse(file)
# 	#d = b.parts[0]
# 	for item in b.recurse():
# 	    if ('notehead' in dir(item)) and ('name' in dir(item)):
# 	        listanotas.append(item.name)
              
              
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
	listazero.append(0)
for i in range(umP):
	listazero.append(1)
for i in range(doisP):
	listazero.append(2)              
for i in range(tresP):
	listazero.append(3)
for i in range(quatroP):
	listazero.append(4)
for i in range(cincoP):
	listazero.append(5)
for i in range(seisP):
	listazero.append(6)
for i in range(seteP):
	listazero.append(7)

for i in range(zeroP):
	listaum.append(1)
for i in range(umP):
	listaum.append(2)
for i in range(doisP):
	listaum.append(3)
for i in range(tresP):
	listaum.append(4)
for i in range(quatroP):
	listaum.append(5)
for i in range(cincoP):
	listaum.append(6)
for i in range(seisP):
	listaum.append(7)
for i in range(seteP):
	listaum.append(0)

for i in range(zeroP):
	listadois.append(2)
for i in range(umP):
	listadois.append(3)
for i in range(doisP):
	listadois.append(4)
for i in range(tresP):
	listadois.append(5)
for i in range(quatroP):
	listadois.append(6)
for i in range(cincoP):
	listadois.append(7)
for i in range(seisP):
	listadois.append(0)              
for i in range(seteP):
	listadois.append(1)
              
for i in range(zeroP):
	listatres.append(3)
for i in range(umP):
	listatres.append(4)
for i in range(doisP):
	listatres.append(5)
for i in range(tresP):
	listatres.append(6)
for i in range(quatroP):
	listatres.append(7)
for i in range(cincoP):
	listatres.append(0)
for i in range(seisP):
	listatres.append(1)
for i in range(seteP):
	listatres.append(2)

for i in range(zeroP):
	listaquatro.append(4)
for i in range(umP):
	listaquatro.append(5)
for i in range(doisP):
	listaquatro.append(6)
for i in range(tresP):
	listaquatro.append(7)
for i in range(quatroP):
	listaquatro.append(0)
for i in range(cincoP):
	listaquatro.append(1)
for i in range(seisP):
	listaquatro.append(2)
for i in range(seteP):
	listaquatro.append(3)              
              
for i in range(zeroP):
	listacinco.append(5)
for i in range(umP):
	listacinco.append(6)
for i in range(doisP):
	listacinco.append(7)
for i in range(tresP):
	listacinco.append(0)
for i in range(quatroP):
	listacinco.append(1)
for i in range(cincoP):
	listacinco.append(2)
for i in range(seisP):
	listacinco.append(3)
for i in range(seteP):
	listacinco.append(4)

for i in range(zeroP):
	listaseis.append(6)
for i in range(umP):
	listaseis.append(7)
for i in range(doisP):
	listaseis.append(0)
for i in range(tresP):
	listaseis.append(1)
for i in range(quatroP):
	listaseis.append(2)
for i in range(cincoP):
	listaseis.append(3)
for i in range(seisP):
	listaseis.append(4)
for i in range(seteP):
	listaseis.append(5)
              
for i in range(zeroP):
	listasete.append(7)
for i in range(umP):
	listasete.append(0)
for i in range(doisP):
	listasete.append(1)
for i in range(tresP):
	listasete.append(2)
for i in range(quatroP):
	listasete.append(3)
for i in range(cincoP):
	listasete.append(4)
for i in range(seisP):
	listasete.append(5)
for i in range(seteP):
	listasete.append(6)
              
              
dados = {"zero" : listazero, "um": listaum, "dois": listadois, "tres": listatres, "quatro": listaquatro, "cinco": listacinco, "seis": listaseis, "sete": listasete}
with open('dadosprob.json', 'w') as fp:
    json.dump(dados, fp)
