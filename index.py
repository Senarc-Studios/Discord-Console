import asyncio

from discord import Intents, User

from cool_utils import Terminal

from discord.ext.commands import Bot

from functions import Constants

class Console(Bot):
    def __init__(self):
        super().__init__(
            command_prefix = "c!",
            intents = Intents.all(),
            application_id = Constants.get("APPLICATION_ID")
        )

    async def is_owner(self, user: User):
        if Constants.get("OWNER_ONLY_ACCESS"):
            return user.id == Constants.get("OWNER_ID")
        return True

    async def start(self, *args, **kwargs):
        await super().start(*args, **kwargs)

    async def close(self, *args, **kwargs):
        await super().close(*args, **kwargs)

    async def setup_hook(self):
        await self.load_extension("jishaku")

bot = Console()

@bot.listen("on_ready")
async def startup():
    Terminal.display("Console bot has established connection with discord api.")

@bot.listen("on_message")
async def console(message):
    if message.channel.id == int(Constants.get("CONSOLE")):
        message.content = f"c!jsk sh {message.content}"
        await bot.process_commands(message)

asyncio.run(bot.start(Constants.get("TOKEN")))