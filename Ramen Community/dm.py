import discord
from discord.ext import commands
import random

bot = commands.Bot(
    command_prefix="rm!",
    case_insensitive=True, 
    intents=discord.Intents.all(),
    help_command=None
)
        
import discord
from discord.ext import commands
import random

bot = commands.Bot(
    command_prefix="rm!",
    case_insensitive=True, 
    intents=discord.Intents.all(),
    help_command=None
)
        
@bot.command(pass_context=True)
async def dm(ctx):
    user = discord.utils.get(bot.users, id=899038836942844025)
    await user.send('Hey guys! We have a gift for you!')

@bot.command()
@commands.has_permissions(administrator=True)
async def cmd(message):
    await message.channel.send("コマンドを受信しました。")
    print("コマンドを受信しました。(cmd)")

@bot.event
async def on_ready():
    channel = bot.get_channel(1033696768745021511)
    await channel.send('DmBotverが起動しました✅')
    print("Botは正常に起動しました！")
    print(bot.user.name)  # Botの名前
    print(bot.user.id)  # ID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
    await bot.change_presence(activity=discord.Game(name=f"DmBotver"), status=discord.Status.dnd)


bot.run('Token')

    
@bot.command()
async def cmd(message):
    await message.channel.send("コマンドを受信しました。")
    print("コマンドを受信しました。(cmd)")

@bot.event
async def on_ready():
    channel = bot.get_channel(1033696768745021511)
    await channel.send('Botが起動しました✅')
    print("Botは正常に起動しました！")
    print(bot.user.name)  # Botの名前
    print(bot.user.id)  # ID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
    await bot.change_presence(activity=discord.Game(name=f"RamenCommunity/{len(bot.guilds)}のサーバーに参加中**rm!help**"), status=discord.Status.dnd)


bot.run('Token')
