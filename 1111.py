from pprint import pprint
import telepot

bot = telepot.Bot('694271764:AAGOyAluTq1Lq9KyHnZpDIzT4pUUMKNhGKU')


response = bot.getUpdates()
pprint(response)