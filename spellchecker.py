import time
import re
import os.path
from difflib import SequenceMatcher
from datetime import datetime
import time

repeat = True

while(repeat == True):

#Initialising variables for statistics and the "var"s for the loops

    t0 = time.time()
    numofwords = 0
    numofcorrectwords = 0
    numofincorrectwords = 0
    numofwordstodict = 0
    numofwordschanged = 0
    var = True
    var1 = True
    var2 = True
    var3 = True
    var4 = True

    print("Hello!")
    time.sleep(1)
    print("Welcome to Spellchecker!")
    time.sleep(1)
    outputfile = input("All informarion will be put in a separate file. Please enter a name for that file: ")
    outputfileopen = open(outputfile, "a")
    while (var == True):
        spelldecision = int ( input ("What would you like to spell check? \n1. A sentence \n2. A file \nOr press 0 in order to quit.\n"))
#Enter the first branch which consists of reading from an input sentence
        if (spelldecision == 1):
            sentence = input ("Please enter your sentence: ")
            sentence2=re.sub('[^a-zA-Z\s]','',sentence)
            words = sentence2.lower().split()
            eng = open("EnglishWords.txt", "r")
            engwords = eng.read()
            eng.close()
            engwordslist = engwords.split()
            i=0
            j=0
#Going through all words in the string
            while (i < len(words)):
#Checking for them in the english words
                if words[i] in engwords:
                    print (words[i])
                    outputfileopen.write(words[i]+"\n")
                    i += 1
                    numofwords += 1
                    numofcorrectwords += 1
#Things to do if the word is not in the english words
                else:

                    print("The word " + str(words[i]) + " is spelled incorrectly")
                    var1 = True
                    decision = int ( input ("Press 1 to ignore the mistake. \nPress 2 to mark the word. \nPress 3 to add the word to the dictionary. \nPress 4 to be shown a likely correct spelling.\n" ))
#Decide what to do
                    while (var1 == True):
                        if (decision == 1):
                            print ("You decided to ignore the incorrectly spelled word.")
                            outputfileopen.write(words[i]+"\n")
                            var1 = False
                            numofwords += 1
                            numofincorrectwords += 1
                            i += 1
                        elif (decision == 2):
                            print ("You decided to mark the word.")
                            var1 = False
                            marked="?" + words[i] + "?"
                            print(marked)
                            outputfileopen.write(marked+"\n")
                            numofwords += 1
                            numofincorrectwords += 1
                            i += 1
                        elif (decision == 3):
                            print ("You decided to add the word to the dictionary.")
                            engwordsopen = open("EnglishWords.txt", "a")
                            engwordsopen.write(words[i]+"\n")
                            outputfileopen.write(words[i]+"\n")
                            var1 = False
                            numofwords += 1
                            numofcorrectwords += 1
                            numofwordstodict +=1
                            i += 1
                            engwordsopen.close()
                        elif (decision == 4):
#Find a likely word in the english words list
                            while (var3 == True):
                                prediction = SequenceMatcher(None, words[i], engwordslist[j]).ratio()
                                predictionpercent = prediction * 100
#Getting a likely word as a suggested spelling
                                if (predictionpercent > 70):
                                    feedback = int ( input ("You required a likely correct spelling.\nThe suggested spelling is: " + str(engwordslist[j]) + "\nWould you like to keep it?\nPlease enter 1 to keep the suggested spelling. \nPlease enter 0 if you do not want to keep the suggested spelling.\n") )
                                    if (feedback == 1):
                                        words[i] = engwordslist[j]
                                        print (words[i])
                                        outputfileopen.write(words[i]+"\n")
                                        numofwords += 1
                                        numofcorrectwords += 1
                                        numofwordschanged += 1
                                        i += 1
                                        var1 = False
                                    elif (feedback == 0):
                                        print (words[i])
                                        outputfileopen.write(words[i]+"\n")
                                        numofwords += 1
                                        numofincorrectwords += 1
                                        numofwordschanged += 1
                                        i += 1
                                        var1 = False
                                    var3 = False
                                else:
                                    j += 1
                        else:
                            print ("You have to choose between the choices 1, 2, 3 and 4.\nPlease select again.\n")
                            time.sleep(1)
            var = False
#Enter the second branch which consists of reading from a file
        elif (spelldecision == 2):
            while (var2 == True):
                filename = input("Enter Filename: ")
                verify = os.path.exists(filename)
                if (verify != True):
                    print ("The file does not exist. Please try again.\n")
                else:
                    var2 = False
                    file1 = open(filename, "r")
#Creating a string with the words from the file
                    string1 = file1.read()
#Getting rid of special characters
                    string2=re.sub('[^a-zA-Z\s]','',string1)
#Splitting into separate elements
                    words = string2.lower().split()
