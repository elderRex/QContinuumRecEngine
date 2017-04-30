import csv
import collections
import glob, os
class utility:
    def __init__(self):
        self.util = True

    def collection_saver(self,__collection,parent_dir='./classified_cluster/'):
        names = __collection.keys()
        files = [str(x)+'_cluster.txt' for x in names]

        for k,f in zip(names,files):
            with open(parent_dir+f,'w+') as outfile:
                fieldnames = ['rid','rating','review']
                csvwriter = csv.DictWriter(outfile,fieldnames=fieldnames)
                csvwriter.writeheader()
                for j in __collection[k]:
                    #outfile.write(str(j)+'\n')
                    csvwriter.writerow({'rid':j[0],'rating':j[1],'review':j[2]})
            outfile.close()
        print 'done'

    def collection_loader(self,parent_dir='./classified_cluster/'):
        ans = collections.defaultdict(list)
        for file in os.listdir(parent_dir):
            with open(parent_dir+file,'r') as infile:
                #cnt,k = 0,0
                params = file.split('_')
                k = params[0]
                csvreader = csv.DictReader(infile)
                for row in csvreader:
                    #if cnt == 0:
                    #    k = str(row.strip())
                    #    cnt += 1
                    #    continue
                    #print row.strip()
                    ans[k].append([row['rid'],row['rating'],row['review']])
            infile.close()
        return ans