
#Step1: importing nltk and csv

import nltk
import csv


#importing ngrams form nltk
from nltk import ngrams


#opening our csv file
with open('D:\csv\myfile.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    
    
#reading colums
    for colums in reader:
        sentenceOne = colums[0]
        sentenceTwo = colums[1]
        sentencThree = colums[2]
 
#defining a function to Generate our Grams....    
def generate_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams]


print("-Uni-Grams Of Our Sentences-")
print("1st Sentence:", generate_ngrams(sentenceOne, 1))
print("2nd Sentence: ", generate_ngrams(sentenceTwo, 1))
print("3rd Sentence:", generate_ngrams(sentencThree, 1),"\n")

print("--Bi-Grams Of Our Sentences--")
print("1st Sentence:", generate_ngrams(sentenceOne, 2))
print("2nd Sentence: ", generate_ngrams(sentenceTwo, 2))
print("3rd Sentence:", generate_ngrams(sentencThree, 2),"\n")

print("---Tri-Grams Of Our Sentences---")
print("1st Sentence:", generate_ngrams(sentenceOne, 3))
print("2nd Sentence: ", generate_ngrams(sentenceTwo, 3))
print("3rd Sentence:", generate_ngrams(sentencThree, 3),"\n")