#Going through english words
                    eng = open("EnglishWords.txt", "r")
                    engwords = eng.read()
                    engwordslist = engwords.split()
                    eng.close()
                    i=0
                    j=0
#Going through all words in the string
                    while (i < len(words)):
#Checking for them in the english words
                        if words[i] in engwords:
                            print (words[i])
                            outputfileopen.write(words[i]+"\n")
                            i += 1
                            numofwords += 1
                            numofcorrectwords += 1
#Things to do if the word is not in the english words
                        else:
                            print("The word " + str(words[i]) + " is spelled incorrectly")
                            decision = int ( input ("Press 1 to ignore the mistake. \nPress 2 to mark the word. \nPress 3 to add the word to the dictionary. \nPress 4 to be shown a likely correct spelling.\n" ))
                            var1 = True
#Decide what to do
                            while (var1 == True):
                                if (decision == 1):
                                    numofwords += 1
                                    numofincorrectwords += 1
                                    print ("You decided to ignore the incorrectly spelled word.")
                                    outputfileopen.write(words[i]+"\n")
                                    var1 = False
                                    i += 1
                                elif (decision == 2):
                                    numofwords += 1
                                    numofincorrectwords += 1
                                    print ("You decided to mark the word.")
                                    var1 = False
                                    marked="?" + words[i] + "?"
                                    print(marked)
                                    outputfileopen.write(marked+"\n")
                                    i += 1
                                elif (decision == 3):
                                    numofwords += 1
                                    numofcorrectwords += 1
                                    numofwordstodict +=1
                                    print ("You decided to add the word to the dictionary.")
                                    engwordsopen = open("EnglishWords.txt", "a")
                                    engwordsopen.write(words[i]+"\n")
                                    outputfileopen.write(words[i]+"\n")
                                    var1 = False
                                    i += 1
                                    engwordsopen.close()
                                elif (decision == 4):
#Find a likely word in the english words list
                                    while (var3 == True):
                                        prediction = SequenceMatcher(None, words[i], engwordslist[j]).ratio()
                                        predictionpercent = prediction * 100
#Getting a likely word as a suggested spelling
                                        if (predictionpercent > 70):
                                            feedback = int ( input ("You required a likely correct spelling.\nThe suggested spelling is: " + str(engwordslist[j]) + "\nWould you like to keep it?\nPlease enter 1 to keep the suggested spelling. \nPlease enter 0 if you do not want to keep the suggested spelling.\n") )
                                            if (feedback == 1):
                                                numofwords += 1
                                                numofcorrectwords += 1
                                                numofwordschanged += 1
                                                words[i] = engwordslist[j]
                                                print (words[i])
                                                outputfileopen.write(words[i]+"\n")
                                                i += 1
                                                var1 = False
                                            elif (feedback == 0):
                                                numofwords += 1
                                                numofincorrectwords += 1
                                                numofwordschanged += 1
                                                print (words[i])
                                                outputfileopen.write(words[i]+"\n")
                                                i += 1
                                                var1 = False
                                            var3 = False
                                        else:
                                            j += 1
                                else:
                                    print ("You have to choose between the choices 1, 2, 3 and 4.\nPlease select again.\n")
                                    time.sleep(1)
                    var = False
        elif (spelldecision == 0):
            print("You decided to quit. Have a great day!")
            time.sleep(1)
            quit()
        else:
            print ("You have to choose between 0, 1 or 2.\nPlease select again.\n")
            time.sleep(1)
#Initializing the date
    now = datetime.now()
    dateandtime = now.strftime("%d/%m/%Y %H:%M:%S")
#Initializing the time
    t1 = time.time() - t0
#Writing the statistics
    statistics = str ("The number of words is: " + str(numofwords) + "\nThe number of words spelt correctly is: " + str(numofcorrectwords) + "\nThe number of incorrectly spelt words is: " + str(numofincorrectwords) + "\nThe number of words added to the dictionary is: " + str(numofwordstodict) + "\nThe number of words changed by the user accepting the suggested word is: " + str(numofwordschanged) + "\nThe date and time: " + str(dateandtime) + "\nTime elapsed: " + str(t1))

    outputfileopen.write("\n" + "Summary statistics:\n\n" + statistics + "\n")

    outputfileopen.close()

    print("The input has been spellchecked.\nPress 1 if you would like to return to main menu.\nPress 0 if you would like to quit.\nThank you for using Spellchecker!:)\n")
#Loop for returning to main menu
    while(var4 == True):
        repeatdecision = int (input ("Enter your decision:\n") )
        if(repeatdecision == 0):
            repeat = False
            var4 = False
            quit()
        elif(repeatdecision == 1):
            var4 = False
            continue
        else:
            print("You have to choose between 1 and 0.\n")
