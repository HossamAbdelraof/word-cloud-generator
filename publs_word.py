"""
Word cloud generator 
it takes the word, count  in .CSV file 
it generate word cloud from the word in any language

"""


## auth libraries
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

import arabic_reshaper
from bidi.algorithm import get_display

## read data file
df = pd.read_csv("C:\\Users\\20812018100700\\Desktop\\top_words.csv")


## add and repeat the words in list 
lis = []
for i in range(len(df)):
     for j in range(df.iloc[:, 1][i]):
        lis.append(df.iloc[:, 0][i])
        
## select language and join text 
language = "ar"
text = " ".join(lis)

## if the language is arabic then reshape the language else continus
if language == "ar":
    te = arabic_reshaper.reshape(text)
    te = get_display(te)
    
    word_replace = {"ﺀ":"ء","ﺍ":"ا", "ﺏ":"ب","ﺕ":"ت", "ﺓ":"ة","ﺙ":"ث","ﺝ":"ج",
                    "ﺡ":"ح","خ":"ﺥ","ﺩ":"د","ﺫ":"ذ","ﺭ":"ر","ﺯ":"ز", "ﺱ":"س",                       
                    "ﺵ":"ش", "ﺹ":"ص", "ﺽ":"ض", "ﻁ":"ط", "ﻅ":"ظ", "ﻉ":"ع",                       
                    "ﻍ":"غ", "ﻑ":"ف", "ﻕ":"ق", "ﻙ":"ك", "ﻝ":"ل", "ﻡ":"م",                       
                    "ﻥ":"ن", "ﻩ":"ه", "ﻭ":"و", "ﻱ":"ى", "ﻯ":"ي",}                      
    for i in word_replace.keys():
        te = te.replace(i, word_replace[i])
else:
    te = text

   
wordcloud = WordCloud(width = 1080, height = 1080,
                background_color ='white',
                stopwords = set(STOPWORDS),
                font_path='C:\\Users\\20812018100700\\Desktop\\Tajawal-Regular.ttf',
                min_font_size = 8,
                collocations=False).generate(te)
wordcloud.to_file("C:\\Users\\20812018100700\\Desktop\\arabic_example.png")

# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show() 
