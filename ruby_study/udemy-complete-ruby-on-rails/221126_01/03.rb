
fname = "Tomy"
fname_2 = fname # fname_2 points to the same address as fname

p fname
p fname_2

# change fname_2
# fname is still pointing to Tomy
fname_2 = "Boby"

p fname # Tomy
p fname_2 # Boby
# string are copied, not referenced
