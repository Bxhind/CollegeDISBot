from typing import Any
import disnake
import datetime
from disnake import Embed
from disnake.utils import MISSING

Main_embed = Embed(
    title= "Car Dealer DataBase",
    timestamp= datetime.datetime.now(),
    )
Main_embed.add_field(
    name= "Here is all communicate with database",
    value = ""
    )