import os
import discord

# Define las intenciones del cliente para incluir la intención de mensajes
intents = discord.Intents.default()
intents.messages = True  # Corrección: Utilizar 'messages' en lugar de 'message_content'

# Obtiene el token de autenticación del entorno
TOKEN = os.getenv('DISCORD_TOKEN')

# Inicializa el cliente con las intenciones definidas
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Nos hemos conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!holi'):
        await message.channel.send('cállate puto mueble')
        
    if message.content.startswith('!negro'):
        await message.channel.send('Ojalá se mueran')

# Ejecuta el cliente con el token de autenticación
client.run(TOKEN)

