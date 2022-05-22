from discord.ext import commands

class Reactions(commands.Cog):
    """Work with Reactions""" # descrição que o cog faz

    def __init__(self, bot):
        self.bot = bot # passar o bot pra cá

#bot.events => 
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user): # toda vez que um reação for ativada // adicionou self pq é orientação a objetos
        print(reaction.emoji) # pra fazer o emoji aparecer no meu console
        if reaction.emoji == "👍":
            role = user.guild.get_role(976847404622020658) # guild pegar o servidor que o usario está
            await user.add_roles(role) # adicionar o cargo "role" ao usuario
        elif reaction.emoji == "👎":
            role = user.guild.get_role(976847473068875846) # guild pegar o servidor que o usario está
            await user.add_roles(role) # adicionar o cargo "role" ao usuario



def setup(bot):
    bot.add_cog(Reactions(bot)) # pro talks interagir com o bot