import numpy as np

unsorted_list = [7, 10, 9, 8]


unsorted_list = [10, 7, 9, 8]

holder_list = unsorted_list.copy()

number_steps = np.floor(len(holder_list)**0.5) 


# for step in range(number_steps):
#%%

step_outer = 0

jump_size = 2**step_outer


np.ceil(number_steps/2)


step_inner = 0

cursor_left = 0 + 2*step_inner
cursor_right = 1 + 2*step_inner

if holder_list[cursor_left] > holder_list[cursor_right]:
    holder_list[cursor_right], holder_list[cursor_left] = \
        holder_list[cursor_left], holder_list[cursor_right]
else:
    if cursor_right == jump_size + cursor_left:
        if cursor_left == jump_size - 1:
            print("continue")
            pass
            # continue
        else:
            cursor_left += 1
    else:
        cursor_right += 1


#%%
step_inner += 1 

cursor_left = 0 + 2*step_inner
cursor_right = 1 + 2*step_inner

if holder_list[cursor_left] > holder_list[cursor_right]:
    holder_list[cursor_right], holder_list[cursor_left] = \
        holder_list[cursor_left], holder_list[cursor_right]
else:
    if cursor_right == jump_size + cursor_left:
        if cursor_left == jump_size - 1:
            print("continue")
            pass
            # continue
        else:
            cursor_left += 1
    else:
        cursor_right += 1








#%%



cursor_left += jump_size
cursor_right += jump_size

if holder_list[cursor_left] > holder_list[cursor_right]:
    holder_list[cursor_right], holder_list[cursor_left] = \
        holder_list[cursor_left], holder_list[cursor_right]


cursor_left = 0
cursor_right = jump_size




if holder_list[cursor_left] > holder_list[cursor_right]:
    holder_list[cursor_right], holder_list[cursor_left] = \
        holder_list[cursor_left], holder_list[cursor_right]
else:
    if cursor_right == jump_size + cursor_left - 1:
        cursor_left += 1
    else:
        cursor_right += 1




if holder_list[cursor_left] > holder_list[cursor_right]:
    holder_list[cursor_right], holder_list[cursor_left] = \
        holder_list[cursor_left], holder_list[cursor_right]
else:
    if cursor_right == jump_size + cursor_left - 1:
        cursor_left += 1
    else:
        cursor_right += 1

