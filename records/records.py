#!/usr/bin/env python

"""
Class object that queries GBIF Occurence data for a genus and time period

"""
import requests
import pandas as pd

class Records:
    def __init__(self, year, genusKey):
        
        # store input params
        self.year = year
        self.genusKey = genusKey
        
        # will be used to store output results
        self.df = pd.DataFrame()
        self.json = {}
        
    def generate_genus_key(self):

        if type(self.genusKey) is int:
            self.genusKey = genusKey

        elif type(self.genusKey) is str:
            getgkey = requests.get(
                url="https://api.gbif.org/v1/species/search/", 
                params={
                "q": self.genusKey,
                "limit" : 1}
                )
            getgkey.json()
            gkeydf = pd.json_normalize(getgkey.json()["results"])
            self.genusKey = gkeydf["genusKey"][0]

        else:
            print("please enter a valid genus or genusKey")


    def get_single_batch(self, offset=0, limit=20):
        "returns JSON result for a small batch query"
        # ...
        self.offset = offset
        self.limit = limit
        
        batch = requests.get(
            url="https://api.gbif.org/v1/occurrence/search/",
            params={
                "key": self.genusKey,
                "year": self.year,
                "offset": self.offset,
                "limit": self.limit,
            }
        )
        return batch.json()
        
    def get_all_records(self):
        "stores result for all records to self.json and self.df"
        # ...
        res = requests.get(
            url="https://api.gbif.org/v1/occurrence/search/",
            params={
                "key": self.genusKey,
                "year": self.year,
            }
        )
        
        self.json = res.json()
        self.df = pd.json_normalize(self.json["results"])
        