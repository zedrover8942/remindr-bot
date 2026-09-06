import json
import os
import random
import time
from pathlib import Path

import discord
from discord import app_commands
from discord.ext import tasks

STATE = Path("state.json")
QUOTES = [
    "Done is better than perfect.",
    "Simplicity is the soul of efficiency.",
    "Make it work, make it right, make it fast.",
    "Small steps every day.",
]


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"reminders": []}


def save_state(st):
    STATE.write_text(json.dumps(st, indent=1))


class StudyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)
        self.state = load_state()

    async def setup_hook(self):
        self.reminder_loop.start()

    @tasks.loop(seconds=15)
    async def reminder_loop(self):
        now = time.time()
        due = [r for r in self.state["reminders"] if r["due"] <= now]
        for r in due:
            ch = self.get_channel(r["channel"])
            if ch:
                await ch.send("<@%s> reminder: %s" % (r["user"], r["text"]))
        if due:
            keep = [r for r in self.state["reminders"] if r["due"] > now]
            self.state["reminders"] = keep
            save_state(self.state)


bot = StudyBot()


@bot.tree.command(name="quote", description="quote of the moment")
async def quote(itx: discord.Interaction):
    await itx.response.send_message(random.choice(QUOTES))


@bot.tree.command(name="remind", description="remind me later")
async def remind(itx: discord.Interaction, minutes: int, text: str):
    bot.state["reminders"].append({
        "user": itx.user.id, "channel": itx.channel_id,
        "text": text, "due": time.time() + minutes * 60})
    save_state(bot.state)
    await itx.response.send_message(
        "ok, reminding you in %d min" % minutes, ephemeral=True)


if __name__ == "__main__":
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        raise SystemExit("set DISCORD_TOKEN first")
    bot.run(token)
