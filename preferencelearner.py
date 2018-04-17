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
import random
NUM_TRIES = 20
NUM_TAKE = 5
class PreferenceLearner:
	incoming_points = [] ## list of (config, science, cost)
	outgoing_points = []
	def __init__(self):
		self.fitness_map = {} # configuration -> [science, cost, fitness]
		self.target = 0
		self.lock = Lock()
		self.targetLock = Lock()


	def calc_local_pts(self, jump_config):
		with self.targetLock:
			config_tuples = []
			for i in range(0, NUM_TRIES):
				index = random.randint(0,60)
				config_lst = list(jump_config)
			
				if(config_lst[index] == 0):
					config_lst[index] = 1
				else:
					config_lst[index] = 0

				new_config = "".join(config_lst)
				science, cost = evaluate_architecture(new_config)
				fitness = cost + science + (get_num_blocks(config)-self.target)
				config_tuples.append((new_config, science, cost, fitness))

			sorted_config_tuples = sorted(configs, key = lambda a : a[3])[0:NUM_TAKE]
			return sorted_config_tuples

	def update_target(self):
		raise NotImplemented

	def recompute_fitness(self):
		max_fitness = 0
		max_config = ""
		for config in self.fitness_map:
			science, cost, fitness = self.fitness_map[config]
			new_fitness = cost + science + (get_num_blocks(config)-self.target)
			self.fitness_map[config] = (science, cost, new_fitness)
			if new_fitness > max_fitness:
				max_fitness = new_fitness
				max_config = config
		return max_config

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
			jump_config = recompute_fitness()
			config_tuples = calc_local_pts(jump_config)
			for config_tuple in config_tuples:
				config, science, cost, fitness = config_tuple
				fitness_map[config] = (science, cost, fitness)
			#post new configurations to user


	

def run():
	p = PreferenceLearner()
	p.compute_preferences()


if __name__ == '__main__':
	run()




