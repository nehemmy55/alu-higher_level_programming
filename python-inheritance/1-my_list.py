#!/usr/bin/python3
 ''' inherted class from build in'''


class MyList(list):
  ''' inherted class from list '''
 
 def print_sorted(self):
        '''Prints the list in a sorted order  '''
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
