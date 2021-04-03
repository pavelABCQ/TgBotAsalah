import telebot

buttons = ReplyKeyboardMarkup()

bot = telebot.TeleBot("1798380147:AAEjWdMGWsQEaHqzuy8EFUxBLsOvJu0ACZw")

@bot.message_handler(content_types = ["text"])
def home(message):
	bot.send_message(message.chat.id, message.text)

@bot.message_handler(command = ["time"])
def time(message):

	try:
		due = int(due = message.text)
		if due < 0:
			bot.send_message(chat.message.id, "Прошлое не вернуть! :( ")
			return 0

		bot.send_message(chat.message.id, "all successfull")
	except:
		bot.send_message(message.chat.id, "UNCORRECT")



bot.polling(none_stop = True)