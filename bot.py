from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import wiki

with open("tokenbt.txt", "r") as ftb:
    TOKEN = ftb.readline().strip()


def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


button_list = [
    InlineKeyboardButton("col1", callback_data=...),
    InlineKeyboardButton("col2", callback_data=...),
    InlineKeyboardButton("row 2", callback_data=...)
]



reply_keyboard = [['/address','/phone'], ['/help', '/close']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


button_list = [InlineKeyboardButton('address', callback_data=0),
                  InlineKeyboardButton('phone', callback_data=1),
                  InlineKeyboardButton('help', callback_data=2),
                  InlineKeyboardButton('close', callback_data=3)]
reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=4))

some_strings = ["col1", "col2", "row2"]
button_list = [[KeyboardButton(ss)] for ss in some_strings]
# сборка клавиатуры из кнопок `KeyboardButton`
reply_markup1 = ReplyKeyboardMarkup(build_menu(button_list, n_cols=2))
# отправка клавиатуры в чат



def echo(update, context):
    txt = update.message.text
    if txt.lower() in ['привет', 'здаров']:
        txt = "И тебе привет человек!"
    update.message.reply_text(txt)


def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    reply_markup=reply_markup
    )
    #update.send_message(chat_id=context.chat_id, text="Меню из двух столбцов", reply_markup=reply_markup1)

def button(update, context):
    query = update.callback_query
    variant = query.data

    # `CallbackQueries` требует ответа, даже если
    # уведомление для пользователя не требуется, в противном
    #  случае у некоторых клиентов могут возникнуть проблемы.
    # смотри https://core.telegram.org/bots/api#callbackquery.
    query.answer()
    # редактируем сообщение, тем самым кнопки
    # в чате заменятся на этот ответ.
    query.edit_message_text(text=f"Выбранный вариант: {variant}")

def close_keyboard(update, context):
    update.message.reply_text("Ok", reply_markup=ReplyKeyboardRemove())

def help(update, context):
    update.message.reply_text(
        "/start - запуск бота\n/help - вызов помощи")

def address(update, context):
    update.message.reply_text("Выдаем на экран какой-то адрес, или ищем его в интерете")

def phone(update, context):
    update.message.reply_text("Идет взлом Пентагона, тикайте...")


def wikipedia(update, context):
    update.message.reply_text("Идет поиск в википедии...")
    print(context.args, " ".join(context.args), "=======")
    rezult, urlrez = wiki.search_wiki(" ".join(context.args))
    update.message.reply_text(rezult + urlrez)

def set_timer(update, context):
    chat_id = update.message.chat_id
    try:
        due = int(context.args[0])
        if due < 0:
... (63 lines left)