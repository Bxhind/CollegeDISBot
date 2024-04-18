import disnake

from disnake.ui.action_row import ModalUIComponent
from disnake.utils import MISSING
from db import DataBase
from disnake import TextInputStyle
import buttons


class ModalAdd(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label= "Name",
                placeholder= "Input name here",
                custom_id = "name",
                style = TextInputStyle.short,
                max_length= 50
            ),
            disnake.ui.TextInput(
                label= "Surname",
                placeholder= "Input surname here",
                custom_id= "surname",
                style= TextInputStyle.short,
                max_length= 50
            ),
            disnake.ui.TextInput(
                label= "Phone Number",
                placeholder= "Input phone number here",
                custom_id= "phone",
                style= TextInputStyle.short,
                max_length= 13
            ),
            disnake.ui.TextInput(
                label = "Car ID",
                placeholder= "Input number of car_id here (from 8 to 10)[WIP]",
                custom_id= 'carid',
                style= TextInputStyle.short,
                max_length= 4
            )
        ]
        super().__init__(
            title = "Insert a Customer",
            components= components,
            custom_id= "insertmodal",
            timeout= 300
        )
    
    
    async def callback(self, inter: disnake.ModalInteraction) -> None:
        await inter.response.defer()
        name = inter.text_values['name']
        surname = inter.text_values['surname']
        phone = inter.text_values['phone']
        carid = inter.text_values['carid']
        try:
            await DataBase.add_customer(name, surname, phone, carid)
            await inter.send("Customer added successfully!")
        except Exception as e:
            await inter.send("Something gone wrong. Ohh shit, I'm sorry")
            print(e)
        return await super().callback(inter)

class UpdateModal(disnake.ui.Modal):
    def __init__(self, bot) -> None:
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label= "Name",
                placeholder= "Set new customer name",
                custom_id= "name",
                style= disnake.TextInputStyle.short,
                max_length= 40
            ),
            disnake.ui.TextInput(
                label = "Surname",
                placeholder= "Set new customer surname",
                custom_id= "surname",
                style= disnake.TextInputStyle.short,
                max_length= 40
            ),
            disnake.ui.TextInput(
                label= "Phone Number",
                placeholder= "Set new customer phone",
                custom_id= "phone",
                style= TextInputStyle.short,
                max_length= 13
            ),
            disnake.ui.TextInput(
                label = "Car ID",
                placeholder= "Set new customer carid",
                custom_id= 'carid',
                style= TextInputStyle.short,
                max_length= 4
            )
        ]
        super().__init__(
            title= "Updating",
            components=components,
            custom_id="update",
            timeout= 300)
    
    
    async def callback(self, inter: disnake.ModalInteraction) -> None:
        name = inter.text_values['name']
        surname = inter.text_values['surname']
        phone = inter.text_values['phone']
        carid = inter.text_values['carid']
        
        return await super().callback(inter)

class searchUpdModal(disnake.ui.Modal):
    def __init__(self, bot) -> None:
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label= "Select ID",
                placeholder= "insert here an ID",
                custom_id= "id",
                style= disnake.TextInputStyle.paragraph,
                max_length= 3
            ),
            disnake.ui.TextInput(
                label= "Select Name",
                placeholder= "insert here a name",
                custom_id = "name",
                style= disnake.TextInputStyle.short,
                max_length= 40
            )
        ]
        super().__init__(
            title= "Select to update",
            components= components,
            custom_id = "updatemod",
            timeot = 300
        )
    
    
    async def callback(self, inter: disnake.ModalInteraction) -> None:
        id = inter.text_values['id']
        name = inter.text_values['name']
        try:
            finder = await DataBase.update_search(id, name)
            if finder:
                view = buttons.UpdateButton(bot = self.bot)
                await inter.send("Customer found \nPlease, use button to update", view= view)
            else:
                pass
        except Exception as e:
            await inter.send(f"Incorrect error: \nerror type: {e}")
        return await super().callback(inter)
        
class QueryModal(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot
        components = [
            disnake.ui.TextInput(
                label= 'Insert a query',
                placeholder= "For example [SELECT * FROM CUSTOMERS]",
                custom_id= 'query',
                style= disnake.TextInputStyle.paragraph,
                max_length= 2000
            )
        ]
        super().__init__(
            title= "Insert a Query",
            components= components,
            timeout= 500,
            custom_id= "querymod"
        )

    
    async def callback(self, inter: disnake.ModalInteraction) -> None:
        await inter.response.defer()
        query = inter.text_values['query']
        try:
            query_res = await DataBase.query_cast(self, query)
            if query_res:
                result_str = "\n".join([str(row) for row in query_res])
                await inter.send(f"Query complete! Result:\n{result_str}")
            else:
                await inter.send("Query completed successfully")
        except Exception as e:
            await inter.send("Something went wrong: "+str(e))
        return await super().callback(inter)


class Selection(disnake.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        
        options = [
            disnake.SelectOption(
                label= "Update",
                value= "update"
                ),
            disnake.SelectOption(
                label= "Delete",
                value= "delete"
                ),
            disnake.SelectOption(
                label= "Custom Query",
                value= "custom"
                )
        ]
        super().__init__(
            placeholder="Choose option",
            options= options,
            min_values=1,
            max_values= 1
        )
        
        
    async def callback(self, inter:disnake.MessageInteraction):
        value = inter.data['values'][0]
        if value == 'update':
            pass
        if value == 'delete':
            pass
        if value == "custom":
            modal = QueryModal(bot = self.bot)
            await inter.response.send_modal(modal= modal)
                
                