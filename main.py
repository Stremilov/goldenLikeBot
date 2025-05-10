import asyncio

from loader import dp, bot
from core.database.create_tables import engine, Base, fill_video_projects
import handlers


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    fill_video_projects()
    asyncio.run(main())
