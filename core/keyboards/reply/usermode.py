from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Список работ")],
        [KeyboardButton(text="Голосование")],
        [KeyboardButton(text="Карта мероприятия")],
    ]
)

cancel_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Назад")]])

