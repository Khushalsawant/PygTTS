#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime
from PyDictionary import PyDictionary
from nltk.corpus import wordnet

now_UTC_hr = datetime.utcnow().hour # Get the UTC time
print('The UTC Time is ', datetime.utcnow())
dictionary=PyDictionary()
language = 'en'

path_of_file = 'C:/Users/khushal/Pictures/temp.txt'
file = open(path_of_file,'w')

def gratitude_wish(word,language):
    print(word)
    myobj = gTTS(text=word, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named
    path_of_file_tst = 'C:/Users/khushal/Documents/Python Scripts/gratiude.mp3'
    # Saving the converted audio in a mp3 file named
    myobj.save(path_of_file_tst)
    # Playing the converted file
    if os.path.exists(path_of_file_tst):
        playsound(path_of_file_tst)
        os.remove(path_of_file_tst)
    else:
        print("The file does not exist")

def gratiude_language(language):
    if now_UTC_hr >= 4 and now_UTC_hr < 12:
        print("It's time to say, Good Morning")
        gratiude = 'Good Morning'
        gratitude_wish(gratiude, language)
    elif now_UTC_hr >= 12 and now_UTC_hr < 17:
        print("It's time to say, Good Afternoon")
        gratiude = 'Good Afternoon'
        gratitude_wish(gratiude, language)
    elif now_UTC_hr >= 17 and now_UTC_hr <= 21:
        print("It's time to say, Good Evening")
        gratiude = 'Good Evening'
        gratitude_wish(gratiude, language)
    elif now_UTC_hr > 21:
        print("It's time to sleep, Good Night")
        gratiude = 'Good Night'
        gratitude_wish(gratiude, language)

gratiude_language(language)

synonyms = []
antonyms = []

#keyword_for_synonyms_antonyms = input("Enter the keyword for in which you want synonyms & antonyms = \n")
keyword_for_synonyms_antonyms = "bring"

def word_for_synonyms_antonyms(keyword_for_synonyms_antonyms):
    print('keyword_for_synonyms_antonyms := ', keyword_for_synonyms_antonyms)
    #to get synonyms and antonyms
    for syn in wordnet.synsets(keyword_for_synonyms_antonyms):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    #print(set(synonyms))
    synonyms_words =set(synonyms)
    synonyms_words_dict = dict()
    pos_l1 = set()
    for words in synonyms_words:
        for tmp in wordnet.synsets(words):
            if tmp.name().split('.')[0] == words:
                pos_l1.add(tmp.pos())
        synonyms_words_dict[words] = pos_l1
    #print(set(antonyms))
    antonyms_words =set(antonyms)
    antonyms_words_dict = dict()
    pos_l2 = set()
    for words in antonyms_words:
        for tmp in wordnet.synsets(words):
            if tmp.name().split('.')[0] == words:
                pos_l2.add(tmp.pos())
        antonyms_words_dict[words] = pos_l2

    return synonyms_words_dict,antonyms_words_dict

w = keyword_for_synonyms_antonyms
pos_all = dict()
pos_l = set()
for tmp in wordnet.synsets(w):
    if tmp.name().split('.')[0] == w:
        pos_l.add(tmp.pos())
pos_all[w] = pos_l

output_synonyms_words,output_antonyms_words = word_for_synonyms_antonyms(keyword_for_synonyms_antonyms)
print('output_synonyms_words = ',output_synonyms_words,'\noutput_antonyms_words = ', output_antonyms_words)

# using Pydictionary module
def word_with_meaning(word):
    meaning_of_word = dictionary.meaning(keyword_for_synonyms_antonyms)
    print(meaning_of_word.keys())
    meaning_of_word_google = dictionary.googlemeaning(keyword_for_synonyms_antonyms)
    print(meaning_of_word_google)
    for key in list(meaning_of_word.keys()):
        if key == 'Noun':
            meaning_of_word_Noun = meaning_of_word['Noun']
            return meaning_of_word_Noun, meaning_of_word_google
            break
            # print("Noun Meaning", meaning_of_word_Noun)
        elif key == 'Verb':
            meaning_of_word_Verb = meaning_of_word['Verb']
            return meaning_of_word_Verb, meaning_of_word_google
            break
            # print("Verb meaning", meaning_of_word_Verb)

meaning_of_word_Output,meaning_of_word_From_google = word_with_meaning(keyword_for_synonyms_antonyms)

def audible_meaning_of_word(value,word):
    if value.upper() == 'Y':
        print('-'*60)
        print('Listen it carefully !!')
        i =0
        for values in word:
            print(values)
            myobj = gTTS(text=values, lang=language, slow=False)
            i +=1
            # Saving the converted audio in a mp3 file named
            path_of_file_tst = 'C:/Users/khushal/Documents/Python Scripts/word_meaning' + str(i) + '.mp3'
            # Saving the converted audio in a mp3 file named
            myobj.save(path_of_file_tst)
            # Playing the converted file
            if os.path.exists(path_of_file_tst):
                playsound(path_of_file_tst)
                os.remove(path_of_file_tst)
            else:
                print("The file does not exist")

    elif value.upper() == 'N':
        print('-'*60)
        print('Displaying the result !!')
        for values in word:
            print(values)
        pass
    else:
        print("You've entered the incorrect value")
word_meaning = list(meaning_of_word_Output)
switch = 'y'
audible_meaning_of_word(switch,word_meaning)
switch = 'n'
audible_meaning_of_word(switch,word_meaning)
file.close()