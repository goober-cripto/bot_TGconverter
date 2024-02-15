from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from bot.utils.exchangeRate import currency_converter


def start(update: Update, context: CallbackContext) -> None:
    """Обработка команды /start"""
    update.message.reply_text('Привет! Я бот для конвертации валют. '
                              'Используй команду /help, чтобы узнать доступные команды.')


def help_command(update: Update, context: CallbackContext) -> None:
    """Обработка команды /help"""
    update.message.reply_text('Доступные команды:\n'
                              '/start - Начать взаимодействие с ботом\n'
                              '/help - Получить справку по командам\n'
                              '/convert <сумма> <валюта_из> в <валюта_в> - Конвертировать валюту')


def echo(update: Update, context: CallbackContext) -> None:
    """Обработка текстовых сообщений"""
    text = update.message.text
    if text.lower() == 'привет':
        update.message.reply_text('Привет!')
    else:
        update.message.reply_text('Не понимаю, что вы говорите.')


def convert(update: Update, context: CallbackContext) -> None:
    """ Обработка команды /convert"""
    text = update.message.text.split()
    if len(text) != 5:
        update.message.reply_text('Используйте команду в формате /convert <сумма> <валюта_из> в <валюта_в>')
        return
    amount = text[1]
    currency_from = text[2].upper()
    currency_to = text[4].upper()

    try:
        amount = float(amount)
    except ValueError:
        update.message.reply_text('Неверный формат суммы')
        return

    try:
        exchange_rate = currency_converter(amount, currency_from, currency_to)
        update.message.reply_text(f'За {amount} {currency_from}\nвы получите: <b>{exchange_rate} {currency_to}</b>', parse_mode='HTML')

    except Exception as e:
        update.message.reply_text('Ошибка при конвертации валюты')




