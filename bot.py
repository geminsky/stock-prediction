import discord

TOKEN = 'secret token'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!nthella'):
        await message.channel.send('Nthella Monuse {0.author.mention}'.format(message))

    if message.content.startswith('!chali'):
        msg = 'Fanish aanu athilu best'
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
