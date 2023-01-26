import telebot
import random

bot = telebot.TeleBot('API')
ans = list('')

@bot.message_handler(commands=["start"])
def get_start_command(m):
    bot.send_message(m.chat.id, 'Привет, это бот предсказаний! Напиши /add и добавь фразу в свой список. Ты можешь вывести вес список с помощью команды /write_all. А ещё я могу вывести случайную фразу из твоего списка, для этого напиши /answer.')

@bot.message_handler(commands=["answer"])
def get_text(m):
        bot.send_message(m.chat.id,ans[random.randint(0, len(ans))])

@bot.message_handler(commands=["add"])
def get_text(m):
        bot.send_message(m.chat.id, 'Введите фразу для добавления в список')
        @bot.message_handler()
        def get_text(m):
            ans.append(m.text)

@bot.message_handler(commands=["write_all"])
def get_text(m):
   bot.send_message(m.chat.id, ', '.join(ans))
bot.polling(none_stop=True)