import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random as rand

# Generate lists n elements long with random utility function parameters

# Random Cooperation Preferences (0 < C <= 2), returns list
def rand_cooperation_param(players):
    cooperation_list = [rand.uniform(0, 2) for _ in range(players)]
    # print(cooperation_list)
    return cooperation_list

# Random Effort Preferences (0 < E <= 2), returns list
def rand_effort_param(players):
    effort_list = [rand.uniform(0, 2) for _ in range(players)]
    # print(effort_list)
    return effort_list

# Random Risk Preferences (0 < r <= 2), returns list
def rand_risk_param(players):
    risk_list = [rand.uniform(0, 2) for _ in range(players)]
    # print(risk_list)
    return risk_list

# Random Movement-aversion Preferences (0 < a <= 2), returns list
def rand_m_aversion_param(players):
    m_aversion_list = [rand.uniform(0, 2) for _ in range(players)]
    # print(m_aversion_list)
    return m_aversion_list

# Random generation of all parameters for a single player, returns 4 variables
def rand_single_player_params():
    coop = rand.uniform(0, 2)
    effort = rand.uniform(0, 2)
    risk = rand.uniform(0, 2)
    m_aversion = rand.uniform(0, 2)
    return coop, effort, risk, m_aversion