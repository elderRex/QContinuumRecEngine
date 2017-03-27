from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import os
import collections

class search_body:

    def __init__(self):
        self.params = {}
        self.result = []

    def setparams(self,lang,term=None,loc=None):
        self.params['lang'] = lang
        if term:
            self.params['term'] = term

class bus_holder:

    def __init__(self):
        self.holder = {}
        self.reviews = collections.defaultdict(list)

    def fill(self,content,name):
        self.holder[name] = content


print os.path.dirname(__file__)

sr = search_body()
rh = bus_holder()

with open(os.path.dirname(__file__)+'/confidential_config.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)
    sr.setparams('en','restaurants')
    res = client.search('New York',**sr.params)

    for bus in res.businesses:
        rh.fill(bus.id,bus.name)

    print rh.holder

    bus_sr = search_body()
    bus_sr.setparams('en')

    for k in rh.holder.keys():
        #print rh.holder[k]
        ans = client.get_business(rh.holder[k],**bus_sr.params)

        rh.reviews[k].append(ans.business.reviews[0].excerpt)

    for k in rh.reviews.keys():
        print k,'   ',rh.reviews[k][0]



