import logging
import settings
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

today = date.today()


def planet(update, context):
    print("Вызван /planet")
    user_planet = update.message.text
    if 'Mars' in user_planet:
        mars = ephem.Mars(today)
        constellation = ephem.constellation(mars)
        print(constellation)
        update.message.reply_text(
            f'Планета находится в созвездии {constellation}')
    else:
        update.message.reply_text('Такой планеты нет')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():

    mybot = Updater(
        settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('бот стартовал')

    mybot.start_polling()

    mybot.idle()


def greet_user(update, context):
    print("Вызван /start")

    update.message.reply_text('Вечер в хату! Ты вызвал команду /start')


if __name__ == "__main__":
    main()
