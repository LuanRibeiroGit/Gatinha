from asyncio import all_tasks
from discord.ext import commands
import discord

class Talks(commands.Cog):
    """Talks with user""" # descrição que o cog faz

    def __init__(self, bot):
        self.bot = bot # passar o bot pra cá

    #bot.command => pq ele é um comando
    @commands.command(name = "oi") # ira aparecer no help
    async def send_hello(ctx): # CTX onde foi enviado, qm autor
        name = ctx.author.name # o nome da pessoa que digitou o comando

        response = "Olá, " + name

        await ctx.send(response)

    @commands.command(name = "segredo") #mandar na DM
    async def secret(self, ctx):
        try:
            await ctx.author.send("Testando 123")
            await ctx.author.send("A Gatinha é foda")
            await ctx.author.send("")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")


def setup(bot):
    bot.add_cog(Talks(bot)) # pro talks interagir com o bot