# records
*For Assignment 12*

`records` pulls occurence data from GBIF for all species in a queired Genus for given decades

Required arguments:
`genusKey`: accepts GBIF genusKey *or* genus name as a string
`year`: returns data for all years in the decade following the indicated year (e.g. "2000" returns all records from years 2000-2010)

```python
import records

mydataset = records.Records(genusKey=147447113, year="1990,2000")
```

It is optional to supply `offset` and `limit` values to `get_single_batch()` function
default values: `offset=0`, `limit=20`
```python
mydataset.get_single_batch() #returns JSON summary for batch size

```

```python
mydataset.get_all_records() #retrieves all records and returns JSON and dataframe formats

#access returned data:
mydataset.json 
mydataset.df
```