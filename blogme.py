import pandas as pd
from vaberSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel or xlsx files
data = pd.read_excel('articles.xlsx') 

#summary of the data
data.describe()

#summary of the columns
data.info()

#counting the number of articles per source
#format of groupby: df.groupby(['colname_to_group'])['colname_to_count'].count
data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping column
data = data.drop('engagement_comment_plugin_count' , axis=1)

#functions in python
#define the function
def thisFunction():
    print('This is my First Function!')
#call the function
thisFunction()

#this is a function with variables
def aboutMe(name):
    print('My name is ' + name)
    return name

name = 'Kim'
aboutMe(name)

#using for loops in functions
def favfood(food):
    for x in food: 
        print('top food is ' + x)


fastfood = ['burgers', 'pizza', 'pie']

favfood(fastfood)

#sentiment analysis!
# #creating a keyword flag
# keyword = 'crash'
# length = len(data)
# keyword_flag = [] #if you want to create a new column you need to declare it
# #lets create a for loop to isolate each title row
# for x in range(0,length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)

#creating a function
def keywordflag(keyword): #the word of choice is the word that the user inputs into the function
    length = len(data)
    keyword_flag = [] 
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keywordflag

k = keywordflag('support')

#creating a new column in data dataframe
data['keyword_flag'] = pd.Series(keywordflag)

#sentiment analysis = guage attitude of speaker

#SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()
text = data['title'][15]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding a for loop to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#writing the data
data.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index = False)