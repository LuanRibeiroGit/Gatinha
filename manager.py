from calendar import c
from http import client
import random
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound # importei meus erros identificados
from discord.ext import commands



class Manager(commands.Cog):
    """Manager the bot""" # descrição que o cog faz

    def __init__(self, bot):
        self.bot = bot # passar o bot pra cá

    @commands.Cog.listener() # toda vez que...
    async def on_ready(self):
        print(f"Estou pronto, estou conectado como bot {self.bot.user}") # toda vez que o bot estiver on, exibira está msg... F = pra funcionar o bot.user


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user: # se for msg do meu bot, ele retornara
            return;

        var = random.randint(1, 2)
        if "palavrão" in message.content:
            if var == 1:
                await message.channel.send(f"Por favor <@{message.author.id}>, não ofenda os membros") # se a pessoa mandar um palavrão ira aparacer
                await message.delete() # caso for um palavrão, a msg sera apagada
            if var == 2:
                await message.channel.send(f"olha essa boca <@{message.author.id}>, se não eu te mando de volta pra casa") # se a pessoa mandar um palavrão ira aparacer
                await message.delete() # caso for um palavrão, a msg sera apagada
        #await self.bot.process_commands(message) # para ele processar todas as msgns enviadas

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send(f"Por favor <@{ctx.author.id}>, enviar todos os Argumentos,\nDigite h!help para ver os parametros de cada comando")
        elif isinstance(error,CommandNotFound):
            await ctx.send("A Gatinha não reconhece este comando. Diooos mioooo! Digite h!help para ver todos os comandos")
        else:
            raise error




def setup(bot):
    bot.add_cog(Manager(bot)) # pro talks interagir com o bot