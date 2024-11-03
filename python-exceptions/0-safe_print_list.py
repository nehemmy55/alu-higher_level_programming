#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end=' ')
            count += 1
        except :
            break
    print() 
    return count

my_list = [1, "hello", 3.5, "world", 5]
num_elements = safe_print_list(my_list, 7)
print(f"\nNumber of elements printed: {num_elements}")
