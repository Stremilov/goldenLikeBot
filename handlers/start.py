import logging

from aiogram import types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from core.database.create_tables import session, VideoProject, UserVote, User, Comment
from core.keyboards.reply.usermode import main_kb, cancel_kb
from loader import dp
from core.utils.google_sheets import append_comment_to_sheet

from core.keyboards.inline.usermode_inline import list_kb, comment_kb
from aiogram.types.input_file import FSInputFile

import yaml

with open("texts.yml", "r", encoding="utf-8") as file:
    txt_messages = yaml.safe_load(file)


class CommentState(StatesGroup):
    waiting_for_comment = State()


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
        reply_markup=list_kb(),
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
async def process_callback(callback_data: CallbackQuery, state: FSMContext):
    data = callback_data.data.split("_")
    action = data[0]
    
    # Удаляем клавиатуру после нажатия
    await callback_data.message.edit_reply_markup(reply_markup=None)
    
    if action == "vote":
        user_id = callback_data.from_user.id
        video_id = int(data[1])

        existing_vote = session.query(UserVote).filter_by(user_id=user_id).first()

        if existing_vote:
            await callback_data.message.answer(text=txt_messages[6])
        else:
            video = session.query(VideoProject).filter_by(id=video_id).first()

            if video:
                video.voices += 1
                new_vote = UserVote(user_id=user_id)
                session.add(new_vote)
                session.commit()
                
                await state.update_data(project_id=video_id)
                await callback_data.message.answer(
                    text="Спасибо за ваш голос! Хотите оставить комментарий к этой работе?",
                    reply_markup=comment_kb
                )
            else:
                await callback_data.message.answer(text=txt_messages[3])
    
    elif action == "comment":
        if data[1] == "yes":
            await state.set_state(CommentState.waiting_for_comment)
            await callback_data.message.answer("Пожалуйста, напишите ваш комментарий:")
        else:
            await callback_data.message.answer("Спасибо за участие в голосовании!")
            await state.clear()


@dp.message(CommentState.waiting_for_comment)
async def process_comment(message: types.Message, state: FSMContext):
    data = await state.get_data()
    project_id = data.get("project_id")
    
    if project_id:
        project = session.query(VideoProject).filter_by(id=project_id).first()
        if project:
            new_comment = Comment(
                project_id=project_id,
                user_id=message.from_user.id,
                text=message.text
            )
            session.add(new_comment)
            session.commit()

            try:
                append_comment_to_sheet(
                    project_name=project.name,
                    username=message.from_user.username or str(message.from_user.id),
                    comment=message.text
                )
                await message.answer("Спасибо за ваш комментарий!")
            except Exception as e:
                logging.error(e)
                await message.answer("Комментарий сохранен в базе данных, но произошла ошибка при сохранении в таблицу.")
    
    await state.clear()
