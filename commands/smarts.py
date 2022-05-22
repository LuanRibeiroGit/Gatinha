from discord.ext import commands

class Smarts(commands.Cog):
    """A lot of Smarts Commands""" # descrição que o cog faz

    def __init__(self, bot):
        self.bot = bot # passar o bot pra cá

    @commands.command(name = "calc")
    async def calculate_expression(self, ctx, *expression): # ctx sempre na frente pro discord entender que é uma expressão // * pega todos os argumentos e fala que é uma coisa só
        expression = "".join(expression) #
        response = eval(expression) # pegar o valor //tomar cuidado com o eval, se não as pessoas iram poder invadir o banco de dados
        
        await ctx.send("A resposta é: "+ str(response)) # STR pra transformar em string

def setup(bot):
    bot.add_cog(Smarts(bot)) # pro talks interagir com o bot