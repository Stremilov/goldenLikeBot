from aiogram import types
from core.config_data.config import DEFAULT_COMMANDS


async def set_default_commands(bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command, description)
            for command, description in DEFAULT_COMMANDS
        ]
    )
