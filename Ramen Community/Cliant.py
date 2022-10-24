import discord

intents = discord.Intents.default()  # デフォルトのIntentsオブジェクトを生成
intents.typing = False  # typingを受け取らないように
client = discord.Client(intents=intents)

@client.event
# 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
async def on_ready(): 
    embed = discord.Embed( # Embedを定義する
                          title="ルール",# タイトル
                          color=0x00ff00, # フレーム色指定(今回は緑)
                          description="RamenCommunity/ラーメンコミニュティ ルール", # Embedの説明文 必要に応じて
                          url="https://sites.google.com/view/ramendocs/" # これを設定すると、タイトルが指定URLへのリンクになる
                          )
    embed.set_author(name=client.user, # Botのユーザー名
                     url="https://repo.exapmle.com/bot", # titleのurlのようにnameをリンクにできる。botのWebサイトとかGithubとか
                     icon_url="https://blog.zpw.jp/test/uploads/45b313.png" # Botのアイコンを設定してみる
                     )

    embed.set_thumbnail(url="https://blog.zpw.jp/test/uploads/d6cbf1.png") # サムネイルとして小さい画像を設定できる

    embed.set_image(url="https://blog.zpw.jp/test/uploads/cb189b.png") # 大きな画像タイルを設定できる

    embed.add_field(name="フィールド１",value="値１") # フィールドを追加。
    embed.add_field(name="フィールド２",value="値２")

    embed.set_footer(text="made by SHUtk", # フッターには開発者の情報でも入れてみる
                     icon_url="https://blog.zpw.jp/test/uploads/0ad677.png")

    channel = client.get_channel("1032265541211148318")

    await channel.send(embed=embed) # embedの送信には、embed={定義したembed名}

client.run("MTAzMjk3NDMyMTQzOTc0MDAwNQ.G1x86D.aJFoY-_GEcK50JUHyvL4LwkzHTVVXWo4xoAzLk")
