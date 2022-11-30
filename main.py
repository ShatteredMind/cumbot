import asyncio

from bot.events import Events
from settings import bot, TOKEN
from database.utils import init_pudge_names
from database.session import session


async def init_app():
    bot.add_cog(Events(bot))
    await session.init()
    await init_pudge_names()
    await session.create_all()
    print('Init completed')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_app())
    loop.run_until_complete(bot.run(TOKEN))
