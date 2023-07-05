import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'YOUR API TOKEN HERE'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# setting language

wikipedia.set_lang('uz')

# start command

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Sálem! Bul bot sizge Wikipedia.org saytınan maqalalardı hám maǵlıwmatlardı tabıwda járdemlesedi. \nDıqqat: Wikipedia saytında qaraqalpaq tili joq, sol sebepli maǵlıwmatlardı ózbek tilinde izleń \n \nBotta qátelikler bolsa /help buyrıǵın jiberiń.")

# /help command
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Eger botta qátelikler bolıp atırsa yáki basqa maqsette xabarlasajaq bolsańız: \nProgrammist: @aytjanov999")

# respond

@dp.message_handler()
async def sendWiki(message: types.Message):
     try:
         respond = wikipedia.summary(message.text)
         await message.answer(respond)
     except:
         await message.answer("Bul temaǵa baylanıslı maqala yáki maǵlıwmat joq. \n \nBotta qátelikler bolsa /help buyrıǵın jiberiń.")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
