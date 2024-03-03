import telebot
from telebot import types

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, "به ربات دانلود فیلم خوش اومدی، برای عضویت روی /membership کلیک کن"
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("درباره ما")
    item2 = types.KeyboardButton("تماس با ما")
    item3 = types.KeyboardButton("⬅️")
    markup.add(item1, item2, item3)

    bot.send_message(
        message.chat.id, "یکی از موارد زیر را انتخاب کنید", reply_markup=markup
    )

@bot.message_handler(commands=['membership'])
def send_membership_plans(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("یک ماهه")
    item2 = types.KeyboardButton("سه ماهه") 
    item3 = types.KeyboardButton("⬅️")
    markup.add(item1, item2, item3)

    bot.send_message(
        message.chat.id, "نوع عضویت خود را تعیین کنید", reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    if message.text == "درباره ما":
        bot.send_message(message.chat.id, " این ربات توسط سعید توسعه داده شده است")
    elif message.text == "تماس با ما":
        email = "text@test.com"
        websute = "www.test.com"
        contact_info =f"اطلاعات تماس \n ایمل: {email} \n وبسایت: {websute}"
        bot.send_message(message.chat.id, contact_info)
    elif message.text == "سه ماهه":
        bot.send_message(message.chat.id, "شما عضویت سه ماهه را انتخاب کردید")
    elif message.text == "یک ماهه":
        bot.send_message(message.chat.id, "شما عوضیت یک ماهه را انتحاب کردید")
    elif message.text == "⬅️":
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "شما به منوی اصلی بازگشتید", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "متوجه منظور شما نشدم!")


if __name__ == "__main__":
    bot.polling()