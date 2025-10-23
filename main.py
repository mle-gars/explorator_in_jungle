import pandas


explorator_df = pandas.read_csv("./parcours_explorateurs.csv")

# print(explorator_df.head(7))
# print(explorator_df.tail(7))
# print(len(explorator_df))

adjacent_table = {row["noeud_amont"] : row["noeud_aval"] for _, row in explorator_df.iterrows()}

starting_nodes = explorator_df[explorator_df["type_aretes"] == "depart"]["noeud_amont"].values
print(starting_nodes)