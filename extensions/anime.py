import discord
from discord.ext import commands
from utils import kitsuapi
from utils import randomness
from utils import date

class AttrDict: # fine mart
    def __init__(self, data: dict):
        self.data = data

    def __getattr__(self, key: str):
        return self.data[key]

class Anime:
    def __init__(self, bot):
        self.bot = bot
        self.kitsu = kitsuapi.KitsuAPI()

    @commands.command(aliases=['ksearch', 'anime'])
    async def search(self, ctx, *, name:str):
        data = await self.kitsu.get_anime(name)
        if len(data) == 0:
            return await ctx.send(':no_entry_sign: Not found.')
        anime = AttrDict(data[0])
        attrs = AttrDict(anime.attributes)
        embed = discord.Embed(color=randomness.random_colour())
        embed.title = f'{attrs.titles["ja_jp"]} ({attrs.titles["en_jp"]})'
        if not attrs.nsfw:
            embed.set_thumbnail(url=attrs.posterImage['medium'])
        embed.description = attrs.synopsis
        embed.url = f'https://kitsu.io/anime/{attrs.slug}'
        embed.set_footer(text='Powered by kitsu.io')
        embed.add_field(name='Started On', value=date.parse_date(attrs.startDate))
        embed.add_field(name='Ended On', value='Ongoing' if attrs.status != 'finished' else date.parse_date(attrs.endDate))
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Anime(bot))
