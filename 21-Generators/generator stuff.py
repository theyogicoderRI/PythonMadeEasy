#too generators

##ctype = ['hot', 'cold']
##flavor = ['plain', 'vanilla', 'hazelnut']
##size = ['sm', 'md', 'lg', 'xlg']
##
##for drink in ((c, f, s) for c in ctype for f in flavor for s in size):
##    print(drink)


#groupby
##
##tools = ['hammer', 'saw', 'drill', 'screwdriver', 'tape measure',
##         'excavator', 'nails', 'clamps', 'wrenches', 'knives', 'hand planes',
##         'cutters', 'crimpers', 'glue', 'wood', 'rotary', 'routers',
##         'sanders', 'compressors', 'grinders', 'planers']
##
##tools.sort(key=len, reverse=True) # sorts elements in list  in reverse order
##import itertools
##
##for l, g in itertools.groupby(tools, len):
##    print('Length: {} -- Tools:  {}'.format(l, list(g)))

##
##def jumble(s):
##    for item in range(len(s)):
##        yield s[item:] + s[:item]
##
##res = list(jumble('python'))
##print(res)

word = "weekend"
jumble2 =  (word[item:] + word[:item] for item in range(len(word)))
print(list(jumble2))

    
