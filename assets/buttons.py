import disnake

from disnake.ui import button
from db import DataBase


class MainButtons(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout= None)
        
    
    @button(
        label="Show Customers",
        style=disnake.ButtonStyle.blurple,
        emoji="📺"
    )
    async def show_customers(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.response.defer()
        fetch_res = DataBase.fetch_customer(self)
        await inter.send(f"{fetch_res}")