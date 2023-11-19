import discord
from discord.ext import commands



from config import CONFIG

bot = commands.Bot(command_prefix='.',intents=discord.Intents.all())


@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)

bot.run(CONFIG['token'])
