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
channel_id_mudae = 1139449991782477886

bot = commands.Bot(command_prefix=prefix, self_bot=True)

# Tạo biến để theo dõi trạng thái của chức năng và nội dung tin nhắn
function_enabled = False
message_content = "$wa"  # Nội dung mặc định

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def start(ctx, *args):
    global function_enabled, message_content
    if not function_enabled:
        function_enabled = True
        if args:
            message_content = " ".join(args)
        await ctx.send(f"Chức năng hiện đã được kích hoạt với nội dung tin nhắn: {message_content}")
        await send_messages()

@bot.command()
async def stop(ctx):
    global function_enabled
    if function_enabled:
        function_enabled = False
        await ctx.send("Chức năng bây giờ đã dừng lại.")

async def send_messages():
    global function_enabled, message_content
    message_intervals = [10] * 11  # Gửi tin nhắn mỗi 10 giây, tổng cộng 11 lần
    pause_interval = 3600  # Đợi 3600 giây (1 giờ) trước khi gửi tin nhắn tiếp theo

    while function_enabled:
        for interval in message_intervals:
            if not function_enabled:
                break
            await bot.get_channel(channel_id_mudae).send(message_content)
            await asyncio.sleep(interval)
        if function_enabled:
            await asyncio.sleep(pause_interval)  # Đợi 1 giờ trước khi gửi tin nhắn tiếp theo

bot.run(token)