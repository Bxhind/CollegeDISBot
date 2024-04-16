import disnake


from assets import buttons, embeds
from disnake.ui import button
from disnake.ext import commands
from db import DataBase

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='showall', description="Show table with customers of digital dealer service")
    @commands.is_owner()
    async def show_customer(self, inter: disnake.ApplicationCommandInteraction):
        embed = embeds.Main_embed
        view = buttons.MainButtons(bot= self.bot)
        await inter.response.defer()
        await inter.send("Here is your button!", view=view, embed= embed)

def setup(bot):
    bot.add_cog(Commands(bot))