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
then read the data as .CSV file contain 2 rows, [\<the word\>, \<the word count\>]
  
```python
## read data file
df = pd.read_csv("<file path>.csv")
```
you can get the data from any source but in the specific format
recommended for the data to be from pandas DataFrame 
you can select the data from pandas DataFrame after filtering and save it to .csv file as in the code 

```python
## save the file
df.<col_name>.value_counts().to_csv(<file path>.csv, index = True)
```

after reading the data will add every word in a list by the number of it's repeating and join it as text 

```python
## add and repeat the words in list 

word_list = []
for i in range(len(df)):
     for j in range(df.iloc[:, 1][i]):
        word_list.append(df.iloc[:, 0][i])
        
## join the text 
text = " ".join(word_list)
```

if the text include arabic words it wont display correctly then you should use "reshape_arabic()" function
it reshapr all arabic words ther replace the single words th prevent any problems

```python
def reshape_arabic(text_file):
    te = arabic_reshaper.reshape(text_file)
    te = get_display(te)
    
    word_replace = {"ﺀ":"ء", "ﺍ":"ا", "ﺏ":"ب", "ﺕ":"ت", "ﺓ":"ة", "ﺙ":"ث", "ﺝ":"ج",
                    "ﺡ":"ح", "خ":"ﺥ", "ﺩ":"د", "ﺫ":"ذ", "ﺭ":"ر", "ﺯ":"ز", "ﺱ":"س", 
                    "ﺵ":"ش", "ﺹ":"ص", "ﺽ":"ض", "ﻁ":"ط", "ﻅ":"ظ", "ﻉ":"ع", "ﻍ":"غ",
                    "ﻑ":"ف", "ﻕ":"ق", "ﻙ":"ك", "ﻝ":"ل", "ﻡ":"م", "ﻥ":"ن", "ﻩ":"ه",
                    "ﻭ":"و", "ﻱ":"ى", "ﻯ":"ي" ,}                      
    
    for i in word_replace.keys():
        te = te.replace(i, word_replace[i])
        
    return te
```


  
