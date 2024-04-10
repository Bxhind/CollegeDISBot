import disnake

from disnake.ui import button
from db import DataBase


class MainButtons():
    def __init__(self, bot):
        self.bot = bot
    
    
    @button(
        label = "Show Customers",
        style= disnake.ButtonStyle.blurple,
        emoji= "📺")
    async def show_customers(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.response.defer()
        await DataBase.fetch_customer()