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
YOUR_SPECIFIC_CHANNEL_ID = config['YOUR_SPECIFIC_CHANNEL_ID']

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}') 

@bot.command()
async def ping(ctx):
  await ctx.message.delete()
  await ctx.send("Pong")

#Gửi UID HSR
@bot.command()
async def uidhsr(ctx):
  await ctx.message.delete()
  await ctx.send("801672829")

#Gửi UID GI
@bot.command()
async def uidgi(ctx):
  await ctx.message.delete()
  await ctx.send("805423229")

@bot.event
async def on_message(message):
   if message.author == bot.user:
      return

   if message.channel.id != YOUR_SPECIFIC_CHANNEL_ID:
      await bot.process_commands(message)
      return

   await bot.process_commands(message)

   words = message.content.lower().split()
   with open('danhsach.txt','r') as file:
      danh_sach_tu = [line.strip().lower() for line in file]

# Chuyển nội dung tin nhắn và danh sách từ về chữ thường để so sánh
   message_content_lower = message.content.lower()
   danh_sach_tu_lower = [tu.lower() for tu in danh_sach_tu]
# Kiểm tra xem từng từ trong danh sách từ có tồn tại trong tin nhắn không
   '''for tu in danh_sach_tu_lower:
    if tu in message_content_lower:
      await asyncio.sleep(10) # Đợi 10 giây
      await message.add_reaction("❤")'''
# Kiểm tra embed trong tin nhắn
   for embed in message.embeds:
       embed_content = embed.description.lower() if embed.description else ""
       for tu in danh_sach_tu:
         if tu in embed_content:
            #await asyncio.sleep(10)  # Đợi 10 giây
            await message.channel.send(f"<a:Verify:980814232599793705> Claim giúp anh nhân vật trong anime: **{tu}** với đi nè.....")
            await message.add_reaction("❤")

#Thả emoji khi có chứa từ Tân trong tin nhắn.
   if any(word in ["tân"] for word in words):
      await message.add_reaction("❤")

#Thả emoji khi được reply tin nhắn.
   if message.reference:
      replied_message = await message.channel.fetch_message(message.reference.message_id)
      if replied_message.author == bot.user:
         await message.add_reaction("❤")

bot.run(token)