import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import nextcord

import nextcord
import datetime
from nextcord.ext import commands
from nextcord import SyncWebhook

from utils.config_loader import load_config


config = load_config()
TOKEN = config.get("bot_token")
webhook_url = config.get("webhook_url")


intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=["?"], intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(
        activity=nextcord.Streaming(
            name="?ask | rlyaa.xyz",
            url="https://youtu.be/sVaQQRx6-es?si=WddbMqrjlhmF6kF8",
        )
    )
    print("Bot is ready!")

bot.load_extension("command.AI_interaction")
bot.load_extension("command.LensMind")
bot.load_extension("command.summary")

if __name__ == "__main__":
    bot.run(TOKEN)