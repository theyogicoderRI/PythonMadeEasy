from collections import *

##s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
##d = defaultdict(list)
##for k, v in s:
##    d[k].append(v)
##
##print(type(d))
##print(d.items())
##print(type(d.items()))


##from collections import *
##kwargs = {"one":1, 'ten': 10, 'twenty-five': 25, 'one-hundred':100}
##my_d_int = defaultdict(int, **kwargs)
##print(my_d_int)
##
##print("WE CAN TREAT IT LIKE A REGULAR DICT FROM SEE?")
##for k, v in my_d_int.items():
##    print(v*2)

    
##from collections import *

##l1 = [('a', 1), ('b', 2), ('a', 3), ('a', 4), ('b', 77), ('d', 56)]
##print("l1 is of type: ", type(l1))
##dd = defaultdict(list)
##print("dd is of type: ", type(dd))
##for k,v, in l1:
##    dd[k].append(v)
##
##print(dd)

from collections import *

# Time complexity O(n^2)
##def delete_nth_naive(array, n):
##    ans = []
##    for num in array:
##        if ans.count(num) < n:
##            ans.append(num)
##    return ans

### when int is use as a default_factory it always returns 0 by default
##def default_val1(list1,n): 
##    result = []
##    counts = defaultdict(int) 
##
##    for i in list1:   # second time we go through i is 2
##        if counts[i] < n:  # here is calls counts witha key of i which is 1, counts doesn't have it
##            # so it adds to with a defalut value of 0
##            # second time the key for counts is 2, but the value is 0 still less than 2,   it does not have a key of 2 so it adds it with a default value of 0
##            #print("prints count after if: ", counts)
##            # value fr count[i] is always 0 here
##            result.append(i) 
##            counts[i] += 5  # now for counts[i], the key which is still 1, it takes its value which is zero and adds 1, so it is now 1
##            # the value is zero for key 2, so it adds one to the value and and it is now 1
##            #print("counts in loop after update: ", counts)
##    print(counts)        
##    return result
##
##x = [1,2,3,4,5,6,7,8,9, 10,11,12,13,14,15]
##print(default_val(x, n=2))



# when int is used as a default_factory it always returns 0 by default
def default_val(list1,n): 
    result = []
    counts = defaultdict(int) 

    for i in list1:  
        if counts[i] < n:  
            result.append(i) 
            counts[i] += 5          
    print(counts)        
    return result

x = [1,2,3]
# caller
print(default_val(x, 2))

