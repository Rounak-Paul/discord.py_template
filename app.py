import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$help'):
            await message.channel.send("Help is no more")
            
        print(f'{message.author}: {message.content}')

intents = discord.Intents.default()
print(intents)
intents.message_content = True

token = ''
client = MyClient(intents=intents)
client.run(token)