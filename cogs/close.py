import discord.utils
from discord import Message
from discord.ext.commands import Bot, Cog, Context, command


class Close(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def close(self, ctx: Context) -> None:
        guild: discord.Guild = ctx.guild

        alpha_category: discord.channel.CategoryChannel = discord.utils.get(guild.categories, name="alpha-team")
        beta_category: discord.channel.CategoryChannel = discord.utils.get(guild.categories, name="beta-team")
        alpha_text: discord.channel.TextChannel = discord.utils.get(guild.text_channels, name=f"alpha-text")
        beta_text: discord.channel.TextChannel = discord.utils.get(guild.text_channels, name=f"beta-text")
        alpha_voice: discord.channel.VoiceChannel = discord.utils.get(guild.voice_channels, name=f"alpha-VC")
        beta_voice: discord.channel.VoiceChannel = discord.utils.get(guild.voice_channels, name=f"beta-VC")
        alpha_role: discord.Role = discord.utils.get(guild.roles, name=f"alpha-team")
        beta_role: discord.Role = discord.utils.get(guild.roles, name=f"beta-team")

        await guild.me.add_roles(alpha_role)
        await guild.me.add_roles(beta_role)

        if alpha_text is not None:
            await alpha_text.delete()

        if beta_text is not None:
            await beta_text.delete()

        if alpha_voice is not None:
            await alpha_voice.delete()

        if beta_voice is not None:
            await beta_voice.delete()

        if alpha_category is not None:
            await alpha_category.delete()

        if beta_category is not None:
            await beta_category.delete()

        if alpha_role is not None:
            await alpha_role.delete()

        if beta_role is not None:
            await beta_role.delete()


def setup(bot: Bot) -> None:
    bot.add_cog(Close(bot))
