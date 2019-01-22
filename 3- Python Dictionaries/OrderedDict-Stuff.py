from collections import OrderedDict

### a regular unsorted dict
##seasons = { "Spring": 2,"Winter": 1, "Summer": 3, "Fall": 4}
##
### using an OrderedDIct to Sort by Dictionary Key
##order_by_key = OrderedDict(sorted(seasons.items(), key=lambda s: s[0]))
##print("Order_by_key's type is: ", (type(order_by_key)))
##print("Ordered By Key: ", order_by_key)
##
### using an OrderedDIct to Sort by Dictionary value
##order_by_value = OrderedDict(sorted(seasons.items(), key=lambda s: s[1]))
##print("Ordered By Value: ", order_by_value)
##
### using an OrderedDIct to Sort by the length of the key (so how may characters each key has)
##order_by_key_len = OrderedDict(sorted(seasons.items(), key=lambda s: len(s[0])))
##print("Ordered By Key Lengths: ", order_by_key_len)
##
### using an OrderedDIct to Sort by Dictionary value in reverse
##order_by_value_rev = OrderedDict(sorted(seasons.items(), key=lambda s: s[1] , reverse=True))
##print("Ordered By Value Reverse: ", order_by_value_rev)
##
### Note: when new keys are added, the keys are appended to the end and the sort is not maintained.
##order_by_value_rev["New Season"] = 5
##print("Added an element: ", order_by_value_rev, "5 is added to the end")
##
### new sorted dictionaries maintain their sort order when entries are deleted
##order_by_value_rev.pop("Winter")
##print("Ordered By Value After Delete: ", order_by_value_rev, "Original Order is Kept")

##import json
##
##dict1 = {"Earth":1, "Fire": 2, "Wind":3, "Ether":4, "Water": 5}
##print(json.dumps(dict1))

d1 = {"apple": "pie", "fudge": "brownies", "carrot": "cake", "milky": "way", "yum": "YUM"}
d2 = {"apple": "crumble", "vanilla": "brownies", "carrot": "cake", "milky": "way", "yum": "YUM"}

# what keys are in common
keys_com = d1.keys() & d2.keys()
print( "Keys in common: ", keys_com)

# what  items (keys and values) are in common
in_common = d1.items() & d2.items()
print("Items in common: ", in_common)

# what  keys are in d1 but NOT d2?
only_d1 = d1.keys() -  d2.keys()
print("keys in d1 only: ", only_d1)

# what  keys are in d2 but NOT d1?
only_d2 = d2.keys() -  d1.keys()
print("keys in d2 only: ",only_d2)

# what  keys are in d2 but NOT d1?
items_d2 = d2.items() -  d1.items()
print("pairs in  d2 only: ", items_d2)

# what  keys are unique to each set, but not in both
unique = d2.items() ^ d1.items()
print("Keys unique to each: ", unique)


