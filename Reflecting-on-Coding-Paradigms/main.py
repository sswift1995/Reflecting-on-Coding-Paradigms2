'''
Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

>>> flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4})
{'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
'''


def flatten_dict(d):
  """Flattens a nested dictionary.
  keys must be strings in all dictionaries for this to work.
    """
  result = dict()
  for i in d.keys():
    if type(d[i]) == dict:
      #value = dictionary, result to flatten
      for k, v in d[i].items():
        #make new key
        new_key = i + "." + k
        #add k:v pair
        result[new_key] = v
    else:
      #add k:v pair = result dictionary
      result[i] = d[i]
  return result


print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))
'''
Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.

>>> unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4})
{'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
'''


def unflatten_dict(d):
  """Unflattens a nested dictionary. (reverses flatten_dict)
  keys must be strings in all dictionaries for this to work.
    """
  result = dict()
  for i in d.keys():
    if "." in i:
      #this should become nested
      new_key, sep, inner_key = i.partition(".")
      #create dictionary
      if new_key not in result.keys():
        result[new_key] = dict()


#add elements to inner dictionary
      result[new_key][inner_key] = d[i]
    else:
      #add the k:v pair = result dictionary
      result[i] = d[i]
  return result

print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))
'''
Problem 3: Write a function treemap to map a function over nested list.

>>> treemap(lambda i: i*i, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
'''


def treemap(func, lst):
  #loop that iterates over input list
  for i in range(len(lst)):
    #conditional statement at index i in the list lst
    if type(lst[i]) == list:
      lst[i] = treemap(func, lst[i])
    else:
      lst[i] = func(lst[i])

  return lst


print(treemap(lambda i: i * i, [1, 2, [3, 4, [5]]]))
