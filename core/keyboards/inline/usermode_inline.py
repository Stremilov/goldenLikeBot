from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

projects = [
        "Ни вчера, ни завтра",
        "Не убегай",
        "Дом",
        "Internal noise",
        "Рассудок",
        "солл",
        "Чёрные мопсы",
        "Инсайт",
        "Доппельгангер",
        "slam casino - #XOXO",
        "Работа кинотеатров в годы Блокады",
        "ЯМЫ"
    ]


def list_kb():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton(text=f"{project}", callback_data=f"vote_{i}")]
        for i, project in enumerate(projects)
    ])

    return keyboard


def read_kb():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
        [InlineKeyboardButton(text=f"{project}", callback_data=f"read_{i + 1}_{i}")]
        for i, project in enumerate(projects)
    ])

    return keyboard


comment_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text="Да", callback_data="comment_yes")],
    [InlineKeyboardButton(text="Нет", callback_data="comment_no")],
])

