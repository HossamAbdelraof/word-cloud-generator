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
then read the data as .CSV file contain 2 rows, [<the word>, <whe word count>]
  
```python
## read data file
df = pd.read_csv("C:\\Users\\20812018100700\\Desktop\\top_words.csv")
```
  
