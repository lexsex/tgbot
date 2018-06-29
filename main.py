import telebot
from telebot.apihelper import ApiException


bot = telebot.TeleBot("550759224:AAE2GvBjmW7J_MmhHfTOyF2wib1f8Viq2Dk")


@bot.message_handler(commands=["start"])
def handle_command(message):
    bot.send_message(message.from_user.id, "Отправьте Ваше объявление боту.")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        bot.send_message(575287839, message.from_user.username)
        bot.send_message(575287839, message.text)
    except ApiException:
        bot.send_message(575287839, message.from_user.id)
        bot.send_message(575287839, message.text)
    bot.send_message(message.from_user.id, "Ваше объявление в обработке.")


bot.polling(none_stop=True, interval=0)
