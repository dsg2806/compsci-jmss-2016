import nltk
from nltk import tokenize
import random
import time
import wikipedia
from chatterbot import ChatBot

bot = ChatBot("Terminal",
              storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
              logic_adapters=[
                  "chatterbot.adapters.logic.EvaluateMathematically",
                  "chatterbot.adapters.logic.TimeLogicAdapter",
                  "chatterbot.adapters.logic.ClosestMatchAdapter"
              ],
              io_adapter="chatterbot.adapters.io.TerminalAdapter",
              database="../database.db")
# Train based on the english corpus
bot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
bot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
bot.train("chatterbot.corpus.english.conversations")

# who questions, auto correct, what is
negativity = 0
numCounter = 0
continuea = 0
nameCheck = 0
nounNum = 0
greetingsList = ["Hello, how are you?", "Wassup man?", "Hey, hows things?", "Hi dude",
                 "G'Day lads"]
negativeList = ["I sense negativity...", "Why so sad?", "You negative person.", "Are you serious?", "Cheer up buddy!"]
positiveList = ["I can feel the happiness from here!", "That sounds awesome!", "You fun person.", "Cool.",
                "I am happy for you!"]
replyNegList = []
potNegAns = ["n't", "no", "cannot", "bad", "can't", "nope", "terrible"]
questionAreList = ["Probably?", "Yes.", "Yeh?", "Nah...", "No way.", "No.", "Yeh!", "Nah!"]
howList = ["Well I'm alright but...", "Seems good.", "Ehh...ok I guess",
           "I think I am alright, in regards to that thanks...", "Fine!"]

uncertainList = ["I don't understand your uncertainty...", "How are you not sure?", "You can't be serious.",
                 "Are you sure?",
                 "It can't be..."]
profanityList = ["Watch your profanity...", "Mind your language son.", "Watch your mouth!", "Don't say that!",
                 "You what?"]
theList = ["Good to note.", "I understand...", "I don't understand...", "Are you sure of that fact?",
           "How could it be?"]
helloList = ["hi!", "g'day mate!", "yo!", "hey m8", "waddup?", "hello? hello to you too.", "hello to you too!"]
# print(greetingsList[random.randint(0, 4)])
# inpString = input(greetingsList[random.randint(0, 4)] + " \n")
# searchList = []
e = ""
nameWord = ""
# sentence = inpString
# searchWord = ""

# for i in range (0, len(words)):

# if (words[i] in potNegAns):

#  print(negativeList[random.randint(0, 4)])
#  negativity += 1
# WHATS UP?
# else:
#   print(positiveList[random.randint(0, 4)])
#   break
user_input = "Type something to begin..."

print(user_input)

while True:
    time.sleep(int(random.uniform(0.5, 3)))
    searchList = []
    inpString2 = input("")
    inpString2Str = inpString2
    inpString2 = nltk.word_tokenize(inpString2)
    inpString2A = ""
    if ("name" in inpString2Str.lower()):
        try:
            inpString2A = inpString2Str
            inpStringString = inpString2A
            inpString2A = nltk.pos_tag(inpString2)
            for i in inpString2A:
                #print(str(i) + "\n")
                if i[1] == "JJ" or i[1] == "NNS" or i[1] == "NNP":
                    searchList.append(i[0])
                    nameWord = str(searchList[0])
                    name = nameWord
                    print(nameWord)
                    break
        except ValueError:
            print(searchWord)
            break

    if (inpString2[0].lower() == "are") or (inpString2[0].lower() == "did") or (inpString2[0].lower() == "was") or (inpString2[0].lower() == "do"):
        print(questionAreList[random.randint(0, 7)])
    elif ("hi" in inpString2Str.lower()) or ("hello" in inpString2Str.lower()) or ("g'day" in inpString2Str.lower()):
        print(helloList[random.randint(0, 6)])
        #   elif (inpString2[0].lower() == "not"):
        #   print(negativeList[random.randint(0, 4)])
    elif (inpString2[0].lower() == "but"):
        print(uncertainList[random.randint(0, 4)])

    elif (inpString2[0].lower() == "have"):
        print(questionAreList[random.randint(0, 4)])
    elif (inpString2[0].lower() == "how"):
        print(howList[random.randint(0, 4)])

    elif (inpString2[0].lower() == "the"):
        if inpString2Str.endswith("?"):
            print(profanityList[random.randint(0, 4)])
        else:
            print(theList[random.randint(0, 4)])

    elif (inpString2[0].lower() == "what"):
        checkedVal = 0
        numCounter = 0
        try:
            inpStringString = inpString2
            inpString2 = nltk.pos_tag(inpString2)
            for i in inpString2:

                ### try:
                #     if i.isNumeric() == True:
                # print("Number detected " + i)
                # except ValueError:
                # break
                #  numCounter += 1
                # print(inpString2)
                # print(i)
                try:
                    # print("trying")
                    if i[1] == "JJ" or i[1] == "NN" or i[1] == "NNS" or i[1] == "NNP":
                        # print("it matches")
                        searchList.append(i[0])
                        nounNum += 1
                        # print(searchList)
                        searchWord = str(searchList[0])
                        # print(searchWord)
                        # wikipedia.page(randNoun).content
                        ny = wikipedia.page(searchWord)
                        nySentence = ny.content
                        nySentence = tokenize.sent_tokenize(nySentence)
                        print(nySentence[0])
                        checkedVal = 1
                        break
                except ValueError:
                    break
            if checkedVal == 0:
                print("nothing much")
        except IndexError:
            print(profanityList[random.randint(0, 4)])


            # print(inpString2.index("JJ"))
            # print(searchList)
            # nltk id nouns
            # wikipedia.page("randNoun").content

    elif inpString2 == "":
        print("BREAK")
        break
    else:
        # PROCEED TO CONVERSATIONAL
        user_input = str(inpString2Str)
        bot_input = bot.get_response(user_input)

# while continuea == 0:
#    inp = input("")
#    if inp == "" or " ":
#        print("blank")
#        break
#    print(inp)

# print(findWholeWord("n't" or "no" or "cannot" or "bad")(sentence))
# for i in range(len(words)):
#    if ("n't" or "no" or "cannot" or "bad" or "can't" or "nope" or "terrible") == i:
#        print("NEGATIVE")
