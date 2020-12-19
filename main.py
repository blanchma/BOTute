import os
import discord
import requests
import json
import random
from replit import db

client = discord.Client()

def get_quote():
  response = requests.get('http://philosophy-quotes-api.glitch.me/quotes')
  quotes = json.loads(response.text)
  quote_data = random.choice(quotes)
  print('quote_data', quote_data)
  quote = '{0}\n\t-{1}'.format(quote_data['quote'], quote_data['source'])

  return quote

@client.event
async def on_ready():
  print('We have logged as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  message_text = message.content.lower()
  print('message_text', message_text)
  if message_text.index('$iluminame') > -1:
    quote = get_quote()
    await message.channel.send(quote)


client.run(os.getenv('TOKEN'))

