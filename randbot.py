import discord
import commands as com
import messages as mes
import tokens as tok
from discord.ext import tasks
import datetime

client = discord.Client()


# Information Embed message when bot joins the server for the first time.
@client.event
async def on_guild_join(guild):
    await guild.text_channels[0].send(embed=mes.guild_join_message())


# Information to console when bot successfully logs in the server.
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Reactions to message commands.
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('?random'):
        await com.random_command(message)
    elif message.content.startswith('?8ball'):
        await com.eightball_command(message)
    elif message.content.startswith('?yesno'):
        await com.yesno_command(message)
    elif message.content.startswith('?list'):
        await com.list_command(client, message)
    elif message.content.startswith('?delete'):
        await com.delete_command(message)
    elif message.content.startswith('?commands'):
        await com.commands_command(message)


# daily DB clean loop
@tasks.loop(hours=24)
async def cleandb():
    await com.clean()

    print("DB cleaned " + datetime.datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'))

cleandb.start()

# Connects the client using Discord bot token
client.run(tok.discord_token)
