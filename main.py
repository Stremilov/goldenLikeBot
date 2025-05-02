import asyncio

from loader import dp, bot
from core.database.create_tables import engine, Base
import handlers


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    asyncio.run(main())
