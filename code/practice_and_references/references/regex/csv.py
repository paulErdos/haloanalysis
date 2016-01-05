line = "0,1,2,3,4,5,6,7,8,9\n"

print line 

print line.rstrip()

print line.rstrip().split(',')

values = line.rstrip().split(',')

selection_indices = [4, 2]

selections = []
for index in selection_indices:
  selections.append(values[index])

print selections

