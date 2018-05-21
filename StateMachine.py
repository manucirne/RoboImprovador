import smach
import mido

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
