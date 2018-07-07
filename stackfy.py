#bot related imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

#storage related imports
import json

# NLP related imports
import semantic_search

updater = Updater(token="")

dispatcher = updater.dispatcher

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Olá, eu sou o Stackfy.\nSou capaz de encontrar perguntas no StackOverflow baseadas em textos de usuário.")

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

def parse(bot, update):
	query = update.message.text
	question_obj = semantic_search.best_match(query)
	formated_text = "{}\n\nQuestion:\n{}\n\nAnswer:\n{}".format(question_obj["question"], question_obj["body"], question_obj["answer"])
	bot.send_message(chat_id=update.message.chat_id, text=formated_text)
	

echo_handler = MessageHandler(Filters.text, parse)
dispatcher.add_handler(echo_handler)


updater.start_polling()

