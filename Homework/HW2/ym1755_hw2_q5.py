'''
the odd numbers will appear first, and all the even numbers will appear last. Note
that the inner order of the odd numbers and the inner order of the even numbers
don’t matter.
'''

def split_parity(lst):
    curr_index = 0
    even_numbers = 0
    while curr_index < len(lst):
        if lst[curr_index] % 2 == 0:
            lst.append(lst.pop(curr_index))
            even_numbers += 1
        if even_numbers == (len(lst)-curr_index):
            return lst
        else:
            curr_index+=1
    return lst
