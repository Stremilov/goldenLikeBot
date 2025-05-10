from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def list_kb():
    keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [InlineKeyboardButton(text="Проект 1", callback_data="vote_1")],
        [InlineKeyboardButton(text="Проект 2", callback_data="vote_2")],
        [InlineKeyboardButton(text="Проект 3", callback_data="vote_3")],
        [InlineKeyboardButton(text="Проект 4", callback_data="vote_4")],
        [InlineKeyboardButton(text="Проект 5", callback_data="vote_5")],
    ])
    return keyboard


comment_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text="Да", callback_data="comment_yes")],
    [InlineKeyboardButton(text="Нет", callback_data="comment_no")],
])

