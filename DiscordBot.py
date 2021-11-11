import discord, json, random
import DiscordVoiceBot
from DiscordVoiceBot import Music
from discord.ext import commands

with open("token.json") as jToken:
    token = json.load(jToken)

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Relatively simple music bot example')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author == client.user:
            return

        if 'happy birthday' in message.content.lower():
            await message.channel.send('Happy Birthday! 🎈🎉')

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)

        

bot.add_cog(Music(bot))
client = MyClient()
client.run(token)
