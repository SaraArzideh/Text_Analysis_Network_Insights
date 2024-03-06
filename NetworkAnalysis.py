import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
additional_filters = set(["is", "the", "and", "to", "of", "in", "for", "on", "with", "as", "by", ])


# Co_occurrence_df is the DataFrame with co-occurrence data
co_occurrence_df = pd.read_csv('filtered_co_occurrence_data.csv')

# Creating a graph
G = nx.Graph()

# Adding edges to the graph based on co-occurrences
frequency_threshold = 60
for _, row in co_occurrence_df.iterrows():
    if row['Frequency'] >= frequency_threshold:
        G.add_edge(row['Keyword'], row['Co-occurring Word'], weight=row['Frequency'])

# Visualising the network
plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, k=0.2)  # k regulates the distance between nodes
nx.draw(G, pos, with_labels=True, font_size=8, font_weight='bold', node_size=40, node_color='skyblue', edge_color='gray')
plt.title("Co-occurrence Network")
plt.show()

# Identifying clusters
import community as community_louvain

# Detecting communities in the network
partition = community_louvain.best_partition(G)

# Visualizing the communities
plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, k=0.1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40, cmap=plt.cm.RdYlBu, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=8)
plt.show()
