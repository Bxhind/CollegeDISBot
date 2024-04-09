import disnake
import json

from disnake.ext import commands, tasks
from assets import buttons

class Commands:
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.is_owner()
    @commands.slash_command(name= 'Show Customer', description= "Show table with customers of digital dealer service")
    async def show_customer(self, inter: disnake.MessageInteraction):
        view = buttons.MainButtons
        await inter.response.defer()
        await inter.send("Here is your button!", view= view)
        

def setup(bot):
    bot.add_cog(Commands(bot))