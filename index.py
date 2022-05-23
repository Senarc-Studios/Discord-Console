from discord import Intents

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

    async def start(*args, **kwargs):
        await super().start(*args, **kwargs)

    async def close(*args, **kwargs):
        await super().close(*args, **kwargs)

bot = Console()

@bot.listen("on_ready")
async def startup():
    Terminal.display("Console bot has established connection with discord api.")

bot.start(Constants.get("TOKEN"))