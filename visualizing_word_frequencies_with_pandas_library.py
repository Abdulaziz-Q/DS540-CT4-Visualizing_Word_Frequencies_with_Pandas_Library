# -*- coding: utf-8 -*-
"""Visualizing Word Frequencies with Pandas Library.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MR9orZNwFYJQGCKt1VXWAXqKxWLveebm

#  Visualizing Word Frequencies with Pandas Library

## Table of contents
* [Main code program ](#a)
* [Import and download necessary libraries](#b) 
* [Upload the file from local device into colab](#c)
* [Loading the data](#d)
* [Loading NLTK stop words](#e)
* [Getting the word frequencies](#f)
* [Eliminating the stop words](#g)
* [Sorting the words](#h)
* [Top 30 words ](#i)
* [Creating data frame with two columns](#j)
* [Plotting the 30 words](#k)

<a id='a'></a>
#### Main code program
"""

def main():
    print("Visualizing Word Frequencies with Pandas Library")
    print('\n')
    try:
        
        import traceback 
        import sys
        import nltk 
        from textblob import TextBlob
        from pathlib import Path
        from operator import itemgetter
        import pandas as pd
        from google.colab import files
        from nltk.corpus import stopwords
        nltk.download("stopwords")
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('brown')
        nltk.download('wordnet')
        
        #upload the PERSONAL_LIFE file then continue 
        upload_text = files.upload()
        #loading the data
        blob = TextBlob(Path('PERSONAL_LIFE.txt').read_text())
        #loading NLTK stop words
        stop_words = stopwords.words('english')
        #getting the word frequineces
        get_items = blob.word_counts.items()
        #eliminating the stop words
        eliminate_items = [item for item in get_items if item[0] not in stop_words]
        #sorting the words
        sorted_itmes = sorted(eliminate_items, key=itemgetter(1),reverse=True)
        #top 30 words
        top_words = sorted_itmes[0:30]
        #creating data frame with two columns
        word_df = pd.DataFrame(top_words, columns=['word','count'])
        print('\nWord frequencies of LeBron James personal life text file')
        #ploting the 30 words
        plot_words = word_df.plot.barh(x='word',y='count',legend=False,figsize=(15,7))

    except FileNotFoundError:
        exception_type, exception_value, exception_traceback = sys.int_info()
        print(f'Exception type: {exception_type} and value: {exception_value}')
        file_name, line_number, procedure_name, line_code = traceback.extract_tb(exception_traceback)[-1]
        print(f'File name: {file_name}, line number: {line_number}, procedure name: {procedure_name} and line code: {line_code}')

if __name__ == "__main__":
    main()



"""<a id='b'></a>
#### Import and download necessary libraries
"""

import nltk 
from textblob import TextBlob
from pathlib import Path
from operator import itemgetter
import pandas as pd
from google.colab import files
from nltk.corpus import stopwords
nltk.download("stopwords")
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
nltk.download('wordnet')

"""<a id='c'></a>
#### Upload the file from local device into colab
"""

#upload the PERSONAL_LIFE file then continue 
upload_text = files.upload()

"""<a id='d'></a>
#### Loading the data
"""

blob = TextBlob(Path('PERSONAL_LIFE.txt').read_text())

"""<a id='e'></a>
#### Loading NLTK stop words
"""

stop_words = stopwords.words('english')

"""<a id='f'></a>
#### Getting the word frequencies
"""

get_items = blob.word_counts.items()

"""<a id='g'></a>
#### Eliminating the stop words
"""

eliminate_items = [item for item in get_items if item[0] not in stop_words]

"""<a id='h'></a>
#### Sorting the words
"""

sorted_itmes = sorted(eliminate_items, key=itemgetter(1),reverse=True)

"""<a id='i'></a>
#### Top 30 words
"""

top_words = sorted_itmes[0:30]

"""<a id='j'></a>
#### Creating data frame with two columns
"""

word_df = pd.DataFrame(top_words, columns=['word','count'])

"""<a id='k'></a>
#### Plotting the 30 words
"""

plot_words = word_df.plot.barh(x='word',y='count',legend=False,figsize=(15,7))

