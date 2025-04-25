import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
load_dotenv()

##################
## 뭐가 달라졌나요?
# - intents 추가
# - 가위바위보 게임 추가
# - !rps 명령어 추가
# - 그 외의 명령어 몇가지 추가
##################


intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 접근 허용

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("봇이 준비되었습니다!")
    print("봇 이름:%s" % bot.user.name)

    await bot.sync_commands()
    print("커맨드 동기화 완료!")



@bot.command(name='ping',description='Ping Pong!')
async def ping(ctx):
    await ctx.send("Pong!")



@bot.command(name='echo', description='따라 말하기')
async def echo(ctx, *, message: str):
    await ctx.send(message)



@bot.command(name='calc', description='계산기')
async def calc(ctx, *, expression: str):
    result = eval(expression)
    await ctx.send(f"결과: {result}")
        


# 복사해서 적용해보세요.
@bot.command(name='rps', description='가위바위보 게임')
async def rps(ctx, user_choice: str):
    import random
    choices = ['가위', '바위', '보']
    if user_choice not in choices:
        await ctx.send("가위, 바위, 보 중 하나를 입력해주세요!")
        return
    
    bot_choice = random.choice(choices)
    result = ""
    if user_choice == bot_choice:
        result = "비겼어요!"
    elif (user_choice == "가위" and bot_choice == "보") or \
         (user_choice == "바위" and bot_choice == "가위") or \
         (user_choice == "보" and bot_choice == "바위"):
        result = "이겼어요!"
    else:
        result = "졌어요!"

    await ctx.send(f"당신: {user_choice} | 봇: {bot_choice} → {result}")



bot.run(os.getenv('DISCORD_BOT_TOKEN'))