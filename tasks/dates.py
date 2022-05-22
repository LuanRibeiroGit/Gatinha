import datetime

from discord.ext import commands, tasks


class Dates(commands.Cog):
    """Work with Dates""" # descrição que o cog faz

    def __init__(self, bot):
        self.bot = bot # passar o bot pra cá

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()# ele vai ficar quando este cog estiver ligado

    @tasks.loop(hours=10)
    async def current_time(self):
        now = datetime.datetime.now() # colocar parenteses quando for uma funçao

        now = now.strftime("%d/%m/%Y às  %H:%M:%S")# string formate o time

        channel = self.bot.get_channel(976230646617899080)

        await channel.send("Data atual: " + now)
    


def setup(bot):
    bot.add_cog(Dates(bot)) # pro talks interagir com o bot