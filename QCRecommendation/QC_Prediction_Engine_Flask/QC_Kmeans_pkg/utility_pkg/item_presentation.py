import csv

class util:

    def __init__(self):
        self.types = {}

    def load(self):
        with open('outtypes.txt','r+') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                self.types[row['type']] = int(row['id'])

    def parse_save(self,file):
        ans = {0:'PLACE_HOLDER'}
        outfile = 'out'+file
        cnt = 0
        with open(file,'r+') as typefile:
            for row in typefile:
                cnt += 1
                ans[cnt] = str(row.strip())
        with open(outfile,'w+') as printfile:
            fieldnames = ['id', 'type']
            csvwriter = csv.DictWriter(printfile,fieldnames=fieldnames)
            csvwriter.writeheader()
            for k in ans.keys():
                csvwriter.writerow({'id':k,'type':ans[k]})
        self.types = ans

