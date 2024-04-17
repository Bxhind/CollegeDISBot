import disnake

from disnake.ui import button
from assets import modals
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
        fetch_res = await DataBase.fetch_customer(self)
        customers_info = "\n".join([str(customer) for customer in fetch_res])
        await inter.send(f"Client info: \n{customers_info}")
        
        
    @button(
        label= "Add Someone",
        style = disnake.ButtonStyle.danger,
        emoji= "⚠️"
    )
    async def add_customer(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        modal = modals.ModalAdd(bot= self.bot)
        await inter.response.send_modal(modal= modal)
        
        
    @button(
        label= "Other...",
        style= disnake.ButtonStyle.green,
        emoji= "🔅"
    )
    async def other_option(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        select = modals.Selection(bot= self.bot)
        view = disnake.ui.View()
        view.add_item(modals.Selection(bot= self.bot))
        await inter.send(view= view)
