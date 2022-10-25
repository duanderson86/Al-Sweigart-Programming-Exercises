#Takes any equal-sized lists and formats them in a visually pleasing table

sizes = {}

def printTable(t_lists):
    '''prints any same-sized lists in a table'''
    length = len(t_lists[0]) #check length once, more performant
    for i in range(0,length):
        #calculates longest string in each column
        for list in t_lists:
            sizes.setdefault(i, 0)
            if len(list[i]) > sizes[i]:
                sizes[i] = len(list[i])
    
    for list in t_lists:
        #creates tablet one row at a time
        for i in range(0,length):
            print(list[i].rjust(sizes[i]), end=' ')
        print('\n')
    return sizes
  
print


t_data = [['Alice', 'Bob', 'Carol', 'David'],
          ['apples', 'oranges', 'cherries', 'banana'],
          ['dogs', 'cats', 'moose', 'goose']]

printTable(t_data)
