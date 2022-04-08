import os
import telebot
 
 bot = telebot.TeleBot('5207380248:AAGuFoflyrKSOFHIg39JfHIJciikexHMMAM')

 @bot.message_handler(commands=["startbot"])
 def send_welcome(message):
     bot.reply_to(message,"Hello! I am Group security bot How can i help you")

@bot.message_handler(commands=["contactadmin"])
def send_message(message):
     bot.send_message(message, "https://t.me/SadithST")

@bot.message_handler(commands=["setourcommands"])
def send_message(message):
     bot.send_message(message, "Ok... now you can contact our Telegram assistance - https://t.me/SadithST")

@bot.message_handler(commands=["copybot"])
def send_message(message):
     bot.reply_to(message, "Please send the API Code and then we activate the basic commands")
     
bot.polling()
