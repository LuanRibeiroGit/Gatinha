import random
import discord
from discord.ext import commands


class Images(commands.Cog):
    """Works with Images""" # descrição que o cog faz

    def __init__(self, bot):
        self.bot = bot # passar o bot pra cá

        
    @commands.command(name = "gif1")
    async def get_Kaidou(self, ctx): # carregar uma imagem random
        url_image = "https://c.tenor.com/arj97lLhyvAAAAAC/one-piece-kaido.gif"

        embed_image = discord.Embed(
            title = "Resultado da busca de imagem",
            description = "Ps a busca é totalmente aleatoria",
         color = 0x0000FF,
        )

        embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
        embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

        embed_image.add_field(name = "API", value = "Usamos a API do https://picsum.photos")
        embed_image.add_field(name = "Parâmetros", value = "{largura}/{altura}")

        embed_image.add_field(name = "Exemplo", value = url_image, inline = False) # inline false pra ele ficar sozinho na linha

        embed_image.set_image(url = url_image) # pegar a variavel la em cima

        await ctx.send(embed = embed_image)
    


    @commands.command(name = "gif")
    async def get_Luffy(self, ctx): # carregar uma imagem random
        url_image = "https://i.imgur.com/kgnnEFy.gif"

        embed_image = discord.Embed(
            title = "Resultado da busca de imagem",
            description = "Ps a busca é totalmente aleatoria",
            color = 0x0000FF,
        )

        embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
        embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

        embed_image.add_field(name = "API", value = "Usamos a API do https://i.imgur.com")
        embed_image.add_field(name = "Parâmetros", value = "{largura}/{altura}")

        embed_image.add_field(name = "Exemplo", value = url_image, inline = False) # inline false pra ele ficar sozinho na linha

        embed_image.set_image(url = url_image) # pegar a variavel la em cima

        await ctx.send(embed = embed_image)

    @commands.command(name = "onepiece")
    async def get_random(self, ctx):
        variavel = random.randint(1, 10)
        if variavel == 1:
            url_image = "https://thumbs.gfycat.com/SlimElementaryBrocketdeer-size_restricted.gif"
            

            embed_image = discord.Embed(
                title = "Nome",
                description = "Edward Newgate - Barba Branca",
                color = 0x9400D3,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)
            

            #embed_image.add_field(name = "Nome", value = "Barba Branca")
            embed_image.add_field(name = "Akuma no Mi", value = "Gura Gura no Mi 🍇")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)

        
        elif variavel == 2:
            url_image = "https://pa1.narvii.com/7867/37ff2690ba34cb1f9909468d808a010892357a45r1-500-260_hq.gif"

            embed_image = discord.Embed(
                title = "Nome",
                description = "Marshall D. Teach - Barba Negra",
                color = 0x9400D3,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

            #embed_image.add_field(name = "Nome", value = "Barba Negra")
            embed_image.add_field(name = "Akuma no Mi", value = "Yami Yami no Mi 🍇\nGura Gura no Mi 🍇")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)
        

        elif variavel == 3:
            url_image = "https://i.pinimg.com/originals/7a/c8/df/7ac8df62ddc4f2d61e31c4f50156773a.gif"

            embed_image = discord.Embed(
                title = "Nome",
                description = "Charlotte Linlin - Big Mon",
                color = 0x9400D3,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

            #embed_image.add_field(name = "Nome", value = "Big Mom")
            embed_image.add_field(name = "Akuma no Mi", value = "Soro Soro no Mi 🍇")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)


        elif variavel == 4:
            url_image = "https://assets.zyrosite.com//YD0O1Xn6b9ipNMpQ/img-AMqP26M0GGukBrjz.gif"

            embed_image = discord.Embed(
                title = "Nome",
                description = "Gol D. Roger",
                color = 0xFFD700,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

            #embed_image.add_field(name = "Nome", value = "Gold Roger")
            embed_image.add_field(name = "Akuma no Mi", value = "DESCONHECIDA 👻")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)


        elif variavel == 5:
            url_image = "https://pa1.narvii.com/6807/eeb33a0da80aea01ed49b2ddd29c34d8473651b7_hq.gif"

            embed_image = discord.Embed(
                title = "Nome",
                description = "Kaido",
                color = 0x9400D3,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

            #embed_image.add_field(name = "Nome", value = "Kaidou")
            embed_image.add_field(name = "Akuma no Mi", value = "Uo Uo no Mi 🍇")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)


        elif variavel == 6:
            url_image = "https://i.pinimg.com/originals/1a/ed/97/1aed9753df2351b790f08b49055d66ca.gif"

            embed_image = discord.Embed(
                title = "Nome",
                description = "Monkey D. Luffy",
                color = 0xFFD700,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

            #embed_image.add_field(name = "Nome", value = "Luffy")
            embed_image.add_field(name = "Akuma no Mi", value = "Gomo Gomo no Mi 🍇")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)


        elif variavel == 7:
            url_image = "https://i.makeagif.com/media/7-31-2017/LAe8uI.gif"

            embed_image = discord.Embed(
                title = "Nome",
                description = "Monkey D. Dragon",
                color = 0x006400,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

            #embed_image.add_field(name = "Nome", value = "Monkey D. Dragon")
            embed_image.add_field(name = "Akuma no Mi", value = "DESCONHECIDA 👻")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)


        elif variavel == 8:
            url_image = "https://i.pinimg.com/originals/89/fb/87/89fb87baf0db7f0165930bac6f210a9a.gif"

            embed_image = discord.Embed(
                title = "Nome",
                description = "Sanji",
                color = 0x0000FF,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

            #embed_image.add_field(name = "Nome", value = "Sanji")
            embed_image.add_field(name = "Akuma no Mi", value = "Habilidades Fisicas 🤺")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)


        elif variavel == 9:
            url_image = "https://i.pinimg.com/originals/8a/73/3c/8a733c10b1454b0d31d8a6f41c53eec5.gif"

            embed_image = discord.Embed(
                title = "Nome",
                description = "Shanks",
                color = 0x9400D3,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

            #embed_image.add_field(name = "Nome", value = "Shanks")
            embed_image.add_field(name = "Akuma no Mi", value = "Habilidades Fisicas 🤺")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)


        elif variavel == 10:
            url_image = "https://c.tenor.com/cOhgxKZrGqQAAAAC/zoro-one-piece.gif"

            embed_image = discord.Embed(
                title = "Nome",
                description = "Roronoa Zoro",
                color = 0x0000FF,
            )

            embed_image.set_thumbnail(url="https://media1.giphy.com/media/6KKKVerzrhjRrClNKt/giphy.gif?cid=790b76119ed268a8cfc5af1fcefed14567bc5b6d1376eb03&rid=giphy.gif&ct=s")
            embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url) # pegar o icone que tem no bot
            embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar_url)

            #embed_image.add_field(name = "Nome", value = "Zoro")
            embed_image.add_field(name = "Akuma no Mi", value = "Habilidades Fisicas 🤺")
            embed_image.add_field(name = "Raridade", value = "⭐⭐⭐⭐⭐")
            embed_image.add_field(name = "Vida", value = "❤️❤️❤️❤️❤️")
            embed_image.add_field(name = "Defesa", value = "🛡️🛡️🛡️🛡️🛡️")
            embed_image.add_field(name = "Ataque", value = "⚔️⚔️⚔️⚔️⚔️")
            embed_image.add_field(name = "Magia", value = "💧💧💧💧💧")
            # inline false pra ele ficar sozinho na linha

            embed_image.set_image(url = url_image) # pegar a variavel la em cima

            await ctx.send(embed = embed_image)

def setup(bot):
    bot.add_cog(Images(bot)) # pro talks interagir com o bot
