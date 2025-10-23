import pandas


def prepare_data(explorator_df):

	adjacent_table = {row["noeud_amont"] : row["noeud_aval"] for _, row in explorator_df.iterrows()}
	
	starting_nodes = explorator_df[explorator_df["type_aretes"] == "depart"]["noeud_amont"].values
	
	ending_nodes = set(explorator_df[explorator_df["type_aretes"] == "arrivee"]["noeud_aval"].values)

	return adjacent_table, starting_nodes, ending_nodes


def find_explorators_paths(adjacent_table, starting_nodes, ending_nodes):
	# dans chaque itération on construit pour 1 explorateur
	for starting_node in starting_nodes:
		current_path = [starting_node]
		current_node = current_path[-1]

		while current_node not in ending_nodes:
			next_node = adjacent_table[current_node]
			current_path.append(next_node)
			current_node = current_path[-1]
		
		print(current_path)
		print("_"*20)			






explorator_df = pandas.read_csv("./parcours_explorateurs.csv")
adjacent_table, starting_nodes, ending_nodes = prepare_data(explorator_df)
# print(ending_nodes)
find_explorators_paths(adjacent_table, starting_nodes, ending_nodes)
