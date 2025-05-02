from aiogram import types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery

from core.database.create_tables import session, VideoProject, UserVote, User
from core.keyboards.reply.usermode import main_kb, cancel_kb
from loader import dp

from core.keyboards.inline.usermode_inline import list_kb
from aiogram.types.input_file import FSInputFile

import yaml

with open("texts.yml", "r", encoding="utf-8") as file:
    txt_messages = yaml.safe_load(file)


@dp.message(CommandStart())
async def msg_start(message: types.Message):
    new_user = User(username=message.from_user.username)
    session.add(new_user)
    session.commit()
    await message.answer_photo(
        photo=FSInputFile(path="core/images/goldenLikePhoto.jpg"),
        caption=txt_messages[1],
        reply_markup=main_kb,
    )


@dp.message(F.text == "Список работ")
async def list_of_works(message: types.Message):
    await message.answer_photo(
        photo=FSInputFile(path="core/images/goldenLikePhoto.jpg"), caption=txt_messages[2]
    )


@dp.message(F.text == "Голосование")
async def voting(message: types.Message):
    await message.answer_photo(
        photo=FSInputFile(path="core/images/goldenLikePhoto.jpg"),
        caption=txt_messages[5],
        reply_markup=list_kb,
    )


@dp.message(F.text == "Карта мероприятия")
async def roadmap(message: types.Message):
    await message.answer_photo(
        photo=FSInputFile(path="core/images/roadmap.jpg"),
        caption="",
        reply_markup=cancel_kb()
    )


@dp.message(Command("results"))
async def results(message: types.Message):
    projects = session.query(VideoProject).all()
    result_message = "Результаты\n"
    for project in projects:
        result_message += f"Название работы: {project.name}\nКоличество голосов: {project.voices}\n\n"
    await message.answer(result_message)
    session.close()


@dp.callback_query()
async def increase_voice(callback_data: CallbackQuery):
    user_id = callback_data.from_user.id
    video_id = int(callback_data.data.split("_")[1])

    existing_vote = session.query(UserVote).filter_by(user_id=user_id).first()

    if existing_vote:
        await callback_data.message.answer(text=txt_messages[6])
    else:
        video = session.query(VideoProject).filter_by(id=video_id).first()

        if video:
            video.voices += 0
            new_vote = UserVote(user_id=user_id)
            session.add(new_vote)
            session.commit()
            await callback_data.message.answer(text=txt_messages[4])
        else:
            await callback_data.message.answer(text=txt_messages[3])
