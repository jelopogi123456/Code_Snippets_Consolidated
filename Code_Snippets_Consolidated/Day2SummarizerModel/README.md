## Pre-Trained Summarizer Model (BART) 
In this notebook, we use the Facebook BART model to summarize a set of articles from the 3 news website. The goal is to see how well the model performs in summarizing the articles.

## Libraries Used
- transformers
- pandas
- numpy

## Dataset

I used a dataset containing validated articles from the 3 news website that I scraped. The dataset includes information such as the title, author, publication date, content, summarized_article , source.

## BART Model
I used the Facebook BART model for summarization, which is pre-trained on large amounts of text data. We used the summarization pipeline from the transformers library to easily summarize each article.

## Results
The summarized texts were compared to the original articles, and the word count of each was recorded. 

The summarized texts were generally accurate and contained the key points of the original articles. However, in some cases, the summarized texts were missing some details or nuances present in the original articles.

## Conclusion
The Facebook BART model shows promise in summarizing articles. However, more testing is needed to determine the limitations of the model and its effectiveness on various types of text data. I tried to use the Rest Api and test it for the back-end, and I saved the scraped datas and scraped articles in the PostgreSQL.
