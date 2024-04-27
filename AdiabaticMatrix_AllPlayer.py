import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random as rand
from GenerationFunctions import rand_cooperation_param, rand_effort_param, rand_risk_param, rand_m_aversion_param
from PerturbationFunctions import play_adiabatic_matrix_UniformRij_game, play_adiabatic_matrix_RandomRij_game, \
play_adiabatic_matrix_RandomRij_game_node_rule
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
pi_losses = 3 # number of times player i accepts a negative iteration utility before quitting

# Setting the seed for any random generation
np.random.seed(gen_seed)

# Generating the interaction matrix
def random_positive_or_negative(value):
    return np.matmul(value, np.random.choice(np.array([-10, 10]), value.shape))
example_weights = np.random.rand(n, n)
interact_matrix = random_positive_or_negative(example_weights)
for a in range(n):
    interact_matrix[a][a] = 0

# U_x_values = []
# U_plot1_lines = []
# U_plot2_lines = []
R_x_values = []
R_plot1_lines = []
R_plot2_lines = []
# RN_x_values = []
# RN_plot1_lines = []
# RN_plot2_lines = []

# # # # # Use randomly generated parameters for players? (RESETS TO RANDOM PARAMS) # # # # #
choice = 'Y'
coop_list = rand_cooperation_param(n)
effort_list = rand_cooperation_param(n)
risk_list = rand_risk_param(n)
m_aversion_list = rand_m_aversion_param(n)

for i in range(n):
    # Generating the network
    network = nx.fast_gnp_random_graph(n, 0.5, seed=gen_seed)
    # Storing the interaction parameters for player i at each node
    for b in range(n):
        network.nodes[b]['num'] = b
        network.nodes[b]['value'] = interact_matrix[i][b]

    if choice == 'Y': # Random parameters
        # U_pi_utot, U_pi_its, U_pi_moves = play_adiabatic_matrix_UniformRij_game(network, network.nodes[i]['num'], interact_matrix, n, i, pi_losses, coop_list[i], effort_list[i], risk_list[i], m_aversion_list[i], cost)
        R_pi_utot, R_pi_its, R_pi_moves = play_adiabatic_matrix_RandomRij_game(network, network.nodes[i]['num'], interact_matrix, n, i, pi_losses, coop_list[i], effort_list[i], risk_list[i], m_aversion_list[i], cost)
        # RN_pi_utot, RN_pi_its, RN_pi_moves = play_adiabatic_matrix_RandomRij_game_node_rule(network, network.nodes[i]['num'], interact_matrix, n, i, pi_losses, coop_list[i], effort_list[i], risk_list[i], m_aversion_list[i], cost)
    else: # Uniform parameters
        # U_pi_utot, U_pi_its, U_pi_moves = play_adiabatic_matrix_UniformRij_game(network, network.nodes[i]['num'], interact_matrix, n, i, pi_losses, coop, effort, risk, m_aversion, cost)
        R_pi_utot, R_pi_its, R_pi_moves = play_adiabatic_matrix_RandomRij_game(network, network.nodes[i]['num'], interact_matrix, n, i, pi_losses, coop, effort, risk, m_aversion, cost)
        # RN_pi_utot, RN_pi_its, RN_pi_moves = play_adiabatic_matrix_RandomRij_game_node_rule(network, network.nodes[i]['num'], interact_matrix, n, i, pi_losses, coop, effort, risk, m_aversion, cost)

    # U_plot1_lines.append(U_pi_utot)
    # U_plot2_lines.append(U_pi_its)
    # U_x_values.append(U_pi_moves)

    R_plot1_lines.append(R_pi_utot)
    R_plot2_lines.append(R_pi_its)
    R_x_values.append(R_pi_moves)

    # RN_plot1_lines.append(RN_pi_utot)
    # RN_plot2_lines.append(RN_pi_its)
    # RN_x_values.append(RN_pi_moves)

# ONLY FOR GRAPHING 5 LINES
# warm_colors = ['#FF6FD0', '#ED1C7D' ,'#F94712', '#FF841B', '#F4D914']
# cool_colors = ['#23C43B', '#57F7C3', '#00D1F9', '#2354DE', '#B478EB']

# Graphing the total utility over moves
p1 = plt.figure(1)
# for j, line1 in enumerate(U_plot1_lines):
#     plt.plot(U_x_values[j], line1, linestyle='-', color=warm_colors[j], label='U.AP {}'.format(j))
for k, line1 in enumerate(R_plot1_lines):
    plt.plot(R_x_values[k], line1, linestyle='-', label='S.AP {}'.format(k))
# for u, line1 in enumerate(RN_plot1_lines):
#     plt.plot(RN_x_values[u], line1, linestyle='-', color=warm_colors[u], label='SN.AP {}'.format(u))
plt.title("Total Utility over Number of Moves")
plt.xlabel("Move")
plt.ylabel("Total Utility")
plt.legend()
p1.show()

# Graphing iteration utility over moves
p2 = plt.figure(2)
# for l, line2 in enumerate(U_plot2_lines):
#     plt.plot(U_x_values[l], line2, linestyle='-', color=warm_colors[l], label='U.AP {}'.format(l))
for m, line2 in enumerate(R_plot2_lines):
    plt.plot(R_x_values[m], line2, linestyle='-', label='S.AP {}'.format(m))
# for v, line2 in enumerate(RN_plot2_lines):
#     plt.plot(RN_x_values[v], line2, linestyle='-', color=warm_colors[v], label='SN.AP {}'.format(v))
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