''' 
    We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet,
     the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment,
      in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file,
 which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), 
 Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, 
 and produce a graph of the Net Score vs Number of Retweets.

1 - To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation 
from everywhere in the word. (Hint: remember the .replace() method for strings.)

2 - Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, 
and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. 
The function should return a positive integer - how many occurrences there are of positive words in the text.
 Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well. 
'''


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    non_punct_chars = word
    
    for char in word:
        if char in punctuation_chars:
            non_punct_chars = non_punct_chars.replace(char, "")

    return non_punct_chars

def get_pos(sentenses):
    count = 0
    
    for word in sentenses.split():
        if strip_punctuation(word).lower() in positive_words:
            count += 1
    
    return count


def get_neg(sentenses):
    count = 0
    
    for word in sentenses.split():
        if strip_punctuation(word).lower() in negative_words:
            count += 1
    
    return count

twitter_data = []
with open("project_twitter_data.csv") as file:
    
    for line in file.readlines():
        twitter_data.append(line.strip())

with open("resulting_data.csv", "w") as file:
    file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    for tweet in twitter_data[1:]:
        pos_words = get_pos(tweet.split(",")[0])
        neg_words = get_neg(tweet.split(",")[0])
        retweets_count = tweet.split(",")[1]
        reply_count = tweet.split(",")[2]
        net_score = pos_words - neg_words
        file.write("{}, {}, {}, {}, {}\n".format(retweets_count, reply_count, pos_words, neg_words, net_score))
        #print("{}, {}, {}, {}, {}\n".format(retweets_count, reply_count, pos_words, neg_words, net_score))

my_sentence = twitter_data[10]
print(my_sentence)
print(my_sentence.split(",")[0])
print('pos', get_pos(my_sentence.split(",")[0]))
print('neg', get_neg(my_sentence.split(",")[0]))
print("net", get_pos(my_sentence.split(",")[0]) - get_neg(my_sentence.split(",")[0]))
