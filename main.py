import pandas
from model.explorator import Explorator
from model.edge import Edge


def prepare_data(explorator_df):
	adjacent_table = {}
	for _, row in explorator_df.iterrows():
		upstream_node = row["noeud_amont"]
		downstream_node = row["noeud_aval"]
		edge_type = row["type_aretes"]
		distance = row["distance"]
		edge_id = row["arete_id"]

		edge_object = Edge(upstream_node, downstream_node, edge_type, distance, edge_id)
		adjacent_table[upstream_node] = edge_object
	
	starting_nodes = explorator_df[explorator_df["type_aretes"] == "depart"]["noeud_amont"].values
	
	ending_nodes = set(explorator_df[explorator_df["type_aretes"] == "arrivee"]["noeud_aval"].values)

	return adjacent_table, starting_nodes, ending_nodes



def find_explorators_paths(adjacent_table, starting_nodes, ending_nodes):
	# dans chaque itération on construit pour 1 explorateur
	for index, starting_node in enumerate(starting_nodes):
		starting_edge = adjacent_table[starting_node]
		current_explorator = Explorator(explorator_id=index, starting_edge=starting_edge)
		current_node = current_explorator.get_current_node() # on reccupère l'information lié à la position en cours de l'explorateur


		# tant que l'explorateur n'a pas atteint un des points finaux de l'exploration
		while current_node not in ending_nodes: 
			# la randonnée de la journée en cours : on réccupère le noeud de la fin de journée ainsi que la distance parcourue pdt la journée
			next_edge = adjacent_table[current_node]

			# on stocker la noeud où l'explorateur est arrivé en fin de journée
			current_explorator.move_to_next_edge(next_edge)
			
			# on actualiser l'information lié à la position en cours de l'explorateur
			current_node = current_explorator.get_current_node()
		
		print(f"La distance parcourue: {current_explorator.get_total_distance():.3f} Kms ")# prooo

		print(current_explorator.path)
		print("_"*20)			






explorator_df = pandas.read_csv("./parcours_explorateurs.csv")
adjacent_table, starting_nodes, ending_nodes = prepare_data(explorator_df)
find_explorators_paths(adjacent_table, starting_nodes, ending_nodes)
