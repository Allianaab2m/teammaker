from discord import Message
from discord.ext.commands import Bot, Cog, Context, command
import random


class Team(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def team(self, ctx: Context) -> None:



def setup(bot: Bot) -> None:
    bot.add_cog(Team(bot))
