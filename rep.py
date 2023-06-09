import random
import networkx as nx
import matplotlib.pyplot as plt

def representation(dist,path,n):
    G = nx.Graph()
    G.add_nodes_from(range(n))

    list = []
    for i in range(0,len(path)):
        if len(path)-1==i:
            break
        list.append((path[i],path[i+1]))
    list.append((path[len(path)-1],path[0]))

    for i in range(n):
        for j in range(i+1, n):
            if (i,j) not in list and (j,i) not in list:
                G.add_edge(i, j, linestyle='dotted',color='black',weight=dist[i][j])
            else:
                G.add_edge(i, j, linestyle='solid',color='green',weight=dist[i][j])


    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos=pos, node_color="lightblue", node_size=500)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos=pos, font_size=12, font_weight="bold")
    
    # Draw edges
    edges = G.edges()
    edge_styles = nx.get_edge_attributes(G, 'linestyle')
    edge_colors = nx.get_edge_attributes(G, 'color')
    edge_weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edges(G, pos=pos, edgelist=edges, style=edge_styles.values(), edge_color=edge_colors.values())
    
    for (u, v), weight in edge_weights.items():
        x = (pos[u][0] + pos[v][0]) / 2 
        y = (pos[u][1] + pos[v][1]) / 2 
        offset_x = random.uniform(-0.1, 0.1)
        offset_y = random.uniform(-0.1, 0.1)
        plt.text(x + offset_x, y + offset_y, weight, fontsize=10, ha='left', va='bottom')
    

    plt.axis("off")
    plt.show()
