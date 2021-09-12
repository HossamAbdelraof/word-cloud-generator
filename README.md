# word-cloud-generator
generate word cloud from Repeated words

the code start with importing necessary libraries 

```python
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
```
then read the data as .CSV file contain 2 rows, [\<the word\>, \<whe word count\>]
  
```python
## read data file
df = pd.read_csv("<file path>.csv")
```
you can get the data from any source but in the specific format
recommended for the data to be from pandas DataFrame 
you can select the data from pandas DataFrame after filtering and save it to .csv file as in the code 

```python
## save the file
df.<row_name>.value_counts().to_csv(<file path>.csv, index = True)
```





  
