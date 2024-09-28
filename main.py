from config import TOKEN
import asyncio
from aiogram import Bot, Dispatcher, types , F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils import executor
import logging

#Первичная логика бота 
bot = Bot(token=TOKEN) 
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📋Список команд")
    btn2 =types.KeyboardButton("Список сервисов")
    
    markup.add(btn1, btn2)
 #   btn5 = types.KeyboardButton("/test1")
  #  markup.row(btn5)
    await message.answer(
        "Используй команду /help для списка команд, либо выбери команду в меню",
        reply_markup=markup
    )

@dp.message(F.text == "📋Список команд")
async def btn1(message: Message):
    await help(message)  

@dp.message(F.text == "Список сервисов")
async def btn2(message: Message):
    await help(message)
    
#@bot.message_handler(func=lambda message: message.text == "test1")
#def btn3(message):
#    test1(message)   

@dp.message(Command('help'))    
async def help(message: Message):
    await message.answer("Список команд: /start , /help , /list")

''' Тестирование '''   

   
''' Основа '''    
    
# @bot.message_handler(commands=['listy'])
# async def listy(message):
#     markup = types.ReplyKeyboardMarkup()
#     lsbtn1 = types.KeyboardButton("Onex")
#     markup.row(lsbtn1)
#     lsbtn2 =types.KeyboardButton("Shipper")
#     markup.row(lsbtn2)
#     bot.send_message(message.chat.id, f"Выберите желаемвый сервис", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Выбран Onex")
# async def lsbtn1(message):
#     onex(message)   

# @bot.message_handler(func=lambda message: message.text == "Выбран Shipper")
# async def lsbtn2(message):
#     shipper(message) 

# # Выбран Onex

# @bot.message_handler(commands=['onex'])
# async def onex(message):
#     markup = types.ReplyKeyboardMarkup()
#     obtn1 = types.KeyboardButton("В Америке")
#     markup.row(obtn1)
#     obtn2 =types.KeyboardButton("В пути")
#     markup.row(obtn2)
#     obtn3 =types.KeyboardButton("Записать в GDocs")
#     markup.row(obtn3)
#     bot.send_message(message.chat.id, f"Выберите пункт", reply_markup=markup)
    
# @bot.message_handler(func=lambda message: message.text == "В Америке")
# async def obtn1(message):
#     o_usa(message)   

# @bot.message_handler(func=lambda message: message.text == "В пути")
# async def obtn2(message):
#     o_way(message)     
    
# @bot.message_handler(func=lambda message: message.text == "Записать в GDocs")
# async def obtn3(message):
#     o_docs(message)    

# @bot.message_handler(commands=['ousa'])
# async def o_usa(message):
#     bot.send_message(message.chat.id, f"Срабатывание Onex В Америке")

# @bot.message_handler(commands=['oway'])
# async def o_way(message):
#     bot.send_message(message.chat.id, f"Срабатывание Onex В пути")
    
# @bot.message_handler(commands=['odocs'])
# async def o_docs(message):
#     bot.send_message(message.chat.id, f"Срабатывание Onex Запись в доки")
        
# # Выбран Shipper

# @bot.message_handler(commands=['shipper'])
# async def shipper(message):
#     markup = types.ReplyKeyboardMarkup()
#     sbtn1 = types.KeyboardButton("В Америке")
#     markup.row(sbtn1)
#     sbtn2 =types.KeyboardButton("В пути")
#     markup.row(sbtn2)
#     sbtn3 =types.KeyboardButton("Записать в GDocs")
#     markup.row(sbtn3)
#     bot.send_message(message.chat.id, f"Выберите пункт", reply_markup=markup)
    
# @bot.message_handler(func=lambda message: message.text == "В Америке")
# async def sbtn1(message):
#     s_usa(message)   

# @bot.message_handler(func=lambda message: message.text == "В пути")
# async def sbtn2(message):
#     s_way(message)     
    
# @bot.message_handler(func=lambda message: message.text == "Записать в GDocs")
# async def sbtn3(message):
#     s_docs(message)

# @bot.message_handler(commands=['s_usa'])
# async def s_usa(message):
#     bot.send_message(message.chat.id, f"Срабатывание Onex В Америке")

# @bot.message_handler(commands=['s_way'])
# async def s_way(message):
#     bot.send_message(message.chat.id, f"Срабатывание Onex В пути")
    
# @bot.message_handler(commands=['s_docs'])
# async def s_docs(message):
#     bot.send_message(message.chat.id, f"Срабатывание Onex Запись в доки")


# #Фразовые команды    
# @bot.message_handler()
# async def info(message):
    
#     if (message.text.lower() == 'привет' or message.text.lower() == 'салам'):
#         bot.send_message(message.chat.id, f"Еще раз привет,пожалуйста, используй команду /help или меню для работы со мной")
           
#     elif (message.text.lower() == 'список команд' or message.text.lower() == 'команды'):
#         help(message) 
                       
#     else:
#         bot.send_message(message.chat.id, "Не знаю такую команду, проверьте на правильность написания команды. Используйте /help или меню")

''' Запуск бота '''

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
    