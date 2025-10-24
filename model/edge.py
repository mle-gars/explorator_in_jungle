class Edge:
	def __init__(self, upstream_node, downstream_node, edge_type, distance, edge_id):
		self.upstream_node = upstream_node
		self.downstream_node = downstream_node
		self.edge_type = edge_type
		self.distance = distance
		self.edge_id = edge_id


	def __add__(self, other_edge):# (+)
		return self.distance + other_edge.distance


	def __radd__(self, other_object):# (sum())
		return self.distance + other_object


	def __repr__(self):
		return self.edge_id