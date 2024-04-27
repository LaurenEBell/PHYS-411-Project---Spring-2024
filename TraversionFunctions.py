import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random as rand

# Different traversions of the network: base traversion, traversion with adiabatic change to utility function, and 
# adiabatic change (perturbation) to a matrix

# Returns the coordinates for a player's utility over a base game traversion (no changes)

# BASE TRAVERSION
def play_base_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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
                R_it = network.nodes[neighbor]['value']
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
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break

    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        # of.close()
        return tot_utility_list, it_utility_list, moves_list
    
    # of.close()
    return tot_utility_list, it_utility_list, moves_list

# Returns the coordinates for a player's utilityover a traversion with adiabatic changes to the utility function
# Multaplicative adiabatic changes

# Cooperation (Increase or Decrease)
def play_mult_adiabatic_UF_C_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_coop = adia_coop * 1.001
            # adia_coop = adia_coop * 0.999
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break
    
    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
        
    return tot_utility_list, it_utility_list, moves_list

# Effort (Increase or Decrease)
def play_mult_adiabatic_UF_E_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):       
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_effort = adia_effort * 1.001
            # adia_effort = adia_effort * 0.999
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break
    
    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
      
    return tot_utility_list, it_utility_list, moves_list

# Risk (Increase or Decrease)
def play_mult_adiabatic_UF_r_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_risk = adia_risk * 1.001
            # adia_risk = adia_risk * 0.999
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break

    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
    
    return tot_utility_list, it_utility_list, moves_list

# Movement-aversion (Increase or Decrease)
def play_mult_adiabatic_UF_a_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_m_aversion = adia_m_aversion * 1.001
            # adia_m_aversion = adia_m_aversion * 0.999
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1
            
            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break

    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
    
    return tot_utility_list, it_utility_list, moves_list

# Cost (Increase or Decrease)
def play_mult_adiabatic_UF_c_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_cost = adia_cost * 1.001
            # adia_cost = adia_cost * 0.999
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break

    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
    
    return tot_utility_list, it_utility_list, moves_list

# Returns the coordinates for a player's utilityover a traversion with adiabatic changes to the utility function
# Additive adiabatic changes

# Cooperation (Increase or Decrease)
def play_add_adiabatic_UF_C_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # determining the range for the adiabatic change while staying within the parameters
        add_increase = (2 - coop) / 1000 # take 1000 steps to become the most cooperative
        add_decrease = coop / 1000 # take 1000 steps to become the least cooperative

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_coop = adia_coop + add_increase
            # adia_coop = adia_coop - add_decrease
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break
    
    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
        
    return tot_utility_list, it_utility_list, moves_list

# Effort (Increase or Decrease)
def play_add_adiabatic_UF_E_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # determining the range for the adiabatic change while staying within the parameters
        add_increase = (2 - effort) / 1000 # take 1000 steps to get highest effort
        add_decrease = effort / 1000 # take 1000 steps to get lowest effort

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_effort = adia_effort + add_increase
            # adia_effort = adia_effort - add_decrease
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break
    
    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
        
    return tot_utility_list, it_utility_list, moves_list

# Risk (Increase or Decrease)
def play_add_adiabatic_UF_r_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # determining the range for the adiabatic change while staying within the parameters
        add_increase = (2 - risk) / 1000 # take 1000 steps to become most risk-seeking
        add_decrease = risk / 1000 # take 1000 steps to become most rirsk-averse

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_risk = adia_risk + add_increase
            # adia_risk = adia_risk - add_decrease
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break
    
    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
        
    return tot_utility_list, it_utility_list, moves_list

# Movement-aversion (Increase or Decrease)
def play_add_adiabatic_UF_a_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # determining the range for the adiabatic change while staying within the parameters
        add_increase = (2 - m_aversion) / 1000 # take 1000 steps to become the most movement-averse
        add_decrease = m_aversion / 1000 # take 1000 steps to become the least movement-averse

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_m_aversion = adia_m_aversion + add_increase
            # adia_m_aversion = adia_m_aversion - add_decrease
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break
    
    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
        
    return tot_utility_list, it_utility_list, moves_list

# Cost (Increase or Decrease)
def play_add_adiabatic_UF_c_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # determining the range for the adiabatic change while staying within the parameters
        add_increase = (2 - cost) / 1000 # take 1000 steps to become the most cooperative
        add_decrease = cost / 1000 # take 1000 steps to become the least cooperative

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_cost = adia_cost + add_increase
            # adia_cost = adia_cost - add_decrease
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break
    
    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
        
    return tot_utility_list, it_utility_list, moves_list

# What happens when 2+ adiabatic changes happen at once within the utility function? One example of this is
# adiabatically changing the cooperation and risk parameters...
# SITUATION: Let the player prefer more cooperation, but they become more averse to risk as it happens

