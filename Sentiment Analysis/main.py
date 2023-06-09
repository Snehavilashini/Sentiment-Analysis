import string
from collections import Counter
import matplotlib.pyplot as plt

# Reading text file
text = open('read.txt', encoding='utf-8').read()

# Converting into lowercase
lower_case = text.lower()

# Removing punctuations
processed_text = lower_case.translate(str.maketrans('', '', string.punctuation))
print(processed_text)

# Splitting text into words
tokenizedWordsList = processed_text.split()
print(tokenizedWordsList)

exclusion_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# creating an empty list
modifiedWords = []

# loop through the tokenizedwords
for word in tokenizedWordsList:
    if word not in exclusion_list:
        modifiedWords.append(word)

# NLP Emotion Algorithm

emotionalStates = []

# Open the emotion.txt file
# loop through the file and clear
# If word is present add emotion into emotion_list


with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in modifiedWords:
            emotionalStates.append(emotion)

print(emotionalStates)

# Finally count each emotion in the emotion list
w = Counter(emotionalStates)
print(w)

# This is to plot the graph keys in a slanting.
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
ax1.set_title("Sentiment Bar Graph")
plt.savefig('bargraph.png')
plt.show()

# This code is to plot the graph keys in straight line
# plt.bar(w.keys(), w.values())
# plt.savefig('graph.png')
# plt.show()