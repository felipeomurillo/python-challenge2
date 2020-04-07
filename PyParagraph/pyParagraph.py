# ---------------------------------------------------------------
# Name: pyParagraph.py
# Created by: Felipe Murillo
# Date Created: April 7, 2020
#
# Description: This script performs a lingusitic analysis on 
# an inputted excerpt
#
# Inputs: ../Resources/raw_data_paragraph_x.txt (where x = 1,2,3...)
# 
# Outputs: Paragragh analysis print to screen
# 
# ---------------------------------------------------------------

# Import modules to manipulate filesystems and use reguialr expression
import os
import re

# Prompt user to specify text file to analyze
input_file = input("Enter input txt file from ../Resources to be analyzed: ")

# Specify path to input data
txtpath = os.path.join("..","Resources",input_file)

# Open input data file
with open(txtpath) as txtfile:
    list = txtfile.readlines()
    # Break up excerpt into individual sentences. 
    # Split where termination punctuation [.!?] is found.
    sentences = re.split(r'(?<=[.!?]) +',list[0])

    # Initialize lists
    letter_cnt = []
    wrd_cnt = []
    mySpecialList = [ '-', '+', '#', '@', '!', '(', ')', '?', '.', ',', ':', ';', '"', "'", '`' ]

    for sentence in sentences:
        # Split each sentence into words
        words = re.split(r' ',sentence)
        # Count words in each sentence
        wrd_cnt.append(len(words))
        
        # Initialize letter count per sentence
        letter_no = 0

        # Count each letter in each sentence
        for i in range(0,len(words)):
            # Cycle thru each letter in each word
            for letters in words[i]:
                # Only count letters, not special characvters
                if letters not in mySpecialList:
                    letter_no += 1
        # Keep track of each sentence's letter count
        letter_cnt.append(letter_no)

# Print out paragragh analysis
print('Paragragh Analysis')
print('------------------')
print(f'Approximate Word Count: {sum(wrd_cnt[:])}')
print(f'Approximate Sentence Count: {len(sentences)}')
print(f'Average Letter Count (per word): {sum(letter_cnt[:])/sum(wrd_cnt[:]):.2}')
print(f'Average Sentence Length (in words): {sum(wrd_cnt[:])/len(sentences)}')