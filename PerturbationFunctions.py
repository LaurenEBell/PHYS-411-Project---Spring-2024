import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random as rand

# Perturbing a given matrix with another matrix that induces a small change on the elements

# Perturbing the interaction matrix, returns resulting matrix
def play_adiabatic_matrix_UniformRij_game(network, start_node, interact_matrix, players, player_i, pi_losses, coop, effort, risk, m_aversion, cost):
    try:
        tot_utility_list = []
        it_utility_list = []
        moves_list = []
        
        # when keeping track of nodes, pass around the 'num' value (same as value i for player i)
        current_node = network.nodes[start_node]['num']
        num_of_losses = 0

        total_utility = 0
        iteration_utility = 0
        moves = 0

        adia_interact_matrix = interact_matrix
        perturbing_matrix = np.eye(players) # creates an identity matrix
        for a in range(players):
            perturbing_matrix[a][a] = 1.001

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = coop
                effort_it = effort
                risk_it = risk
                m_aversion_it = m_aversion
                cost_it = cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = adia_interact_matrix[player_i][neighbor]
                if (R_it < 0): # Switching neg sign position due to exponent
                    coop_it = coop_it * -1
                    R_it = R_it * -1
                
                # utility calculation
                loop_utility = (coop_it * ((R_it * effort_it) ** risk_it)) - (effort_it * cost_it * (ith_move ** m_aversion_it))
                possible_iteration_utilities.append(loop_utility)
                neighbor_nodes_list.append(network.nodes[neighbor]['num'])
            
            # choosing a path based on which gives the highest utility
            iteration_utility = max(possible_iteration_utilities)
            
            # sending the player to the next node
            holding_index = possible_iteration_utilities.index(iteration_utility) # indices will match, parallel
            current_node = network.nodes[neighbor_nodes_list[holding_index]]['num']

            # updating the number of moves made
            moves = moves + 1
        
            # adding gained iteration utility to total utility
            total_utility = total_utility + iteration_utility
            # adding a coordinate point to the lists of coordinates
            tot_utility_list.append(total_utility) # Utility gain
            it_utility_list.append(iteration_utility) # Iteration utility
            moves_list.append(moves) # Moves

            # Applying the perturbation to the interaction matrix
            adia_interact_matrix = adia_interact_matrix @ perturbing_matrix
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break

    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
    
    return tot_utility_list, it_utility_list, moves_list

def play_adiabatic_matrix_RandomRij_game(network, start_node, interact_matrix, players, player_i, pi_losses, coop, effort, risk, m_aversion, cost):
    try:
        tot_utility_list = []
        it_utility_list = []
        moves_list = []
        
        # when keeping track of nodes, pass around the 'num' value (same as value i for player i)
        current_node = network.nodes[start_node]['num']
        num_of_losses = 0

        total_utility = 0
        iteration_utility = 0
        moves = 0

        adia_interact_matrix = interact_matrix
        perturbing_matrix = np.eye(players) # creates an identity matrix
        for a in range(players):
            perturbing_matrix[a][a] = rand.uniform(1, 1.01)

        while (num_of_losses < pi_losses):   
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = coop
                effort_it = effort
                risk_it = risk
                m_aversion_it = m_aversion
                cost_it = cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = adia_interact_matrix[player_i][neighbor]
                if (R_it < 0): # Switching neg sign position due to exponent
                    coop_it = coop_it * -1
                    R_it = R_it * -1
                
                # utility calculation
                loop_utility = (coop_it * ((R_it * effort_it) ** risk_it)) - (effort_it * cost_it * (ith_move ** m_aversion_it))
                possible_iteration_utilities.append(loop_utility)
                neighbor_nodes_list.append(network.nodes[neighbor]['num'])
            
            # choosing a path based on which gives the highest utility
            iteration_utility = max(possible_iteration_utilities)
            
            # sending the player to the next node
            holding_index = possible_iteration_utilities.index(iteration_utility) # indices will match, parallel
            current_node = network.nodes[neighbor_nodes_list[holding_index]]['num']

            # updating the number of moves made
            moves = moves + 1
        
            # adding gained iteration utility to total utility
            total_utility = total_utility + iteration_utility
            # adding a coordinate point to the lists of coordinates
            tot_utility_list.append(total_utility) # Utility gain
            it_utility_list.append(iteration_utility) # Iteration utility
            moves_list.append(moves) # Moves

            # Applying the perturbation to the interaction matrix
            adia_interact_matrix = adia_interact_matrix @ perturbing_matrix
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 100000 or iteration_utility < -100000 or moves == 1000):
                break

    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
    
    return tot_utility_list, it_utility_list, moves_list

# Random/Scattered perturbation matrix along with the rule that a player cannot return to the node they were just at
def play_adiabatic_matrix_RandomRij_game_node_rule(network, start_node, interact_matrix, players, player_i, pi_losses, coop, effort, risk, m_aversion, cost):
    try:
        tot_utility_list = []
        it_utility_list = []
        moves_list = []
        
        # when keeping track of nodes, pass around the 'num' value (same as value i for player i)
        current_node = network.nodes[start_node]['num']
        previous_node = 0
        hist_node = 0
        num_of_losses = 0

        total_utility = 0
        iteration_utility = 0
        moves = 0

        adia_interact_matrix = interact_matrix
        perturbing_matrix = np.eye(players) # creates an identity matrix
        for a in range(players):
            perturbing_matrix[a][a] = rand.uniform(1, 1.01)

        while (num_of_losses < pi_losses):   
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = coop
                effort_it = effort
                risk_it = risk
                m_aversion_it = m_aversion
                cost_it = cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = adia_interact_matrix[player_i][neighbor]
                if (R_it < 0): # Switching neg sign position due to exponent
                    coop_it = coop_it * -1
                    R_it = R_it * -1
                
                # utility calculation
                loop_utility = (coop_it * ((R_it * effort_it) ** risk_it)) - (effort_it * cost_it * (ith_move ** m_aversion_it))
                possible_iteration_utilities.append(loop_utility)
                neighbor_nodes_list.append(network.nodes[neighbor]['num'])
            
            # noting the previous node
            if (moves > 0):
                hist_node = previous_node
            previous_node = current_node
            
            # choosing a path based on which gives the highest utility
            iteration_utility = max(possible_iteration_utilities)
            
            # sending the player to the next node
            holding_index = possible_iteration_utilities.index(iteration_utility) # indices will match, parallel
            current_node = network.nodes[neighbor_nodes_list[holding_index]]['num']

            # NODE RULE - Cannot go back to the previous node
            if (hist_node == current_node):
                sorted_utility = sorted(possible_iteration_utilities) # sorting from lowest to highest
                iteration_utility = sorted_utility[-2] # next best option given the rule
                
                holding_index = possible_iteration_utilities.index(iteration_utility)
                current_node = network.nodes[neighbor_nodes_list[holding_index]]['num'] # resets the current_node

            # updating the number of moves made
            moves = moves + 1
        
            # adding gained iteration utility to total utility
            total_utility = total_utility + iteration_utility
            # adding a coordinate point to the lists of coordinates
            tot_utility_list.append(total_utility) # Utility gain
            it_utility_list.append(iteration_utility) # Iteration utility
            moves_list.append(moves) # Moves

            # Applying the perturbation to the interaction matrix
            adia_interact_matrix = adia_interact_matrix @ perturbing_matrix
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 100000 or iteration_utility < -100000 or moves == 1000):
                break

    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
    
    return tot_utility_list, it_utility_list, moves_list
