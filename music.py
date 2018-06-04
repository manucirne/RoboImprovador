from music21 import *
from random import randint

tom = "Am"
chords = ["Am", "Bm", "E7", "Am", "Dm", "G7", "C", "Bm", "Em", "Am"]
s = stream.Stream()
s.id = 'some notes'
notes = []
myDuration = duration.Duration("quarter")

for ch in chords:
	if tom[-1] == "m":
		if "m" in ch: 
			if (ch[1] == "-") or (ch[1] == "#"):
				scaleT = scale.MelodicMinorScale(ch[0:2])
			else:
				scaleT = scale.MelodicMinorScale(ch[0]) 
		elif "7" in ch: 
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
	scaleT = scaleT.getPitches()
	for i in range(4):
		numnot = randint(0,len(scaleT)-1)
		s.append(note.Note(scaleT[numnot]))
	# for n in range(len(notes)):
	# 	notes[n].duration.type = "quarter"
		#print(notes[n])
		#s.append(notes[n])

mf = midi.translate.streamToMidiFile(s)
mf.open('imp1.mid', 'wb')
mf.write()
mf.close()
s.show('midi')

print(notes)

