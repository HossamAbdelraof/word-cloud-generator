"""
Word cloud generator 
it takes the word, count  in .CSV file 
it generate word cloud from the word in any language

"""


## auth libraries
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display


def main():
    ## read data file
    df = pd.read_csv("<file path>.csv")
    
    
    ## add and repeat the words in list 
    
    word_list = []
    for i in range(len(df)):
         for j in range(df.iloc[:, 1][i]):
            word_list.append(df.iloc[:, 0][i])
            
    ## join the text 
    text = " ".join(word_list)
    
    language = "ar"
    
    ## if the language is arabic then reshape the language else continus
    if language == "ar":
      text = reshape_arabic(text)
    
    
    ## Generate wordcloud   
    wordcloud = WordCloud(width = 1080, height = 1080,
                    background_color ='white',
                    stopwords = set(STOPWORDS),
                    font_path='<font_path>.ttf',
                    min_font_size = 8,
                    collocations=False).generate(text)
    
    wordcloud.to_file("<saving_path>.png")
    
    
    # plot the WordCloud image                      
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
     
    plt.show() 
    


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


if __name__ == '__main__':
    main()
