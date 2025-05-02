from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Список работ")],
        [KeyboardButton(text="Голосование")],
    ]
)

cancel_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Назад")]])

