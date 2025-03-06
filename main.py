from os import getenv
from aiogram import Bot, Dispatcher
from handlers import router
from handlers import router as client_router

load_dotenv()


#создаем объект бота и диспетчера (маршрутизатора)
bot = Bot(token=getinv("bot_token"))
dp = Dispatcher()
dp.include_router()



dp.run_polling(bot)




