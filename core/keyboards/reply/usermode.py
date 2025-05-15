from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Список работ")],
        [KeyboardButton(text="Голосование")],
        [KeyboardButton(text="Карта мероприятия")],
    ]
)

cancel_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Назад")]])

