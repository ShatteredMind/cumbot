import asyncio

from bot.events import Events
from database.utils import init_pudge_names
from database.session import session
from settings import bot, TOKEN


async def init_app():
    bot.add_cog(Events(bot))
    await session.init()
    await session.create_all()
    await init_pudge_names()
    print('Init completed')


async def main():
    await init_app()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_app())
    loop.run_until_complete(bot.run(TOKEN))
