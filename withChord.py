
from music21 import *
from random import randint
import json
from copy import deepcopy

#Pega o arquivo de dados (probabilidades)
arquivo = open("dadosprob.json", "r")
dados = arquivo.read()
dados = json.loads(dados)

#fornece informações para a música - acordes, tonalidade e fórmula de compasso
tom = "F#"
chords = ["C#","F#", "B", "C#", "C#", "F#", "B", "C#"]
Ctemp = 4
#definição de cada acorde da música para ser usado no arquivo midi
doS = chord.Chord(["C#3", "E#3", "G#3"])
faS = chord.Chord(["F#3", "A#3", "C#4"])
si = chord.Chord(["B2", "D#3", "F#3"])
si7 = chord.Chord(["B2", "D#3", "F#3", "D4"])
sib7 = chord.Chord(["B-2", "D3", "F3", "D-4"])
faSmenor = chord.Chord(["F#3", "A3", "C#4"])
reSm7 = chord.Chord(["D#3", "F#3", "A#3", "C#4"])
solS7 = chord.Chord(["G#3", "C3", "D#3", "F#3"])
#duração de cada acorde - um por compasso
d = duration.Duration()
d.quarterLength = 4
doS.duration = d
faS.duration = d
si.duration = d
si7.duration = d
sib7.duration = d
faSmenor.duration = d
reSm7.duration = d
solS7.duration = d

#stream que recebe todas a parts da música (melodia, acordes e batida inicial)
st = stream.Score()

#parte de batida inicial e sua configuração
p1 = stream.Part()
p1.id = "beat"
n = note.Note("F#6")
n.duration.quarterLength = 1.0
be = note.Unpitched()
be.storedInstrument = instrument.Marimba()
p1.repeatAppend(n, 4)
p1.makeMeasures(inPlace=True)
[n.beat for n in p1.flat.notes]

#pausa para colocar antes de iniciar a música, para que beat não invada o inicio oficial
rest = note.Rest()
rest.duration.quarterLength = 1.0
#Cria part de acordes e inicializa para que os beats não a invada
cifra = stream.Part()
cifra.id = "chords"
cifra.repeatAppend(rest, 4)
#Cria part de melodia - IMPROVISÇÃO! e inicializa como a part doa acordes
s = stream.Part()
s.id = 'melody'
s.repeatAppend(rest, 4)

# Parâmetros e listas inicializadas para serem usadas no programa
notes = []
scaleNote = []
inicio = 0
fim = 0
fimCount = 0


# Inicio da verificação 
#Começo da música
for ch in chords:
	#verifica se a música está no compasso final para terminar na tônica
	fimCount += 1
	if fimCount == (len(chords)):
		fim = 1
	mesureT = 0
	inicio = 0
	#verifica o acorde que está sendo tocado e define a escala a ser utilizada
	if "m" in ch: 
		if (ch[1] == "-") or (ch[1] == "#"):
			scaleT = scale.MinorScale(ch[0:2])
		else:
			scaleT = scale.MinorScale(ch[0]) 
	elif ("7" in ch) and ("M" not in ch) and ("m" not in ch): 
		if (ch[1] == "-") or (ch[1] == "#"):
			scaleT = scale.MixolydianScale(ch[0:2])
		else:
			scaleT = scale.MixolydianScale(ch[0])
	else:
		if len(ch) > 1:
			if (ch[1] == "-") or (ch[1] == "#"):
				scaleT = scale.MajorScale(ch[0:2])
		else:
			scaleT = scale.MajorScale(ch[0])
	#pega os pitches da escala que foi definida a cima e transforma-os em notas
	scalePit = scaleT.getPitches()
	for i in range(0,len(scalePit)-1):
		scaleNote.append(note.Note(scalePit[i]))
	#coloca uma pausa na escala 
	r = note.Rest()
	r.duration.quarterLength = 1.0
	scaleNote.append(r)

	#Verifica se o compasso já terminou
	#Enquanto o tempo for menor que a fórmula de compasso ele acrescenta notas à melodia
	while mesureT < Ctemp:

		if inicio == 0:
			#primeira nota do compasso é sempre aleatória
			numnot = randint(0,len(scaleNote)-1)
			inicio = 2

			#Coloca o acorde no início do compasso durando 4 tempos (fórmula de compasso)
			if ch == "C#":
				doclone = deepcopy(doS)
				cifra.append(doclone)
			elif ch == "F#":
				faclone = deepcopy(faS)
				cifra.append(faclone)
			elif ch == "B":
				siclone = deepcopy(si)
				cifra.append(siclone)
			elif ch == "D#m7":
				reclone = deepcopy(reSm7)
				cifra.append(reclone)
			elif ch == "B-7":
				sibclone = deepcopy(sib7)
				cifra.append(sibclone)
			elif ch == "B7":
				si7clone = deepcopy(si7)
				cifra.append(si7clone)
			elif ch == "G#7":
				solclone = deepcopy(solS7)
				cifra.append(solclone)
			elif ch == "F#m":
				famclone = deepcopy(faSmenor)
				cifra.append(famclone)
			
			
		#Se for o último compasso
		elif fim == 1:
			# Para terminar com a tônica
			if mesureT == 3:
				numnot = 0
			#se ainda não for o último tempo do último compasso continua normalmente
			else:
				if numnot == 0:
					indice ="zero"
				elif numnot == 1:
					indice ="um"
				elif numnot == 2:
					indice ="dois"
				elif numnot == 3:
					indice ="tres"
				elif numnot == 4:
					indice ="quatro"
				elif numnot == 5:
					indice ="cinco"
				elif numnot == 6:
					indice ="seis"
				elif numnot == 7:
					indice ="sete"
				else:
					indice = "um"
				numindice = randint(0,len(dados[indice])-1)
				numnot = dados[indice][numindice]
		# Pega o nome da lista que precisamos de acordo com a nota tocada anteriormente para
		#criar uma melodia de acordo com as listas de probabilidade criadas a partis dos dados
		else:
			if numnot == 0:
				indice ="zero"
			elif numnot == 1:
				indice ="um"
			elif numnot == 2:
				indice ="dois"
			elif numnot == 3:
				indice ="tres"
			elif numnot == 4:
				indice ="quatro"
			elif numnot == 5:
				indice ="cinco"
			elif numnot == 6:
				indice ="seis"
			elif numnot == 7:
				indice ="sete"
			else:
				indice = "um"
			numindice = randint(0,len(dados[indice])-1)
			numnot = dados[indice][numindice]
		#aumenta o tempo de compasso para que quando tivermos 4 notas ele mude de acorde
		mesureT += 1
		#Define a duração para cada note - um tempo do compasso
		scaleNote[numnot].duration.quarterLength = 1
		#clona a nota para que seja possível apenas defini-la uma vez
		clone = deepcopy(scaleNote[numnot])
		#Coloca a nota na part da melodia
		s.append(clone)

#Coloca cada part na Stream da música total
st.insert(0,p1)
st.insert(0,cifra)
st.insert(0,s)
#Grava um arquivo Midi com a música criada
mf = midi.translate.streamToMidiFile(st)
mf.open('imp3.mid', 'wb')
mf.write()
mf.close()
#abre a música quando o código é rodado
st.show('midi')

