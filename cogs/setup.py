import discord.utils
import discord
from discord import Message
from discord.ext.commands import Bot, Cog, Context, command


class Setup(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def setup(self, ctx: Context) -> None:
        guild: discord.Guild = ctx.guild

        alpha_role: discord.Role = discord.utils.get(guild.roles, name=f"alpha-team")
        beta_role: discord.Role = discord.utils.get(guild.roles, name=f"beta-team")

        if alpha_role is None:
            alpha_role = await guild.create_role(name=f"alpha-team")
        else:
            await ctx.send(f"alpha-role has been created.")

        if beta_role is None:
            beta_role = await guild.create_role(name=f"beta-team")
        else:
            await ctx.send(f"beta-role has been created.")

        alpha_category: discord.channel.CategoryChannel = discord.utils.get(guild.categories, name="alpha-team")
        beta_category: discord.channel.CategoryChannel = discord.utils.get(guild.categories, name="beta-team")

        if alpha_category is None:
            overwrites = {
                alpha_role: discord.PermissionOverwrite(read_messages=True),
                guild.me:  discord.PermissionOverwrite(read_messages=True),
                guild.default_role: discord.PermissionOverwrite(read_messages=False)
            }

            alpha_category = await guild.create_category(name="alpha-team", overwrites=overwrites)
        else:
            await ctx.send("alpha-category has been created.")

        if beta_category is None:
            overwrites = {
                beta_role: discord.PermissionOverwrite(read_messages=True),
                guild.me: discord.PermissionOverwrite(read_messages=True),
                guild.default_role: discord.PermissionOverwrite(read_messages=False)
            }

            beta_category = await guild.create_category(name="beta-team", overwrites=overwrites)
        else:
            await ctx.send("beta-category has been created.")

        alpha_text: discord.channel.TextChannel = discord.utils.get(guild.text_channels, name=f"alpha-text")
        beta_text: discord.channel.TextChannel = discord.utils.get(guild.text_channels, name=f"beta-text")
        alpha_voice: discord.channel.VoiceChannel = discord.utils.get(guild.voice_channels, name=f"alpha-VC")
        beta_voice: discord.channel.VoiceChannel = discord.utils.get(guild.voice_channels, name=f"beta-VC")

        if alpha_text is None:
            await alpha_category.create_text_channel("alpha-text")
        else:
            await ctx.send(f"alpha-text has been created.")

        if beta_text is None:
            await beta_category.create_text_channel("beta-text")
        else:
            await ctx.send(f"beta-text has been created.")

        if alpha_voice is None:
            await alpha_category.create_voice_channel("alpha-VC")
        else:
            await ctx.send(f"alpha-VC has been created.")

        if beta_voice is None:
            await beta_category.create_voice_channel("beta-VC")
        else:
            await ctx.send(f"beta-VC has been created.")


def setup(bot: Bot) -> None:
    bot.add_cog(Setup(bot))
