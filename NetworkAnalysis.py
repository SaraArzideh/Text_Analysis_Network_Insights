import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Co_occurrence_df is the DataFrame with co-occurrence data
co_occurrence_df = pd.read_csv('filtered_co_occurrence_data.csv')

# Creating a graph
G = nx.Graph()

# Adding edges to the graph based on co-occurrences
for index, row in co_occurrence_df.iterrows():
    G.add_edge(row['Keyword'], row['Co-occurring Word'], weight=row['Frequency'])

# Visualising the network
plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, k=0.1)  # k regulates the distance between nodes
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray')
plt.show()
