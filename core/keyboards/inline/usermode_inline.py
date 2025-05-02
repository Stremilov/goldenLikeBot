from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

list_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data="btn_0")],
        [InlineKeyboardButton(text="2", callback_data="btn_1")],
        [InlineKeyboardButton(text="3", callback_data="btn_2")],
        [InlineKeyboardButton(text="4", callback_data="btn_3")],
        [InlineKeyboardButton(text="5", callback_data="btn_4")],
        [InlineKeyboardButton(text="6", callback_data="btn_5")],
        [InlineKeyboardButton(text="7", callback_data="btn_6")],
        [InlineKeyboardButton(text="8", callback_data="btn_7")],
        [InlineKeyboardButton(text="9", callback_data="btn_8")],
        [InlineKeyboardButton(text="10", callback_data="btn_9")],
    ]
)
