import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Fired up and ready to go!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-sj'):
        await message.channel.send('https://www.youtube.com/watch?v=mFyUrebJbDg')

client.run('get your own lmao')