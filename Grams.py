documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_case_documents = []
for i in documents:
    lower_case_documents.append(i.lower())
print(lower_case_documents)

sans_punctuation_documents = []
import string

for i in lower_case_documents:
    sans_punctuation_documents.append(''.join(c for c in i if c not in string.punctuation))
    
print(sans_punctuation_documents)


preprocessed_documents = []
for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split(' '))
print(preprocessed_documents)


frequency_list = []
import pprint
from collections import Counter

for i in preprocessed_documents:
    frequency_list.append(Counter(i))
    
pprint.pprint(frequency_list)


import pandas as pd
documents = ['Hello, how are you!',
                'Win money, win from home.',
                'Call me now.',
                'Hello, Call hello you tomorrow?']


from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer(documents)


print(count_vector)


count_vector.fit(documents)
count_vector.get_feature_names()


doc_array = count_vector.transform(documents).toarray()
doc_array


frequency_matrix = pd.DataFrame(doc_array,index=documents,columns=count_vector.get_feature_names())
frequency_matrix