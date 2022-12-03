import asyncio

from bot.events import Events
from database.utils import init_pudge_names
from database.session import session
from settings import bot, TOKEN


async def init_app():
    bot.add_cog(Events(bot))
    await session.init()
    await init_pudge_names()
    await session.create_all()
    print('Init completed')


async def main():
    await init_app()


if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(bot.run(TOKEN))
