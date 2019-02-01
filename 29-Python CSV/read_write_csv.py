#read from one csv and write to another
import csv
from datetime import date

now = date.today()

def get_file():
    '''this creates the file name we will write to each day'''
    return "gaps_" + str(now) + ".csv"

name = get_file()
def create_file(name):
    with open(name, 'w') as create:
        fieldnames= ["GAP#", "ID", "LOB", "Category", "TargetDate", "Criticality", "% Complete"]
        writer = csv.DictWriter(create, fieldnames=fieldnames, lineterminator="\n") # keeps from skipping line
        writer.writeheader()

        with open('mydata/daily_file_2019-01-30.csv', "r") as daily:
            rows = csv.reader(daily)
            Line = 1
            for row in rows:
                new_line = str(now) + "-" + str(Line)
                if row[5] == "High":
                    writer.writerow({"GAP#": new_line, "ID": row[1], "LOB": row[2],"Category": row[3],
                                   "TargetDate": row[4], "Criticality": row[5], "% Complete": row[6]})
                    Line += 1
    print("*" * 50)                
    return "'" +str(name)+"'" + " has been succesfully created!   ON DATE: "  +  str(now)                 
                    
print(create_file(name) )

def get_avg(field_name):
    with open(name, "r") as output:
        rows = csv.DictReader(output)
        
        x = 0
        count = 0
        for row in rows:
            
            y = { key for key in row.items() if key == field_name}
            print(y)
            x = (x + int(row.__getitem__(field_name)))
            count = count +1
            
        return "The % Complete on High-Rated items is : " + str(x/ count) + "%"   
       
print(get_avg('% Complete'))

# get unique Item count from a given column
def get_unique(field_name):
    with open(name, "r") as output:
        rows = csv.DictReader(output)
        list_names = []
        count = 0
        for row in rows:
            if row[field_name] in list_names:
                continue
            else:
                list_names.append(row[field_name])
                count  += 1
        print("There are {} unique values in this field" .format(count))        
       
get_unique('LOB')
        
import csv

# count the number of times an item appears in a row
# also get % across total population for each
ref_count = {} # to export specific row
ref_orig = []  # talley # of rows

def group_me(field_num):
    with open('gaps_2019-01-31.csv', "r") as output:
        rows = csv.reader(output)
        next(rows, None)
        for row in rows:
            ref_orig.append(row)
            if not row[field_num] in ref_count:
                ref_count[row[field_num]] = 0 
                
            ref_count[row[field_num]]+=1   

group_me(2)  # caller - get specific row #2

#prints out results for selected row, gets counts and percentages 
print("-" * 60)
for k, v in ref_count.items():
    print("Item: {0:12} Count: {1} - {2}%" .format( k, v, round((v/len(ref_orig) * 100),1)))
print("-" * 60)
print("Total Population = ", len(ref_orig)) 
print("-" * 60)
   