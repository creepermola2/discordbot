import discord
from discord.ext import commands

# Configura el prefijo de los comandos
bot = commands.Bot(command_prefix='!')

# Define un evento para imprimir un mensaje cuando el bot esté listo
@bot.event
async def on_ready():
    print(f'¡{bot.user.name} está listo para funcionar!')

# Define un comando que responde cuando alguien escribe "hola"
@bot.command()
async def hola(ctx):
    await ctx.send('Calla sillón asqueroso')

# Ejecuta el bot con el token de autenticación
bot.run('')