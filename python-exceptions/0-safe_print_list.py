#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count


if __name__ == "__main__":
    my_list = [1, "me", 3, "turnup", 8]
    result = safe_print_list(my_list, 7)
    print("Number of elements printed:", result)
