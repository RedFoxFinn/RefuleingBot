import os

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_PW = os.environ.get('BOT_PW')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "This is a TG bot for logging refueling our car.")
    bot.send_message(message.chat.id, '''You have to verify you have rights to use this bot. Please, enter your password with command /verify <password>''')

@bot.message_handler(commands=['verify'])
def verify(message):
    if message.text == f'/verify {BOT_PW}':
        bot.reply_to(message, 'You have been successfully verified!')
    else:
        bot.reply_to(message, 'Are you sure? Please, try again')

def main():
    bot.polling()

if __name__ == '__main__':
    main()