import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())

@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
	await interaction.send("command passed! qume1i best")

bot.run("BOT TOKEN HERE")
