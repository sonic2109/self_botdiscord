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
channel_id_mudae = 1116033819552792616

bot = commands.Bot(command_prefix=prefix, self_bot=True)

# Tạo biến để theo dõi trạng thái của chức năng và nội dung tin nhắn
function_enabled = False
message_content = "$w"  # Nội dung mặc định

@bot.event
async def on_ready():
  print(f'Đã đăng nhập vào {bot.user.name}') 

@bot.command()
async def start(ctx, *args):
    global function_enabled, message_content
    if not function_enabled:
        function_enabled = True
        if args:
            message_content = " ".join(args)
        await ctx.send(f"Đã kích hoạt với nội dung tin nhắn: ```{message_content}```")
        await send_messages()

@bot.command()
async def stop(ctx):
    global function_enabled
    if function_enabled:
        function_enabled = False
        await ctx.send("Đã dừng lại.")

async def send_messages():
    global function_enabled, message_content
    message_intervals = [5] * 13  # Gửi tin nhắn mỗi 10 giây, tổng cộng 11 lần
    pause_interval = 3545  # Đợi 3600 giây (1 giờ) trước khi gửi tin nhắn tiếp theo

    while function_enabled:
        for interval in message_intervals:
            if not function_enabled:
                break
            await bot.get_channel(channel_id_mudae).send(message_content)
            await asyncio.sleep(interval)
        if function_enabled:
            await asyncio.sleep(pause_interval)  # Đợi 1 giờ trước khi gửi tin nhắn tiếp theo

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

@bot.command()
async def wish(ctx, *, content):
    # Kiểm tra xem nội dung đã tồn tại trong tệp hay chưa
    if not is_content_in_file(content, 'wish_harem.txt'):
        # Ghi nội dung vào tệp wish_harem.txt
        with open('wish_harem.txt', 'a') as file:
            file.write(f"{content}\n")

        await ctx.send(f"Đã thêm: **'{content}'**.")
    else:
        await ctx.send(f"Nội dung: **'{content}'** đã có.")

# Hàm kiểm tra xem nội dung có tồn tại trong tệp hay không
def is_content_in_file(content, file_path):
    with open(file_path, 'r') as file:
        return content.lower() in file.read().lower()

@bot.command()
async def wishremove(ctx, *, content):
    # Đọc danh sách từ tệp wish_harem.txt
    with open('wish_harem.txt', 'r') as file:
        lines = file.readlines()

    # Loại bỏ nội dung khỏi danh sách
    removed = False
    with open('wish_harem.txt', 'w') as file:
        for line in lines:
            if line.strip().lower() == content.lower():
                removed = True
            else:
                file.write(line)

    if removed:
        await ctx.send(f"Đã xoá: **'{content}'**.")
    else:
        await ctx.send(f"**'{content}'** không tồn tại.")


@bot.command()
async def wishs(ctx, *, content):
    # Kiểm tra xem nội dung đã tồn tại trong tệp hay chưa
    if not is_content_in_file(content, 'wish_series.txt'):
        # Ghi nội dung vào tệp wish_series.txt
        with open('wish_series.txt', 'a') as file:
            file.write(f"{content}\n")

        await ctx.send(f"Đã thêm anime: **'{content}'**.")
    else:
        await ctx.send(f"Nội dung anime: **'{content}'** đã có.")

# Hàm kiểm tra xem nội dung có tồn tại trong tệp hay không
def is_content_in_file(content, file_path):
    with open(file_path, 'r') as file:
        return content.lower() in file.read().lower()

@bot.command()
async def wishremoves(ctx, *, content):
    # Đọc danh sách từ tệp wish_series.txt
    with open('wish_series.txt', 'r') as file:
        lines = file.readlines()

    # Loại bỏ nội dung khỏi danh sách
    removed = False
    with open('wish_series.txt', 'w') as file:
        for line in lines:
            if line.strip().lower() == content.lower():
                removed = True
            else:
                file.write(line)

    if removed:
        await ctx.send(f"Đã xoá animne: **'{content}'**.")
    else:
        await ctx.send(f"Anime **'{content}'** không tồn tại.")

@bot.event
async def on_embed_message(message):
    # Kiểm tra nếu có embed
    if message.embeds and message.channel.id == YOUR_SPECIFIC_CHANNEL_ID:
        with open('wish_series.txt', 'r') as file:
            danh_sach_tu = [line.strip().lower() for line in file]

        for embed in message.embeds:
            embed_content = embed.description.lower() if embed.description else ""
            danh_sach_tu_lower = [tu.lower() for tu in danh_sach_tu]
            
            # Kiểm tra các từ trong danh sách
            for tu in danh_sach_tu_lower:
                if tu in embed_content:
                    await message.channel.send(f"<a:Verify:980814232599793705> Anime: **{tu}** nè Soníc.")
                    await message.add_reaction("❤")

@bot.event
async def on_embed_message_name(message):
    # Kiểm tra nếu có embed
    if message.embeds and message.channel.id == YOUR_SPECIFIC_CHANNEL_ID:
        with open('wish_harem.txt', 'r') as file:
            danh_sach_tu = [line.strip().lower() for line in file]

        for embed in message.embeds:
            if embed.author:
                author_name = embed.author.name.lower() if embed.author.name else ""

                # So sánh thông tin tác giả với danh sách tên anime
                if author_name in danh_sach_tu:
                    # Thực hiện hành động nếu thông tin tác giả khớp
                    #await message.channel.send(f"<a:Verify:980814232599793705> Claim giúp anh nhân vật: **{author_name}** với đi nè.....")
                    await message.add_reaction("📌")

@bot.event
async def on_text_message(message):
   if message.author == bot.user:
      return
   await bot.process_commands(message)
   
   words = message.content.lower().split()
#Thả emoji khi có chứa từ Tân trong tin nhắn.
   if any(word in ["tân"] for word in words):
      await message.add_reaction("<:seen:1136725697314959410>")

#Thả emoji khi được reply tin nhắn.
   if message.reference:
      replied_message = await message.channel.fetch_message(message.reference.message_id)
      if replied_message.author == bot.user:
         await message.add_reaction("<:seen:1136725697314959410>")

# Đăng ký sự kiện cho các event
bot.add_listener(on_embed_message_name, 'on_message')
bot.add_listener(on_text_message, 'on_message')
bot.add_listener(on_embed_message, 'on_message')

bot.run(token)
