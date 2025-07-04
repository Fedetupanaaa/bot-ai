import discord
from discord.ext import commands
import random
from model import get_class 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = random.randint(1,10)):
    await ctx.send("he" * count_heh)


@bot.command()
async def clasificar(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre = archivo.filename
            url = archivo.url
            await archivo.save(nombre)
            await ctx.send(f" la imagen {nombre} se ha guardado correctamente.")
            
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
        except:
            await ctx.send("recuerda que debes adjuntar un archivo de imagen para que pueda clasificarlo.")
    else:
        await ctx.send("Por favor, adjunta una imagen para clasificar.")





bot.run("<TOKEN>")  # remplaza con tu token de bot de Discord
# Asegúrate de que el token esté en un lugar seguro y no lo compartas