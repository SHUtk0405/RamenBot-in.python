import discord
from discord.ext import commands
import random

bot = commands.Bot(
    command_prefix="rm!",
    case_insensitive=True, 
    intents=discord.Intents.all(),
    help_command=None
)
        

    
@bot.command()  
async def help(ctx):
    embed = discord.Embed(title="Help", description="RamenBotHelp", color=0xeee657)

    embed.add_field(name="prefix", value="rm!")

    embed.add_field(name="info", value="このBotの詳細を表示")

    embed.add_field(name="nyancat", value="ニャンキャットのGifが再生されるよ！")
    
    embed.add_field(name="文章反応", value="適当に反応してくれるよ()")      
    
    embed.add_field(name="おすすめのラーメン", value="おすすめのラーメンを決めてくれるよ！")     

    embed.add_field(name="暇", value="おすすめの暇つぶしを教えてくれるよ！")

    embed.add_field(name="icom", value="<@989423244295700540>のアイコンGetだぜ！")  

    embed.add_field(name="サポートサーバー", value="[Invite link](https://discord.gg/HnxUP6Ju2V)")    

    await ctx.send(embed=embed)
    
@bot.command()  
async def info(ctx):
    embed = discord.Embed(title="RamenCommunityBot", description="Nicest bot there is ever.", color=0xeee657)

    embed.add_field(name="Author", value="<!shuuuCream#8444&ラーメン＠アンパンマン工場の器具#0798>")

    embed.add_field(name="導入数", value=f"{len(bot.guilds)}")    

    embed.add_field(name="サポートサーバー", value="[Invite link](https://discord.gg/HnxUP6Ju2V)")

    embed.set_image(url="https://blog.zpw.jp/test/uploads/d85acf.png")

    await ctx.send(embed=embed)
    

 
@bot.command()  
async def nyancat(ctx):
    await ctx.reply("https://c.tenor.com/2urDxuvLvKIAAAAM/peooo-dude.gif")    


@bot.listen('on_message')
async def whatever_you_want_to_call_it(message):
    if message.author.bot:
        return
    if message.content == "醤油ラーメン":
        await message.channel.send(file=discord.File("/home/server/デスクトップ/Ramen Community/images.jpeg"))
        await message.channel.send("へい！お待ち！")
    if message.author.bot:
        return    
    if message.content == "塩ラーメン":
        await message.channel.send("へい！お待ち！")
        await message.channel.send(file=discord.File("/home/server/デスクトップ/Ramen Community/IMG_7125.jpeg"))
    if message.author.bot:
        return        
    if message.content == "何食べようかな":
        await message.channel.send("そこはラーメンやろ")                
    if message.author.bot:
        return   
    if message.content == "ラーメン":
        await message.channel.send("美味しいよね♥")
    if message.author.bot:
        return   
        await message.channel.send(content)
    elif message.content == "おはよう":
        await message.channel.send("おはよう！！")

@bot.command()
async def icom(message):
    await message.channel.send(file=discord.File("/home/server/デスクトップ/Ramen Community/607acad71a2de558ae06716d8100d4c6.png"))
    await message.channel.send("しょうがないなぁ〜（渡す気満々）")

@bot.command()
async def 暇(ctx):
    hima = ["過疎を止めてくれぇ！","Youtubeみれば？","そんなんラーメン食べる以外ないやろ","Twitter見ればよくね？"]
    await ctx.send(random.choice(hima))

#Kickのコマンド
@bot.command()
@commands.has_permissions(manage_roles=True, kick_members=True)
async def kick(ctx, member:discord.Member, reason):
 await member.kick(reason=reason)
 embed=discord.Embed(title="KICK", color=0xff0000)
 embed.add_field(name="メンバー", value=f"{member.mention}", inline=False)
 embed.add_field(name="理由", value=f"{reason}", inline=False)
 await ctx.send(embed=embed)

#BANコマンドのコード 
@bot.command()
@commands.has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, member:discord.Member, reason):
 await member.ban(delete_message_days=7, reason=reason)
 embed=discord.Embed(title="BAN", color=0xff0000)
 embed.add_field(name="メンバー", value=f"{member.mention}", inline=False)
 embed.add_field(name="理由", value=f"{reason}", inline=False)
 await ctx.send(embed=embed)
    
@bot.command()
async def おすすめのラーメン(ctx):
    ramen = ["醤油","塩","豚骨","味噌","お前はラーメン食べてはならぬ"]
    await ctx.send(random.choice(ramen))
    
@bot.command()
async def cmd(message):
    await message.channel.send("コマンドを受信しました。")
    print("コマンドを受信しました。(cmd)")

@bot.event #サーバーを抜けた人を送信
async def on_member_join(member):
    guild = bot.get.guild(1032263043855437825)
    channel = bot.get_channel(1032263044593627148)
    await channel.send(f"「{member.name}」が参加しました！よろしくね！\n <marc1:1034009982804435005> <#1033863434871255051>を確認しましょう！")

@bot.event #サーバーを抜けた人を送信
async def on_member_remove(member):
    guild = bot.get.guild(1032263043855437825)
    channel = bot.get_channel(1032263044593627148)
    await channel.send(f"「{member.name}」が抜けました(;_;)")

@bot.event
async def on_ready():
    channel = bot.get_channel(1033696768745021511)
    await channel.send('Bot起動✅or再起動しました🔄')
    print("Botは正常に起動しました！")
    print(bot.user.name)  # Botの名前
    print(bot.user.id)  # ID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
    await bot.change_presence(activity=discord.Game(name=f"RamenCommunity/{len(bot.guilds)}のサーバーに参加中**rm!help**"), status=discord.Status.dnd)


bot.run('Token')
