# groupby
#
# Group an array of arrays by identity using the given field number
#
# example (group by the third value)
#
#       print groupby([
#           ["house", "4",  "false" ],
#           ["house", "3",  "true"  ],
#           ["car",   "1",  "false" ],
#           ["dog",   "0",  "false" ]
#       ], 2)
#
#       result:
#       {
#           'true': [
#               ['house', '3', 'true']
#           ],
#           'false': [
#               ['house', '4', 'false'],
#               ['car', '1', 'false'],
#               ['dog', '0', 'false']
#           ]
#       }

def groupby(array,index=0):
    obj = {}
    for el in array:
        if str(el[index]) in obj:
            obj[str(el[index])].append(el)
        else:
            obj[str(el[index])] = [el]
    return obj
