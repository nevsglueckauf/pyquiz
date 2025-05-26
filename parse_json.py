import json
import pandas as pd

dta = json.load(open('data/new.json'))['results']
dta_2 = json.load(open('data/newFromApiClient.json'))['results']
print(len(dta), len(dta_2))

exit()
df = pd.DataFrame(dta)

df2 = pd.DataFrame(dta_2)
# see: https://www.geeksforgeeks.org/pandas-concat-function-in-python/
# DO NOT merge, append is deprectaed since a long time, so we use <kbd>concat</kbd>
full = pd.concat([df, df2])

#print(df.head())

print(full.head(), len(full))