#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:38:31 2022

@author: goncalomorais
"""

import numpy as np
import random

n = 30

a_type= 15

utility_factor = 0.2 #normalize the utility to be between 0 and 1 - valu that they give us

mu, sigma = 0.4, 0.3 # mean and standard deviation of the outside option


#are we in the platform or no? Initial situation - 0 people in the platform

status = np.zeros((n), dtype=int)
data = [status]

goal = [np.ones((n), dtype=int)]

#define/ select who is the active agent
active = random.randrange(1, n+1)
active

num_a = len(status [0 : a_type-1]) #N of A type elements
num_b = len(status[a_type-1:-1]) #N of B type elements

ind_status = status[active] #state of the active agent - if he is in the platform or not


#in the fee we now need to model it as also if the platform is optimizng it's value for the long term

    
def fee(ind_status):
        '''fee that the platform charges to the active agent.'''
        '''Varies if the user it's on the platform or no.'''
        ''''Both types pay the same, function of being in the plaform or no'''
            
        ind_status = status[active] #state of the active agent - if he is in the platform or not
            
        if ind_status == 0:  #if the active agent has a status equal to 0 agent is outside of the platform
            return ind_status + 0.1
                
        else:    #agent is inside of the platform
            return 1.1
    
            print(fee(ind_status))
    
def act_type(active):
        '''seeing the type of the active agent'''
        if active >= a_type -1 :
            act_type = 'b'
        else:
            act_type = 'a'
        return act_type
    
act_type = act_type(active)
    
def util_of_plat(act_type):
        if act_type =='b':
            '''utility for a player if he is b type. The presence or no presence in the 
            platform is seen by the fee(ind_status)'''
            own_player_eff = -num_b * utility_factor  #put here some utility factors or leave everything the same
            other_player_eff = num_a * utility_factor
            fee(ind_status)
            
            return fee(ind_status) + own_player_eff + other_player_eff
        
        elif act_type == 'a':
            '''utility for a player if he is a type. The presence or no presence in the 
            platform is seen by the fee(ind_status)'''
            own_player_eff = -num_a * utility_factor
            other_player_eff = num_b * utility_factor
            
            return fee(ind_status) + own_player_eff + other_player_eff
    
        else:
            return 
            
util_of_plat = util_of_plat((act_type)) #Utility of being in the platform
    
util_of_out_opt = np.random.default_rng().normal(mu, sigma) #Utility of the outside option
    
def choice(util_of_plat, util_of_out_opt):
        if util_of_plat > util_of_out_opt:
            return util_of_plat, 'platform'
        else: 
            return util_of_out_opt, 'outside'
    
print(choice(util_of_plat, util_of_out_opt))
    
    
