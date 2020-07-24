# import discord

# TOKEN = 'NzIxOTk5ODg2ODc0MDUwNjAw.Xuc2Fw.EsGzsDRVt2RUhl56b9qZjDhTxMc'

# client = discord.Client()

# @client.event
# async def on_message(message):
#     # we do not want the bot to reply to itself
#     if message.author == client.user:
#         return
#     if message.content.startswith('!nthella'):
#         await message.channel.send('Nthella Monuse {0.author.mention}'.format(message))

#     if message.content.startswith('!chali'):
#         msg = 'Fanish aanu athilu best'
#         await message.channel.send(msg)

# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name)
#     print(client.user.id)
#     print('------')

# client.run(TOKEN)
import random


def rand_dict():
    a1 = random.randint(0, 9)
    a2 = random.randint(0, 9)
    a3 = random.randint(0, 9)
    a4 = random.randint(0, 9)
    a5 = random.randint(0, 9)
    d = {a1: a5*2, a2: a1*2, a3: a2*2, a4: a3*2, a5: a4*2}
    print(d)
    return list(d.items())

a = rand_dict()
print(a)
# dict_a = dict(a)
# print(dict_a)
# sorted_a = {k: v for k, v in sorted(dict_a.items(), key=lambda item: item[1])}
# print(sorted_a)
