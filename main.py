import asyncio

from events import Events
from settings import bot, TOKEN
from store.database.models import init_pudge_names
from store.database.accessor import session


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
