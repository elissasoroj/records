#!/usr/bin/env python

"""
Class object that queries GBIF Occurence data for a genus and time period

"""
import requests
import pandas as pd

class Records:
    def __init__(self, genusKey, year):
        
        # store input params
        self.genusKey = genusKey
        self.year = year
        
        # will be used to store output results
        self.df = pd.DataFrame()
        self.json = {}
        
    def get_single_batch(self, offset=0, limit=20):
        "returns JSON result for a small batch query"
        # ...
        self.offset = offset
        self.limit = limit
        
        batch = requests.get(
            url="https://api.gbif.org/v1/occurrence/search/",
            params={
                "genusKey": self.genusKey,
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
                "genusKey": self.genusKey,
                "year": self.year,
            }
        )
        
        self.json = res.json()
        self.df = pd.json_normalize(self.json["results"])
        