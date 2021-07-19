from discord import Message
import discord
from discord.ext.commands import Bot, Cog, Context, command
import random


class Team(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def team(self, ctx: Context) -> None:
        guild = ctx.guild
        try:

            member: list = [members for members in ctx.author.voice.channel.members]
            # members_name = [members.name for members in ctx.author.voice.channel.members]
            # member_per_teams: int = round(len(member)/2)

            random.shuffle(member)
            alpha_members = member[0::2]
            beta_members = member[1::2]

            alpha_members_name = [alpha_members.name for alpha_members in alpha_members]
            beta_members_name = [beta_members.name for beta_members in beta_members]

            await ctx.send(f"AlphaTeam:{alpha_members_name}")
            await ctx.send(f"BetaTeam:{beta_members_name}")

            for alpha_member in alpha_members:
                alpha_role: discord.Role = discord.utils.get(guild.roles, name="alpha-team")
                await alpha_member.add_roles(alpha_role)

            for beta_member in beta_members:
                beta_role: discord.Role = discord.utils.get(guild.roles, name="beta-team")
                await beta_member.add_roles(beta_role)

        except AttributeError as ae:
            await ctx.send(f"エラー:VCに接続していない，もしくはsetupコマンドが正常に動作していないとかで振り分けが完了しませんでした。\n"
                           f"エラー内容:{ae}")


def setup(bot: Bot) -> None:
    bot.add_cog(Team(bot))
