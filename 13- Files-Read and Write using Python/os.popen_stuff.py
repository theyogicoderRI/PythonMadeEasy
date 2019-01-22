import os
output = os.system('systeminfo')


for line in os.popen('systeminfo'):
    print(line.rstrip())
