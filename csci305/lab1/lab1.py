import argparse
import re
from collections import defaultdict
import string
from operator import itemgetter



# Replace the string value of the following variable with your names.
ME = 'Melody Tribble';
COLLABORATORS = ['Courtney Linder', 'http://stackoverflow.com/', 'https://docs.python.org']

#This function processes a file of music data
#@param     infile = file to be processed, 
#           search_word = first word to search for, 
#           word_count = how many words in the "bigram" song title
#@return    a song title of most common bigram word, whose length is word_count
def process_file(infile, search_word, word_count):
    titles = set()
    #these are the regular expression patterns used to clean up the song data
    pattern = re.compile( r'[<][SEP]{3}[>]', re.M)
    pattern2 = re.compile('[(\["].*|[:]*D(feat.*)|[\.?&;!_]')

    # Loop through each line of the file
    for line in infile:
        #this splits the data into track id, song id, artist name, and song title
        my_list = re.split( pattern, line )
        #this pulls out the song title
        title = my_list[3]
        #this cleans up the song title and converts it to lower case
        clean_title = re.sub(pattern2, '', title ).lower()
        #this removes spaces and end line characters
        clean_title = clean_title.rstrip()
        #this adds each title to the titles set
        titles.add(clean_title)

    # loop over the cleaned titles and compute the bigram counts
    bigram_count = defaultdict(lambda: defaultdict(int))
    for title in titles:
        #splits title into a list of words
        title_list = re.split('\s', title)
        # loop over the words in the title and add each bigram to a dictionary while counting the occurances of each
        for index, word in enumerate(title_list):
            #check if there is a next word and assign to next
            try :
                next = title_list[index+1]
            # if there is not a next word break out of the loop
            except:
                break
            # add words to the dictionary and increment the occurance
            bigram_count[word][next] += 1
    # using bigram_count, recursivly find most common word following 'first_word' 'n' times
    def most_common_word(first_word, n):
        # recursive base case, when n = 0 return
        if (n< 1):
            return []
        # if 'first_word' is in the dictionary
        try:
            #set 'word' to be 'first_word's' dictionary of bigrams and number of occurances
            word = bigram_count.get(first_word) 
            #sorts 'word' dictionary by number of occurances       
            sorted_bigram_list =  sorted(word.items(), key = itemgetter(1), reverse=True)
            # sets 'next_word' to be the most common next word
            next_word = sorted_bigram_list[0][0]
            #return the 'first' word, call most_common_word with next word, decremented n
            n -= 1
            return [first_word] + most_common_word(next_word, n)
        # if first_word is not in the dictionary decrement n, return 'first' word, call function w/ a placeholder word
        except:
            n -= 1
            return [first_word] + most_common_word('_', n)
    #call recursive function with the first word and total number of words in desired title.         
    return most_common_word(search_word, word_count)


#fetches a file 
def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    return parser.parse_args().file_name


#this is the main function prints the assignment heading, asks for input, and returns a result
def main():
    # this prints the heading
    print '\nCSCI 305 Lab 1 submitted by %s' % ME
    print '  with help from %s\n\n' % ', '.join(COLLABORATORS)

    #this asks the user for a word and a number for the title length
    word = raw_input('Enter the first word in the bigram: \n')
    flag = True
    while(flag):
        try:
            number = input('Enter the number of words in your title: \n')
            flag = False
        except :
            print "Try again."

    #this opens a file and calls the 'process_file' function and prints the result
    file_name = get_file_name()
    with open(file_name, 'r') as infile:
        print ' '.join(process_file(infile, word, number))


if __name__ == '__main__':
    main()
