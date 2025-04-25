import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("봇이 준비되었습니다!")
    print("봇 이름:%s" % bot.user.name)

    await bot.sync_commands()
    print("커맨드 동기화 완료!")



bot.run(os.getenv('DISCORD_BOT_TOKEN'))