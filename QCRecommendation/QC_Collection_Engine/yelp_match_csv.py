import csv
import collections
import json

search_ids= collections.defaultdict(list)

whole = {}

with open('train.json') as targets:
    data = json.load(targets)
    for fields in data:
        whole[fields['business_id']] = fields['name']
targets.close()

with open('test.json') as targets:
    data = json.load(targets)
    for fields in data:
        whole[fields['business_id']] = fields['name']
targets.close()

with open('yelp_academic_dataset_review.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    cnt = 0
    for row in csvreader:
        if row['business_id'] in whole:
            if len(search_ids[row['business_id']]) < 5:
                search_ids[row['business_id']].append((row['user_id'],row['stars'],row['text'],row['date']))
                cnt += 1
    print 'found',+cnt
csvfile.close()

with open('users.csv','w+') as outfile:
    fieldnames = ["id","firstname","lastname","email","password"]
    csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    user = set()
    for k in search_ids.keys():
        for item in search_ids[k]:
            user.add(item[0])
    for u in user:
        tmp = {"firstname":'a',"lastname":'b',"email":"a@b","password":"asdf"}
        tmp["id"] = u
        csvwriter.writerow(tmp)
outfile.close()

with open('bus.csv','w+') as outfile:
    fieldnames = ["id", "name", "type", "description", "website"]
    csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    for k in whole.keys():
        tmp = {}
        tmp["id"] = k
        tmp["name"] = whole[k]
        tmp["type"] = "restaurant"
        tmp["description"] = "dummy"
        tmp["website"] = "qc.com"
        csvwriter.writerow(tmp)
outfile.close()

with open('result.csv','w+') as outfile:
    fieldnames = ["id","uid","rating","review_text","iid","datetime"]
    csvwriter = csv.DictWriter(outfile,fieldnames=fieldnames)
    csvwriter.writeheader()
    cnt = 0
    for k in search_ids.keys():
        for item in search_ids[k]:
            tmp = {}
            cnt += 1
            tmp['id'] = cnt
            tmp['uid'] = item[0]
            tmp['rating'] = item[1]
            tmp['review_text'] = item[2]
            tmp['iid'] = k
            tmp['datetime'] = item[3]
            csvwriter.writerow(tmp)
outfile.close()