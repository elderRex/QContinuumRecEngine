import csv
import os

rids = [7,10,11,12,13,15,21,22,24,25,36,37,38,39,40,46,47,48,49]

uids = ["king.kong@kg.com","luke.cage@lc.com","Mr.Spock@ms.com"]

mydict = {}

upath = os.path.dirname(__file__)
print upath

with open(upath+"/sample_data/user_match.csv",'r+') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        mydict[row['email'][1:]] = row['id']

print mydict

with open(upath+"/sample_data/result.csv",'r+') as csvfile:
    with open(upath+"/sample_data/real_result.csv",'w+') as outfile:
        csvreader = csv.DictReader(csvfile)
        fieldnames = ["id", "uid", "rating", "review_text", "iid", "datetime"]
        csvwriter = csv.DictWriter(outfile,fieldnames=fieldnames)
        csvwriter.writeheader()
        for row in csvreader:
            print row['uid']
            row['uid'] = mydict[row['uid']]
            csvwriter.writerow(row)