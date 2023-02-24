# -*- coding: utf-8 -*-
"""
@author: Augusto Fonseca and Rodrigo Dornelles
"""

tower_A_orig = []
tower_B_dest = []
tower_C_aux = []

def Tower_of_Hanoi(n_rings, origin, destination, aux): # Move the rings between towers
    # If you only have one ring, just move to the destination tower
    print("O número n é:", n_rings)
    if n_rings == 1:
        print("Move ring 1 from tower", origin, "to tower", destination, ".")
        return
    '''
    The next line of code will call the method recursively, "reducing the number of rings" (recursively) by one each time. 
    In practice, this logic will focus on the initial rings (from the top) to the bottom.
    The basic function is to move the 2 initial rings and then call it recursively.
    For instance, we will decrease the number of rings from 5 to 4,3 and 2. 
    When it`s "2", we will make the following steps:
    a-) move the 1st one to the auxiliary Tower
    b-) move the 2nd one to the destination
    c-) recover the 1st ring from aux tower to the destination Tower, above the 2nd one.
    Then the function does the reverse path (increasing the n by one unit) to repeat that movement, and so on. 
    '''
    # Attention to the parameters: the next line will move from origin to aux
    Tower_of_Hanoi(n_rings-1, origin, aux, destination)
    #
    # Move the next ring from the origin to the destination
    print("Move ring", n_rings,  "from tower", origin, "to tower", destination, ".")
    #Call the method again to recover the ring from the aux Tower to the destination Tower.
    Tower_of_Hanoi(n_rings-1, aux,destination, origin)

n_rings = 5

Tower_of_Hanoi(n_rings, 'A', 'B', 'C')