# Dependencies
import os 
import re
import string 
import pdb 

# Declerations
word_count=0
total_letter_count=0
avg_letter_count=0
total_letter_count=0
sentence_lenght=0
list_of_words=[]
list_of_letters=[]

print('---------------------------------------')
print('Paragraph Analysis')
print('---------------------------------------')

#creating the txt file path 
path = os.path.join('paragraph_2.txt')

#reading the csv using csv module and creating a file object
with open (path,'r',encoding='utf-8') as txt_file:
    
    #approximate word count - convert txt file object to create list of words using space as delimiter
    txt_read = txt_file.read()
    list_of_words = txt_read.split(' ')
    word_count = len(list_of_words)
    print(f'Approximate word count: {word_count}')
    #print(list_of_words)
    
    #approximate sentence count

    #make a list of delimiters(punctuation) that can be used at the end of sentences -  !?.\n
    punctuation = ('.','?','!','\n')

    #re.escape of regex module builds a pattern with the punctuation escaped
    regulartext_pattern = '|'.join(map(re.escape, punctuation)) 

    #Convert read text to a list of sentences
    txt_read = re.split(regulartext_pattern,txt_read)
    #print(txt_read)

    #subtract 1 for the extra space that is included in the end of the list
    sentence_count = len(txt_read) - 1 
    print(f'Approximate sentence count: {sentence_count}')
    
    # average letter count per word
    # using re.sub from regex module to create a list of words minus the punctuation marks. 
    # It replaces the punctuation marks with spaces and trims the spaces
    for words in list_of_words:    
        a = re.sub(r'[^a-zA-Z0-9\s]','', words)
        list_of_letters.append(a)
    
    #use a conditional to omit cases where only punctuation marks(now empty strings) were part of the list
    for words in list_of_letters:
        if words != '':
            total_letter_count += len(words)
            #print(str(total_letter_count))
    
    #print(list_of_letters)
    avg_letter_count = total_letter_count/word_count
    print(f'Approximate letter count:{round(avg_letter_count,4)}')

    #Average sentence length in words
    sentence_length = word_count/sentence_count
    print(f'Average Sentence Length: {round(sentence_length,4)}')