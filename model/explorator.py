class Explorator:
	def __init__(self, explorator_id, starting_edge):
		self.explorator_id = explorator_id
		self.path = [starting_edge] # list d'instance de la classe Edge

	def get_current_node(self):
		return self.path[-1].downstream_node


	def move_to_next_edge(self, next_edge):
		self.path.append(next_edge)


	def get_total_distance(self):
		return sum(self.path)