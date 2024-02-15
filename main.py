import logging

from bot.settings.settings import data_settings
from bot.handlers import *

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(name)s - "
"(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")


def main():
    updater = Updater(data_settings.bots.bot_token)

    dispatcher = updater.dispatcher

    # Обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("convert", convert))

    # Обработчик текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Стартуем бота
    updater.start_polling()

    # Бот будет работать, пока не остановим его явно или не произойдет ошибка
    updater.idle()


if __name__ == '__main__':
    main()
