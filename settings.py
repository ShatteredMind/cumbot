import os

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

""" BOT CONFIGURATION """

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
CHANNEL = os.getenv("DISCORD_CHANNEL")

intents = Intents.all()
bot = commands.Bot(".", intents=intents)

""" DATABASE CONFIGURATION """

DATABASE = {
    "POSTGRES_USER": os.getenv("POSTGRES_USER"),
    "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    "POSTGRES_DB": os.getenv("POSTGRES_DB"),
    "POSTGRES_PORT": os.getenv("POSTGRES_PORT"),
    "POSTGRES_HOST": os.getenv("POSTGRES_HOST")
}

DATABASE_URI = f"postgresql+asyncpg://" \
    f"{DATABASE['POSTGRES_USER']}:{DATABASE['POSTGRES_PASSWORD']}@" \
    f"{DATABASE['POSTGRES_HOST']}/{DATABASE['POSTGRES_DB']}"
