#made by @tonyKingNZ at Jul 21, 2018 7:50 alone without help and seeing any code
#updated of other app


import json #get json native library

def word_meaning(word): #create a function to the word meaning and print
    data = json.load(open("data.json")) #get data from .json file
    word = word.lower() #implementig Case Sensitive
    if word in data: #check if word is in data
        print("\n",data[word],"\n\n") #print word meanig
    else: #if word not found write message
        print("\n\nWord not found! Check your word\n\n")#message that word is not found

word = input("\nWrite some word to see the meanig:\n\n") #get the word that want the word meaning
word_meaning(word) #get word meanig


#made by @tonyKingNZ at Jul 21, 2018 7:50 alone without help and seeing any code
#update of other app
