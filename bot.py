import discord
import requests
import json

def GetRandomFact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    r = json.loads(requests.get(url).text)
    return r["text"]

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!random'):
        await message.channel.send(GetRandomFact())

@client.event
async def on_ready():
       print('Logged in as')
       print(client.user.name)
       print(client.user.id)
       print('------')

client.run(TOKEN)
