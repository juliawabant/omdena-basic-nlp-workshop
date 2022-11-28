from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

"""Simple Chatbot training using Chatter Python library.
Training generates a .db file in project folder."""

chatbot = ChatBot("Health example chatbot")
trainer = ChatterBotCorpusTrainer(chatbot)

# TODO:
#After reviewing datasets list at https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english, use health dataset to train the model
trainer.train(
    
)

#TODO:
#Use trained chatbot to answer the following question : "Are you feeling sick ?"

response = 
print(response)
