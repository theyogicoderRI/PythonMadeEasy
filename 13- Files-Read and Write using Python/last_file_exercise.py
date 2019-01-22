import re

lines = []
p = re.compile(r'(.*?[\.|\?])\s{2,}')

with open("mtn.txt") as t:
    for line in t:
        find_it = p.findall(line)
        for match in find_it:
            lines.append(match)      
count = 0           
for l in lines:
    print(str(count)+ ":" , l)
    count += 1
print()
print("Total number of lines is:",count)
