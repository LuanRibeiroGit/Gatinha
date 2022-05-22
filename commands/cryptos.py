import requests

from discord.ext import commands

class Cripto(commands.Cog):
    """Works with Cryptocurrency""" # descrição que o cog faz

    def __init__(self, bot):
        self.bot = bot # passar o bot pra cá

    @commands.command()
    async def binance(self, ctx, coin, base):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}") #upper deixar em maiusculo

            data = response.json()
            price = data.get("price")

            if price: #se o bot achar um preço
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else:
                await ctx.send(f"O par {coin}/{base} é inválido")
        except Exception as error:
            await ctx.send("Ops ... Deu algum erro")
            print(error)

def setup(bot):
    bot.add_cog(Cripto(bot)) # pro talks interagir com o bot