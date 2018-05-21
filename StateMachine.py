import smach
import mido


class Brain(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["IrGrau1","IrGrau2", "IrGrau3", "IrGrau4", "IrGrau5", "IrGrau6", "IrGrau7"])

	def execute(self, userdata):
		return

class Grau1(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["ToBrain"])
		self.contador_tempo = 0
		self.tempo_maximo = 1600

	def execute(self, userdata):
		lista_notas = scale() #AQUI CADA ESTADO DEVE TER UMA LISTA DE NOTAS POSSÍVEIS, QUE ESTÃO SENDO CRIADAS NA FUNÇÃO SCALE DO OUTRO ARQUIVO
		for nota in lista_notas:
			

		if self.contador_tempo == tempo_maximo:
			self.contador_tempo = 0
			return "ToBrain"

class Grau2(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["ToBrain"])

	def execute(self, userdata):
		return 

class Grau3(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["ToBrain"])

	def execute(self, userdata):
		return 

class Grau4(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["ToBrain"])

	def execute(self, userdata):

		return 

class Grau5(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["ToBrain"])

	def execute(self, userdata):
		return 

class Grau6(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["ToBrain"])

	def execute(self, userdata):
		return 

class Grau7(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=["ToBrain"])

	def execute(self, userdata):
		return 

def main():

	sm = smach.StateMachine(outcomes=[])
	with sm:
		smach.StateMachine.add('BRAIN', Brain(),
								transitions= {"IrGrau1":"GRAU1",
								"IrGrau2": "GRAU2",
								"IrGrau3": "GRAU3",
								"IrGrau4": "Grau4",
								"IrGrau5": "Grau5",
								"IrGrau6": "Grau6"})

		smach.StateMachine.add('GRAU1', Grau1(),
								transitions={"ToBrain": "BRAIN"})
		
		smach.StateMachine.add('GRAU2', Grau2(),
								transitions={"ToBrain": "BRAIN"})

		smach.StateMachine.add('GRAU3', Grau3(),
								transitions={"ToBrain": "BRAIN"})

		smach.StateMachine.add('GRAU4', Grau4(),
								transitions={"ToBrain": "BRAIN"})

		smach.StateMachine.add('GRAU5', Grau5(),
								transitions={"ToBrain": "BRAIN"})

		smach.StateMachine.add('GRAU6', Grau6(),
								transitions={"ToBrain": "BRAIN"})

		smach.StateMachine.add('GRAU7', Grau7(),
								transitions= {"ToBrain": "BRAIN"})


	outcome = sm.execute()
