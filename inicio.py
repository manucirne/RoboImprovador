
import  mido
import  time
import random

# def Note(tom):
# 	tom = tom[0,len(tom)]
# 	if tom == "C":
# 		note = 48
# 	if tom == "D":
# 		note = 48+1
# 	if tom == "D":
# 		note = 48+2
# 	if tom == "DS":
# 		note = 48+3
# 	if tom == "E":
# 		note = 48+4
# 	if tom == "F":
# 		note = 48+5
# 	if tom == "FS":
# 		note = 48+6
# 	if tom == "G":
# 		note = 48+7
# 	if tom == "GS":
# 		note = 48+8
# 	if tom == "A":
# 		note = 48+9
# 	if tom == "AS":
# 		note = 48+10
# 	if tom == "B":
# 		note = 48+11
# 	return note


# #precisa organizar os ifs e conferir as escalas a partir do sexto grau
# def scale(chord,tom):
# 	note = Note(chord)
# 	if chord == tom:   # primeiro grau I
# 		scale = [note,note+2,note+4,note+5,note+7,note+9,note+11,note+12]  #Jônio
# 	if (chord[-1] == "m") or (chord[-1] == "7" and chord[-2] == "m"): #segundo grau II
# 		scale = [note,note+2,note+3,note+5,note+7,note+8,note+10,note+12]  #dórico
# 	if chord == (tom+5):   #terceiro grau   III
# 		scale = [note,note+1,note+3,note+5,note+7,note+8,note+10,note+12]   #frígio
# 	if chord == (tom+5):   #quarto grau   IV
# 		scale = [note,note+2,note+4,note+6,note+7,note+9,note+11,note+12]   #lídio
# 	if (chord[-1] == "7") and (chord[-2] != "m"): #quinto grau V
# 		scale = [note,note+2,note+4,note+5,note+7,note+9,note+10,note+12] #mixolídio
# 	if chord == (tom+5):   #sexto grau   VI
# 		scale = [note,note+2,note+4,note+5,note+7,note+9,note+10,note+12]   #eólico
# 	if chord == (tom+5):   #sétimo grau   VII
# 		scale = [note,note+2,note+4,note+5,note+7,note+9,note+10,note+12]   #lócrio
	


	
	
#notes numbers

C = 0+48
CS = C+1
D =  C+2
DS = C+3
E = C+4
F = C+5
FS = C+6
G = C+7
GS = C+8
A = C+9
AS = C+10
B = C+11

inst = 15

CMscale = [C,D,E,F,G,A,B,C+12] #Am
DMscale = [D,E,FS,G,A,B,CS+12,D+12] #Bm
EMscale = [E,FS,GS,A,B,CS+12,DS+12,E+12] #C#m
FMscale = [F,G,A,AS,C+12,D+12,E+12,F+12] #Dm
GMscale = [G,A,B,C+12,D+12,E+12,FS+12,G+12] #Em
AMscale = [A,B,CS+12,D+12,E+12,FS+12,GS+12,A+12] #F#m
BMscale = [B,CS+12,DS+12,E+12,FS+12,GS+12,AS+12,B+12] #G#m

tom = "G"
music = ["G","D","G","Em","G","Am","D","G"]

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)
track.append(mido.Message('program_change', program=12, time=0))

for chord in music:
	if chord == tom:
		for i in range(4):
			N = random.randint(0,7)
			track.append(mido.Message('note_on', channel = inst, note=GMscale[N], velocity=94, time=300))
	if chord == "D":
		for i in range(4):
			l=[1,3,4,6]
			N = random.randint(0,len(l)-1)
			track.append(mido.Message('note_on', channel = inst, note=GMscale[l[N]], velocity=94, time=300))
	if chord == "Em":
		for i in range(4):
			l=[0,2,4,5,7]
			N = random.randint(0,len(l)-1)
			track.append(mido.Message('note_on', channel = inst, note=GMscale[l[N]], velocity=94, time=300))
	if chord == "Am":
		for i in range(4):
			l=[0,1,3,5,7]
			N = random.randint(0,len(l)-1)
			track.append(mido.Message('note_on', channel = inst, note=GMscale[l[N]], velocity=94, time=300))



#msg  =  mido.Message('note_on', note=60)
#msg.note

#track.append(Message('note_off', note=64, velocity=127, time=32))

mid.save('Sapo.mid')