
# create a transistor
#%%
def transistor(state: bool = True) -> bool:
    """
    This functions represents the transistor.
    It returns the state of the transistor.
    """
    return state

def not_gate(state: bool) -> bool:
    return not(state)

def and_gate(stateA, stateB):
    transistor(stateA)
    # the exercise doesnt make sense kk

#%%
# not gate
stateA = True
stateA = False
transistor(stateA)
not_gate(transistor(stateA))

# a better exercise would be combine logic gates to do other stuff
# to build logic gates from scratch would be more educational with circuits
# where we are bound to the flow of electrons
