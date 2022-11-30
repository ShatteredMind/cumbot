from typing import Any, List

from sqlalchemy import update, select

from database.session import session
from bot.const import PUDGE_NAMES
from models import Pudge, Word


async def get_all_titles_for_model(model: Any) -> List[str]:
    entities = await session.execute(select(model))
    entity_titles = [entity[0].title for entity in entities]
    return entity_titles


async def add_cum_word(title) -> str:
    query = select(Word).where(Word.title == title)
    result = await session.execute(query)
    cum_word = result.scalars().first()
    if cum_word:
        message = f'Слово **{cum_word.title}** было использовано {cum_word.count} раз'
        await increment_cum_word(cum_word)
    else:
        message = f'Поздравляю! Cлова **{title}** еще не было!'
        cum_word = Word(title=title)
        session.add(cum_word)
        await session.commit()
    return message


async def increment_cum_word(cum_word):
    query = (
        update(Word)
        .where(Word.id == cum_word.id)
        .values(count=cum_word.count + 1)
        .execution_options(synchronize_session='fetch')
    )
    await session.execute(query)
    await session.commit()


async def init_pudge_names():
    pudge_names = await get_all_titles_for_model(Pudge)
    missing_names = set(PUDGE_NAMES).difference(set(pudge_names))
    for pudge_name in missing_names:
        pudge = Pudge(title=pudge_name)
        session.add(pudge)
        await session.commit()
