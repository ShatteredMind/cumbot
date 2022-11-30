import random
import re

import discord
from discord.ext import commands
from discord.utils import get

from const import COLORS
from models import Pudge
from settings import GUILD, CHANNEL
from store.database.models import get_all_titles_for_model, add_cum_word


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def _get_default_guild(self) -> discord.Guild:
        return self.bot.get_guild(int(GUILD))

    def _get_default_text_channel(self) -> discord.TextChannel:
        return self._get_default_guild().get_channel(int(CHANNEL))

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        await self.bot.wait_until_ready()
        self.bot.get_guild(int(GUILD)).get_channel(int(CHANNEL))

    @commands.Cog.listener()
    async def on_member_join(self, member) -> None:
        message = f'Добро пожаловать в наше дружное **Cum**юнити, {member.name}'
        channel = self._get_default_text_channel()
        await channel.send(message)

    async def _handle_pudge_message(self, message) -> None:
        pudge_names = await get_all_titles_for_model(Pudge)
        index = random.randint(0, len(pudge_names) - 1)
        color_index = random.randint(0, len(COLORS) - 1)
        pudge = pudge_names[index]
        color = COLORS[color_index]
        guild = self._get_default_guild()
        await guild.create_role(name=pudge, color=color)
        role = get(guild.roles, name=pudge)
        user = message.author
        await user.edit(roles=[])
        await user.add_roles(role)

    async def _handle_cum_message(self, message_text) -> None:
        pattern = r'(\w*cum\w*)'
        cum_words = re.findall(pattern, message_text)
        message_text = cum_words[0]
        result = await add_cum_word(message_text)
        channel = self._get_default_text_channel()
        await channel.send(result)

    @commands.Cog.listener()
    async def on_message(self, message) -> None:
        message_text = message.content.lower()
        if message.author == self.bot.user:
            return
        if 'cum' in message_text:
            await self._handle_cum_message(message_text)
        if message_text == '!pudge':
            await self._handle_pudge_message(message)
