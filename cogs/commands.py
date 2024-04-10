import disnake
import json

from db import DataBase
from disnake.ext import commands, tasks
from assets import buttons

class Commands(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    
    @commands.slash_command(name= 'showall', description= "Show table with customers of digital dealer service")
    @commands.is_owner()
    async def show_customer(self, inter: disnake.ApplicationCommandInteraction):
        view = buttons.MainButtons(bot = self.bot)
        await inter.response.defer()
        await inter.send("Here is your button!", view= view)
    
        

def setup(bot):
    bot.add_cog(Commands(bot))