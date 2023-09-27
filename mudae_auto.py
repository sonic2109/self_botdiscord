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

channel_id= 1139449991782477886

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    message_intervals = [10] * 11  # Gửi tin nhắn mỗi 10 giây, tổng cộng 11 lần
    pause_interval = 60  # Đợi 3600 giây (1 giờ) trước khi gửi tin nhắn tiếp theo

    while True:
        for interval in message_intervals:
            await bot.get_channel(channel_id).send('$wa')
            await asyncio.sleep(interval)
        await asyncio.sleep(pause_interval)  # Đợi 1 giờ trước khi gửi tin nhắn tiếp theo

bot.run(token)