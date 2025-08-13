import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

#MENSAJE DE INICO DE SESION

@bot.event
async def on_ready():
    print(f'Hemos iniciado como : {bot.user}')

#COMANDO DEL BOT CLASIFICADOR

@bot.command()
async def clasificar(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre = archivo.filename
            await archivo.save(nombre)
            await ctx.send(f"La imagen {nombre} se ha guardado correctamente.")

            try:
                clase = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=nombre)

                if clase[0] == "steve":
                    await ctx.send("este personaje de videojuegos se llama steve proviene de Minecraft un videojuego creado el 17 de mayo de 2009 por la compania Mojang Studios, es un juego de construccion y supervivencia en un mundo abierto.")
                elif clase[0] == "MarioMario":
                    await ctx.send("este personaje de videojuegos se llama Mario Mario proviene de Super Mario Bros un videojuego creado el 13 de septiembre de 1985 por la compania Nintendo, es un juego de plataformas en el que el jugador controla a Mario para rescatar a la princesa Peach.")
                elif clase[0] == "Sonic":
                    await ctx.send("este personaje de videojuegos se llama Sonic proviene de Sonic the Hedgehog un videojuego creado el 23 de junio de 1991 por la compania Sega, es un juego de plataformas en el que el jugador controla a Sonic para detener al malvado Dr. Robotnik.")
                elif clase[0] == "MasterChief":
                    await ctx.send("este personaje de videojuegos se llama Master Chief proviene de Halo un videojuego creado el 15 de noviembre de 2001 por la compania Bungie Studios, es un juego de disparos en primera persona que sigue las aventuras del supersoldado Master Chief.")
                elif clase[0] == "Link":
                    await ctx.send("este personaje de videojuegos se llama Link proviene de The Legend of Zelda un videojuego creado el 21 de febrero de 1986 por Nintendo, es un juego de aventuras donde Link debe rescatar a la princesa Zelda y derrotar a Ganon.")
                elif clase[0] == "Pikachu":
                    await ctx.send("este personaje de videojuegos es Pikachu un Pokémon de tipo eléctrico proviene de la franquicia Pokémon creada el 27 de febrero de 1996 por Game Freak y Nintendo, es uno de los Pokémon más reconocidos y es la mascota oficial de la saga.")
                elif clase[0] == "LaraCroft":
                    await ctx.send("este personaje de videojuegos es Lara Croft la protagonista de Tomb Raider el primer juego fue lanzado el 25 de octubre de 1996 por Core Design y Eidos Interactive, es un juego de aventuras y exploración con elementos de acción y plataformas.")
                elif clase[0] == "Kratos":
                    await ctx.send("este personaje de videojuegos es Kratos protagonista de la saga God of War el primer juego se lanzó el 22 de marzo de 2005 por Santa Monica Studio y Sony Computer Entertainment, es un juego de acción y aventuras con combates épicos contra criaturas mitológicas.")
                elif clase[0] == "PacMan":
                    await ctx.send("este personaje de videojuegos es Pac-Man protagonista del icónico arcade Pac-Man lanzado el 22 de mayo de 1980 por Namco, es un juego de laberintos donde el jugador debe comer puntos y evitar ser atrapado por fantasmas.")

            except:
                await ctx.send("recuerda que debes adjuntar un archivo de imagen para que pueda clasificarlo.")
    else:
        await ctx.send("Por favor, adjunta una imagen para clasificar.")



bot.run("<TOKEN>")  # remplaza con tu token de bot de Discord
# Asegúrate de que el token esté en un lugar seguro y no lo compartas
