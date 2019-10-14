import discord
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")


client.run("NjMzMDI5NTUzNDk2OTE1OTc4.XaQN2g.wUZq5QGGBWzpGtljXxwXRSrBnsU")