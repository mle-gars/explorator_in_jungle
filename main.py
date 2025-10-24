import pandas
from model.explorator import Explorator
from model.edge import Edge


def prepare_data(explorator_df):
	adjacent_table = {}
	for _, row in explorator_df.iterrows()
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
	for starting_node in starting_nodes:
		current_path = [starting_node] # l'explorateur débute l'aventure
		current_node = current_path[-1] # on reccupère l'information lié à la position en cours de l'explorateur
		distance= 0

		# tant que l'explorateur n'a pas atteint un des points finaux de l'exploration
		while current_node not in ending_nodes: 
			# la randonnée de la journée en cours : on réccupère le noeud de la fin de journée ainsi que la distance parcourue pdt la journée
			next_node, current_distance = adjacent_table[current_node]


			# on stocker la noeud où l'explorateur est arrivé en fin de journée
			current_path.append(next_node)

			# on comptablise la distance parcourue dans la journée
			distance += current_distance
			
			# on actualiser l'information lié à la position en cours de l'explorateur
			current_node = current_path[-1]
		
		print(f"La distance parcourue: {distance:.3f} Kms ")# prooo

		print(current_path)
		print("_"*20)			






explorator_df = pandas.read_csv("./parcours_explorateurs.csv")
adjacent_table, starting_nodes, ending_nodes = prepare_data(explorator_df)
# print(ending_nodes)
find_explorators_paths(adjacent_table, starting_nodes, ending_nodes)
