
rids = [7,10,11,12,13,15,21,22,24,25,36,37,38,39,40,46,47,48,49]

uids = ["king.kong@kg.com","luke.cage@lc.com","Mr.Spock@ms.com"]

for uid in uids:
    for rid in rids:
        print str(rid)+",'"+str(uid)+"',"
