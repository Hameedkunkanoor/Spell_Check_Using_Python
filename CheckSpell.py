'''
python based spell checker to find misspelt words and give best matching suggestions
'''
import string
import argparse
import difflib
File = open('Spellchecker/WordsList.txt', 'r')
WordsList = []
for line in File:
 stripped_line = line. strip()
 WordsList. append(stripped_line)

File.close()
# print(WordsList)
if 'and' in WordsList:
 print("true")
# string=None
filename=None
autoreplace=False
def show_suggestions(autoreplace,words_to_search) :
    if(not autoreplace) :
     words_to_search=words_to_search.split(" ")
    for word in words_to_search:
     if word not in WordsList:
      suggestedwords=difflib.get_close_matches(word, WordsList)
      print("(Wrong word -> "+word+") (suggested Words->"+")")
      print(suggestedwords)
def ReplaceSuggestionsFile(filename):
    file = open(filename, 'r')
    pe = list(file.read().split())
    print(pe)
    # if(not autoreplace):
    r=[word.strip(string.punctuation) for word in pe]
    print(r)
    
    for word in pe:
     if word not in WordsList:
      suggestedwords=difflib.get_close_matches(word, WordsList)
      print("(Wrong word -> "+word+") (suggested Words->"+")")
      print(suggestedwords)

if __name__ == '__main__':
	
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-t", "--text", type=str, 
		# help="text to check for spell")
    # ap.add_argument("-f", "--filename", type=str, 
		# help="File to check for spell in")
    # ap.add_argument("-r", "--replace", type=bool, default=False,
		# help="Replace text with first matching word")
    # args = vars(ap.parse_args())
    # filename=args['filename']
    # string=args['text']
    # autoreplace=args['replace']
    filename='Spellchecker/Test.txt'
    autoreplace='fe'
    # string=args['text']
    # autoreplace=args['replace']
    if(filename is not None):
      ReplaceSuggestionsFile(filename)

print(string)