# Multiplicative steps
def play_mult_adiabatic_UF_Cr_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_coop = adia_coop * 1.001
            # adia_coop = adia_coop * 0.999
            # adia_risk = adia_risk * 1.001
            adia_risk = adia_risk * 0.999
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break
    
    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
        
    return tot_utility_list, it_utility_list, moves_list

# Additive steps
def play_add_adiabatic_UF_Cr_game(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        # determining the range for the adiabatic change while staying within the parameters
        add_C_increase = (2 - coop) / 1000 # take 1000 steps to become the most cooperative
        add_C_decrease = coop / 1000 # take 1000 steps to become the least cooperative
        add_r_increase = (2 - risk) / 1000 # take 1000 steps to become most risk-seeking
        add_r_decrease = risk / 1000 # take 1000 steps to become most rirsk-averse

        # parameters
        adia_coop = coop
        adia_effort = effort
        adia_risk = risk
        adia_m_aversion = m_aversion
        adia_cost = cost

        while (num_of_losses < pi_losses):
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = adia_coop
                effort_it = adia_effort
                risk_it = adia_risk
                m_aversion_it = adia_m_aversion
                cost_it = adia_cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
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

            # TODO: Adiabatic increase or decrease?
            adia_coop = adia_coop + add_C_increase
            # adia_coop = adia_coop - add_C_decrease
            # adia_risk = adia_risk + add_r_increase
            adia_risk = adia_risk - add_r_decrease
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break
    
    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        return tot_utility_list, it_utility_list, moves_list
        
    return tot_utility_list, it_utility_list, moves_list

# In a separate situation, what happens when we introduce the rule of a player not being allowed to return
# to the node they are just coming from? Let's establish this with a modified base game...
def play_base_game_node_rule(network, start_node, pi_losses, coop, effort, risk, m_aversion, cost):
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

        while (num_of_losses < pi_losses):
            # print(f"Current node: {format(current_node)}")
            possible_iteration_utilities = []
            neighbor_nodes_list = []
            for neighbor in network.neighbors(current_node):
                coop_it = coop
                effort_it = effort
                risk_it = risk
                m_aversion_it = m_aversion
                cost_it = cost
                ith_move = moves + 1 # update the number of moves (this would be the ___ move)
                R_it = network.nodes[neighbor]['value']
                if (R_it < 0): # Switching neg sign position due to exponent
                    coop_it = coop_it * -1
                    R_it = R_it * -1
                
                # utility calculation
                loop_utility = (coop_it * ((R_it * effort_it) ** risk_it)) - (effort_it * cost_it * (ith_move ** m_aversion_it))
                possible_iteration_utilities.append(loop_utility)
                neighbor_nodes_list.append(network.nodes[neighbor]['num'])
                print(f"neighbor {network.nodes[neighbor]['num']} gets utility {loop_utility}")
            
            # noting the previous node
            if (moves > 0):
                hist_node = previous_node
            previous_node = current_node
            
            # choosing a path based on which gives the highest utility
            iteration_utility = max(possible_iteration_utilities)
            print(f"HIGHEST: {iteration_utility}")
            
            # sending the player to the next node
            holding_index = possible_iteration_utilities.index(iteration_utility) # indices will match, parallel
            current_node = network.nodes[neighbor_nodes_list[holding_index]]['num']
            print(f"before rule: current node: {current_node}")

            # NODE RULE - Cannot go back to the previous node
            if (hist_node == current_node):
                sorted_utility = sorted(possible_iteration_utilities) # sorting from lowest to highest
                iteration_utility = sorted_utility[-2] # next best option given the rule
                
                holding_index = possible_iteration_utilities.index(iteration_utility)
                current_node = network.nodes[neighbor_nodes_list[holding_index]]['num'] # resets the current_node
                print(f"if statement: current node: {current_node}")

            # updating the number of moves made
            moves = moves + 1
        
            # adding gained iteration utility to total utility
            total_utility = total_utility + iteration_utility
            # adding a coordinate point to the lists of coordinates
            tot_utility_list.append(total_utility) # Utility gain
            it_utility_list.append(iteration_utility) # Iteration utility
            moves_list.append(moves) # Moves
            
            # if the player has had more than their given number of losses, traversion ends on next loop check
            if (iteration_utility < 0):
                num_of_losses = num_of_losses + 1

            if (iteration_utility > 1000000 or iteration_utility < -1000000 or moves == 1000):
                break

    except RuntimeWarning:
        print("Warning: Overflow encountered. Returning default value.")
        # of.close()
        return tot_utility_list, it_utility_list, moves_list
    
    # of.close()
    return tot_utility_list, it_utility_list, moves_list
