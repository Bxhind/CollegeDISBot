import disnake
from db import DataBase

class MainButtons():
    def __init__(self, bot):
        self.bot = bot
    super.__init__(timeout= None)
    
    @disnake.ui.Button(
        label = "Show Customers",
        style= disnake.ButtonStyle.blurple,
        emoji= "📺")
    async def show_customers(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        DataBase.fetch_customer()