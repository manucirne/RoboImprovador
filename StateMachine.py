import smach
import mido

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

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)
track.append(mido.Message('program_change', program=12, time=0))

class Grau1(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["IrGrau2", "IrGrau3", "IrGrau4", "IrGrau5", "IrGrau6", "IrGrau7"])

	def execute(self, userdata):
		return 

class Grau2(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["IrGrau1", "IrGrau3", "IrGrau4", "IrGrau5", "IrGrau6", "IrGrau7"])

	def execute(self, userdata):
		return 

class Grau3(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["IrGrau1", "IrGrau2", "IrGrau4", "IrGrau5", "IrGrau6", "IrGrau7"])

	def execute(self, userdata):
		return 

class Grau4(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["IrGrau1", "IrGrau2", "IrGrau3", "IrGrau5", "IrGrau6", "IrGrau7"])

	def execute(self, userdata):
		return 

class Grau5(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["IrGrau1", "IrGrau2", "IrGrau3", "IrGrau4", "IrGrau6", "IrGrau7"])

	def execute(self, userdata):
		return 

class Grau6(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["IrGrau1", "IrGrau2", "IrGrau3", "IrGrau4", "IrGrau5", "IrGrau7"])

	def execute(self, userdata):
		return 

class Grau7(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["IrGrau1", "IrGrau2", "IrGrau3", "IrGrau4", "IrGrau5", "IrGrau6"])

	def execute(self, userdata):
		return 

def main():	
	sm = smach.StateMachine(outcomes=[])
	with sm:
		smach.StateMachine.add('GRAU1', Grau1(),
								transitions={"IrGrau2":"GRAU2",
								"IrGrau3": "GRAU3",
								"IrGrau4": "GRAU4",
								"IrGrau5": "Grau5",
								"IrGrau6": "Grau6",
								"IrGrau7": "Grau7"})
		
		smach.StateMachine.add('GRAU2', Grau2(),
								transitions={"IrGrau1":"GRAU1",
								"IrGrau3": "GRAU3",
								"IrGrau4": "GRAU4",
								"IrGrau5": "Grau5",
								"IrGrau6": "Grau6",
								"IrGrau7": "Grau7"})

		smach.StateMachine.add('GRAU3', Grau3(),
								transitions={"IrGrau1":"GRAU1",
								"IrGrau2": "GRAU2",
								"IrGrau4": "GRAU4",
								"IrGrau5": "Grau5",
								"IrGrau6": "Grau6",
								"IrGrau7": "Grau7"})

		smach.StateMachine.add('GRAU4', Grau4(),
								transitions={"IrGrau1":"GRAU1",
								"IrGrau2": "GRAU2",
								"IrGrau3": "GRAU3",
								"IrGrau5": "Grau5",
								"IrGrau6": "Grau6",
								"IrGrau7": "Grau7"})

		smach.StateMachine.add('GRAU5', Grau5(),
								transitions={"IrGrau1":"GRAU1",
								"IrGrau2": "GRAU2",
								"IrGrau3": "GRAU3",
								"IrGrau4": "Grau4",
								"IrGrau6": "Grau6",
								"IrGrau7": "Grau7"})

		smach.StateMachine.add('GRAU6', Grau6(),
								transitions={"IrGrau1":"GRAU1",
								"IrGrau2": "GRAU2",
								"IrGrau3": "GRAU3",
								"IrGrau4": "Grau4",
								"IrGrau5": "Grau5",
								"IrGrau7": "Grau7"})

		smach.StateMachine.add('GRAU7', Grau7(),
								transitions={"IrGrau1":"GRAU1",
								"IrGrau2": "GRAU2",
								"IrGrau3": "GRAU3",
								"IrGrau4": "Grau4",
								"IrGrau5": "Grau5",
								"IrGrau6": "Grau6"})


	outcome = sm.execute()
