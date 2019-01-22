#fun stuff with files
import re

lines = []
#p = re.compile(r'[\w+\s+\,\"\?\.+\-]+[^\d]\.', re.I)

p = re.compile(r'(.*?\.|.*?\?)\s+|\n', re.I)
#p = re.compile(r'(.*?\.\s+|.*?\?\s+|.*?\n)', re.I)
#p = re.compile(r'.*?((\.|\?)|\\n)', re.I)

            
with open("mytext.txt") as t:
    
    for line in t:
        find_it = p.findall(line)
        for match in find_it:
            lines.append(match)
        
count = 0           
for l in lines:
    print(count,  l)
    count += 1




##    for line in t:
##        lines.append(line)
##    for e in lines:
##        print(e)
        
