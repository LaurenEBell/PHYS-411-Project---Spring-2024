import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random as rand
from TraversionFunctions import play_base_game

# NETWORK PARAMETERS
gen_seed = 1
n = 30 # nodes (num of players)

# UTILITY FUNCTION
# U(x) = C(RE)^r - Ekx^a
coop = 1 # Cooperation preference
effort = 1 # Effort level
risk = 1 # Risk preference
m_aversion = 1 # Movement aversion
cost = 1 # Cost of movement

# PLAYER PARAMETERS
player_i = 0 # player of interest (0 to n-1)

# Setting the seed for any random generation
np.random.seed(gen_seed)

# Generating the interaction matrix
def random_positive_or_negative(value):
    return np.matmul(value, np.random.choice(np.array([-10, 10]), value.shape))
example_weights = np.random.rand(n, n)
interact_matrix = random_positive_or_negative(example_weights)
for a in range(n):
    interact_matrix[a][a] = 0
# print(interact_matrix)

# Generating the network
network = nx.fast_gnp_random_graph(n, 0.5, seed=gen_seed)
# Storing the interaction parameters for player i at each node
for b in range(n):
    network.nodes[b]['num'] = b
    network.nodes[b]['value'] = interact_matrix[player_i][b]

x_values = []
plot1_lines = []
plot2_lines = []

for c in reversed(range(12)):
    pi_loss = c
    # Base Player Network Traversion
    pi_utot, pi_its, pi_moves = play_base_game(network, network.nodes[player_i]['num'], pi_loss, coop, effort, risk, m_aversion, cost)

    plot1_lines.append(pi_utot)
    plot2_lines.append(pi_its)
    x_values.append(pi_moves)

# Graphing the total utility over moves
p1 = plt.figure(1)
for j, line1 in enumerate(plot1_lines):
    plt.plot(x_values[j], line1, linestyle='-', label='Losses Tolerable: {}'.format(j))
plt.title("LDR: Total Utility over Number of Moves")
plt.xlabel("Move")
plt.ylabel("Total Utility")
plt.legend()
p1.show()

# Graphing iteration utility over moves
p2 = plt.figure(2)
for j, line2 in enumerate(plot2_lines):
    plt.plot(x_values[j], line2, linestyle='-', label='Losses Tolerable: {}'.format(j))
plt.title("Utility Gained per Move")
plt.xlabel("Move")
plt.ylabel("Utility Gained per Iteration")
plt.legend()
p2.show()
        
# specifics of the network visual
p3 = plt.figure(3)
pos = nx.kamada_kawai_layout(network)
node_options = {"node_color": "blue", "node_size": 70}
edge_options = {"width": 0.50, "alpha": 0.4, "edge_color": "black"}
# Plotting the network
plt.figure(3, figsize=(8, 8))
nx.draw_networkx_nodes(network, pos, **node_options)
nx.draw_networkx_edges(network, pos, **edge_options)
plt.title("Player Interaction Network")
p3.show()

input("Press 'Enter' to close the plots and terminate the program...")