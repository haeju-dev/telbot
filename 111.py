import telepot

bot = telepot.Bot('694271764:AAGOyAluTq1Lq9KyHnZpDIzT4pUUMKNhGKU')
print(bot.getMe())


from pprint import pprint
response = bot.getUpdates()
pprint(response)