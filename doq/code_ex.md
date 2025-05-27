# Beispiele in Codes

## Abfrage der API 

```python
import pyquiz.api

api = pyquiz.api.OTDBApi()

api.get_questions(8)
```




## Fragenkatalog filtern

```python
df_fil = df.filter_by('Category').equals('History')
```