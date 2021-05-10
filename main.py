from expertai.nlapi.cloud.client import ExpertAiClient
import pandas as pd
import os

# Add login info
# os.environ["EAI_USERNAME"] = 'chang17liu@gmail.com'
# os.environ["EAI_PASSWORD"] = 'Chang001017!'
product_shown_1 = "Nike Women's Reax Run 5 Running Shoes"

df = pd.read_csv('data.csv')
df.drop_duplicates()
df = df[df['content'].notna()]

clean_df = df[['title', 'content', 'date', 'verified', 'rating', 'product']]
clean_df.head()
print(clean_df.head())
# client = ExpertAiClient()
# text = "Michael Jordan was one of the best basketball players of all time. Scoring was Jordan's stand-out skill, but he still holds a defensive NBA record, with eight steals in a half."
# language= 'en'

# Product 1
product1_df = clean_df[clean_df['product'] == product_shown_1]

def senti_score(text):
    """Gives the sentiment score of a given text"""
    return len(text)

product1_df = product1_df.assign(sentiment_score = product1_df["content"].apply(senti_score))
print(product1_df.head())

### 
# import matplotlib.pyplot as plt
# plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger

# Average sentiment for each product

# Sentiment histograms
product1_df['sentiment_score'].plot(kind='hist', title='sentiment_score')

# Sentiment vs. Date graph (Sentiment over time)
product1_df.plot(kind='scatter', x='date', y='sentiment_score', title='Sentiment change over time')

#

product1_df.to_csv("analyzed.csv", index=False)
# output = client.specific_resource_analysis(
#     body={"document": {"text": text}}, 
#     params={'language': language, 'resource': 'sentiment'}
#     )

# print("sentiment:", output.sentiment.overall)

# print (f'{"ENTITY":{50}} {"TYPE":{10}}')
# print (f'{"------":{50}} {"----":{10}}')

# for entity in output.entities:
#     print (f'{entity.lemma:{50}} {entity.type_:{10}}')
