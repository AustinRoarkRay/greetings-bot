import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

token = str(os.environ.get("BOT_TOKEN"))
server_id = str(os.environ.get("SERVER_ID"))

welcome_channel_id = str(os.environ.get("WELCOME_CHANNEL_ID"))

auto_role_id = str(os.environ.get("AUTO_ROLE_ID"))
bot_role_id = str(os.environ.get("BOT_ROLE_ID"))


Client = discord.Client()
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
	await bot.wait_until_ready()
	print (bot.user.name + " is ready")
	print ("ID: " + bot.user.id)
	
@bot.event
async def on_message(message):
	if message.content == "hellomates":
		for role in bot.get_server(server_id).roles:
			print("{0} ({1})".format(role.name, role.id))

@bot.event
async def on_member_join(member):
	
	welcome_channel_object = bot.get_server(server_id).get_channel(welcome_channel_id)
	
	for role in bot.get_server(server_id).roles:
		if role.id == auto_role_id:
			auto_role_object = role
		elif role.id == bot_role_id:
			bot_role_objet = role
	
	
	
	await bot.send_message(welcome_channel_object, "Welcome {0} to Supreme'Gaming~ Where you'll be taught the ways of gaming till, infinity and beyond!".format(member.mention))
	
	if member.bot:
		await bot.add_roles(member, bot_role_object)
	else:
		await bot.add_roles(member, auto_role_object)

@bot.event
async def on_member_remove(member):

	welcome_channel_object = bot.get_server(server_id).get_channel(welcome_channel_id)
	
	await bot.send_message(welcome_channel_object, "Goodbye {0} We've taught you well!".format(member.mention))


	
bot.run(token)
