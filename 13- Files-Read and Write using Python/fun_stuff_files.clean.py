#fun stuff with files
import re

lines = []
#p = re.compile(r'(.*?\.|.*?\?)\s+', re.I)

#p = re.compile(r'(\w+\s+\.\s+[\w]{2,}\.)\s+', re.I)
#p = re.compile(r'.*?\.(\s+|.{2,})', re.I)
#p = re.compile(r'(.*?H\.\s+.*?\.|.*?\.|.*?\?)\s+', re.I)
#p = re.compile(r'(.*?(\w\w\.|\?)\s+)', re.I)
#p = re.compile(r'(.*?H\.\s+.*?\.|.*?\.|.*?\? )\s+.', re.I)
#p = re.compile(r'.*?[\.|\?]\s| .*?H\.\s.*?\.', re.I)
#should get just last line
#p = re.compile(r'(.*?\s+[A-Z]\..*?\.)')
#trying to combine with other lines
#p = re.compile(r'.*?[\.|\?]\s|.*?\s+[A-Z]\..*?\.')
#p = re.compile(r'.*?\s[A-Z]\..*?\.|.*?[\.|\?]\s')
#p = re.compile(r'\..*?[A-Z]\..*?\.|.*?[\.|\?]\s')
#p = re.compile(r'[A-Z]\..*?\.(?<!\w\s\.)|.*?[\.|\?]\s+')
#p = re.compile(r'(?<!\w\s\.)|.*?[\.|\?]\s+')
#p = re.compile(r'(?<=[\.|\?|\r\b\s+]\s)\w+\s+[A-Z]\..*?\.')
#p =re.compile(r'(\.\s)(.*?[A-Z]\..*?\.)')
#JENS that works - negative lookback assertion
#p = re.compile(r'(.*?[\.|\?])\s(?<!\s\w\.\s)')
# a negative lookbehind assertion will find what is outside of the "lookbehind") as
# long as it is not preceeeded by what is in the look back
#p = re.compile(r'(?<!\.\s[A-Z]\.)(.*?[\.|\?]\s)')
p = re.compile(r'(.*?[\.|\?])\s+')


with open("mytext.txt") as t:
    for line in t:
        find_it = p.findall(line)
        for match in find_it:
            lines.append(match)      
count = 0           
for l in lines:
    print(count, l)
    count += 1

##with open("mytext.txt") as t:
##for line in t:
##    find_it = p.findall(line)
##    for match in find_it:
##        print(match)     


# this works for the last sentence
#p2 = re.compile(r'\.\s+.*?\s[H]\.\s\w*\.')

#p1 = re.compile(r'(.*?[\.|\?]\s)|\.\s+.*?\s[A-Z]\.\s\w*')
#p1 = re.compile(r'\.\s+.*?\s[A-Z]\.\s\w*|(.*?[\.|\?]\s)')

#s1 = "This is what time it is. Is this the time? Hi H. Masters."
#should get just last line
##p = re.compile(r'(?<=[\.|\?]\s)\w+\s+[A-Z]\..*?\.')
