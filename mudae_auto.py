import sys
sys.path.insert(0, 'discord.py-self')

import discord
from discord.ext import commands
import json
import asyncio, time

with open('config.json', 'r') as file:
    config = json.load(file)

token = config['token']
prefix = config['prefix']

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}') 

  async def send_messages():
        while True:
            # Gửi tin nhắn vào các kênh cụ thể
            await bot.get_channel(1139449991782477886).send('$wa')
            await asyncio.sleep(5)
            await bot.get_channel(1139449991782477886).send('$wa')
            await asyncio.sleep(5)
            await bot.get_channel(1139449991782477886).send('$wa')
            await asyncio.sleep(5)
            await bot.get_channel(1139449991782477886).send('$wa')
            await asyncio.sleep(5)
            await bot.get_channel(1139449991782477886).send('$wa')
            await asyncio.sleep(5)
            await bot.get_channel(1139449991782477886).send('$wa')
            await asyncio.sleep(5)
            await bot.get_channel(1139449991782477886).send('$wa')
            await asyncio.sleep(5)
            await bot.get_channel(1139449991782477886).send('$wa')
            await asyncio.sleep(5)
            await bot.get_channel(1139449991782477886).send('$wa')
            await asyncio.sleep(5)
            await bot.get_channel(1139449991782477886).send('$wa')
            time.sleep(3600)  # Đợi 20 giây trước khi gửi tin nhắn tiếp theo (tùy chọn)
    
  # Bắt đầu nhiệm vụ gửi tin nhắn định kỳ khi bot đã sẵn sàng
  asyncio.get_event_loop().create_task(send_messages())

bot.run(token)