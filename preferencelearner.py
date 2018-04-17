'''
shared variable target

fitness = |cost|^(-1) + |science| + alpha*(num_blocks-target)

1. Add user points to fitness_map
2. update target -> async
3. recompute fitness
4. pick jumping point
5. calculate local points
6. choose optimum points
7. add points to fitness_map

'''
from threading import Thread, Lock, Condition


class PreferenceLearner(self):
	incoming_configs = [] ## list of (config, science, cost)
	outgoing_configs = []
	def __init__(self):
		self.fitness_map = {} # configuration -> [science, cost, fitness]
		self.target = 0
		self.lock = Lock()


	def add_user_points_to_map(self):
		raise NotImplemented

	def update_target(self):
		raise NotImplemented

	def recompute_fitness(self):
		for config in self.fitness_map:
			cost, science, fitness = self.fitness_map[config]
			new_fitness = 

	def get_num_blocks(self, configuration):
		num_blocks = 0
		lst = list(configuration)
		for i in lst:
			if i == '1':
				num_blocks += 1
		return num_blocks



	def evaluate_architecture(self, configuration):
		return (0,0)


	def push_user_points(self, user_points):
		with self.lock:
			for i in user_points:
				incoming_points.append(i)


	def update_map(self):
		with self.lock:
			for i in incoming_points:
				config, science, cost = i
				fitness_map[config] = (science, cost, 0)
			incoming_points = []


	def compute_preferences(self):
		while true:
			update_map()
			





	

def run():
	p = Pre()

if __name__ == '__main__':
	run()




