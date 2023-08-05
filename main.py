#v2.2

import discord
from discord.ext import commands
import os
from datetime import datetime as dt
import pytz
from keep_alive import keep_alive

last_event_no = 5
next_event_no = last_event_no + 1
last_event = f"GFC {last_event_no:03}"
next_event = f"GFC {next_event_no:03}"
last_event_date = "20/07/23"
next_event_date = "6/08/23"
cup_date = "16/02/24"
uk_timezone = pytz.timezone("Europe/London")

days_until_next_event = abs(
    uk_timezone.localize(dt.strptime(next_event_date, "%d/%m/%y")) -
    dt.now(uk_timezone).replace(hour=0, minute=0, second=0, microsecond=0)
).days

days_since_last_event = abs(
    uk_timezone.localize(dt.strptime(last_event_date, "%d/%m/%y")) -
    dt.now(uk_timezone).replace(hour=0, minute=0, second=0, microsecond=0)
).days

days_until_cup = abs(
    uk_timezone.localize(dt.strptime(cup_date, "%d/%m/%y")) -
    dt.now(uk_timezone).replace(hour=0, minute=0, second=0, microsecond=0)
).days

#Fighters database
fighters = {
    "Shaheer": {
        "weight_class": "LIGHT-HEAVYWEIGHT",
        "weight": "75 kg",
        "record": "2-0-0",
        "last_fight": "GFC 005",
        "last_fight_result": "Shaheer beat Mazhar 3 rounds to 0",
        "pound_for_pound_rank": 1,
        "total_fouls": 1,
        "current_champion": False,
        "former_champion": False,
        "total_rounds_won": 6,
        "total_rounds_lost": 0
    },
    "Mowahid": {
        "weight_class": "LIGHTWEIGHT",
        "weight": "57 kg",
        "record": "1-0-0",
        "last_fight": "GFC 001",
        "last_fight_result": "Mowahid beat Mazhar 3 rounds to 2",
        "pound_for_pound_rank": 3,
        "total_fouls": 0,
        "current_champion": False,
        "former_champion": True,
        "total_rounds_won": 3,
        "total_rounds_lost": 2
    },
    "Mazin": {
        "weight_class": "LIGHTWEIGHT",
        "weight": "52 kg",
        "record": "1-0-0",
        "last_fight": "GFC 002",
        "last_fight_result": "Mazin beat Ubaid 2 rounds to 1",
        "pound_for_pound_rank": 2,
        "total_fouls": 1,
        "current_champion": True,
        "former_champion": False,
        "total_rounds_won": 2,
        "total_rounds_lost": 1
    },
    "Ayaan": {
        "weight_class": "LIGHTWEIGHT",
        "weight": "52 kg",
        "record": "1-0-0",
        "last_fight": "GFC 002",
        "last_fight_result":
        "Ayaan lost to Mazhar 1 round to 2 (Overturned by GFC Council)",
        "pound_for_pound_rank": 5,
        "total_fouls": 2,
        "current_champion": False,
        "former_champion": False,
        "total_rounds_won": 1,
        "total_rounds_lost": 0
    },
    "Ubaid": {
        "weight_class": "MIDDLEWEIGHT",
        "weight": "65 kg",
        "record": "1-2-0",
        "last_fight": "GFC 004",
        "last_fight_result": "Ubaid beat Mazhar 2 rounds to 1",
        "pound_for_pound_rank": 4,
        "total_fouls": 4,
        "current_champion": False,
        "former_champion": False,
        "total_rounds_won": 3,
        "total_rounds_lost": 6
    },
    "Daniyal": {
        "weight_class": "HEAVYWEIGHT",
        "weight": "95 kg",
        "record": "0-0-0",
        "last_fight": None,
        "last_fight_result": None,
        "pound_for_pound_rank": None,
        "total_fouls": 0,
        "current_champion": False,
        "former_champion": False,
        "total_rounds_won": 0,
        "total_rounds_lost": 0
    },
    "Musa": {
        "weight_class": "LIGHT-HEAVYWEIGHT",
        "weight": "75 kg",
        "record": "0-0-0",
        "last_fight": None,
        "last_fight_result": None,
        "pound_for_pound_rank": None,
        "total_fouls": 0,
        "current_champion": False,
        "former_champion": False,
        "total_rounds_won": 0,
        "total_rounds_lost": 0
    },
    "Sharafat": {
        "weight_class": "LIGHTWEIGHT",
        "weight": "50 kg",
        "record": "0-0-0",
        "last_fight": None,
        "last_fight_result": None,
        "pound_for_pound_rank": None,
        "total_fouls": 0,
        "current_champion": False,
        "former_champion": False,
        "total_rounds_won": 0,
        "total_rounds_lost": 0
    },
    "Mazhar": {
        "weight_class": "LIGHT-HEAVYWEIGHT",
        "weight": "75 kg",
        "record": "0-4-0",
        "last_fight": "GFC 005",
        "last_fight_result": "Mazhar lost to Shaheer 0 rounds to 3",
        "pound_for_pound_rank": 6,
        "total_fouls": 7,
        "current_champion": False,
        "former_champion": False,
        "total_rounds_won": 3,
        "total_rounds_lost": 9
    }
}

# Bot token.
TOKEN = os.getenv("TOKEN")

# Enable all intents.
intents = discord.Intents.all()

# Commands prefix
bot = commands.Bot(command_prefix="!", intents=intents)


# On startup sends message in terminal.
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=f"{next_event}"))
  print(f"{bot.user} is active.")


# Commands:
@bot.command(name="gfcdates")
async def response(ctx):
  if days_until_next_event == 0:
    await ctx.send(
        f"Today is {next_event}. {last_event} was {days_since_last_event} day{'s' if days_since_last_event != 1 else ''} ago."
    )
  else:
    await ctx.send(
        f"{next_event} is in {days_until_next_event} day{'s' if days_until_next_event != 1 else ''}. {last_event} was {days_since_last_event} day{'s' if days_since_last_event != 1 else ''} ago."
    )


@bot.command(name="recap")
async def response(ctx):
  await ctx.send(
      f"Last time, at {last_event}, Shaheer beat Mazhar 3 rounds to 0.")


@bot.command(name="fighterdetails")
async def response(ctx, name, *selected_details):
  if not name:
    await ctx.send("Error: Please enter a fighter's name.")
    return
  name = name.capitalize()
  if name == "All":
    for fighter, details in fighters.items():
      await send_fighter_details(ctx, fighter, details, selected_details)
  elif name not in fighters:
    await ctx.send("Error: Invalid fighter.")
  else:
    fighter_details = fighters[name]
    if not selected_details:
      await send_fighter_details(ctx, name, fighter_details)
    else:
      selected_details = [detail.lower() for detail in selected_details]
      valid_details = {key.lower() for key in fighter_details.keys()}
      invalid_details = set(selected_details) - valid_details

      if invalid_details:
        await ctx.send(
            f"Error: Invalid detail(s): {', '.join(invalid_details)}")
        return

      await send_fighter_details(ctx, name, fighter_details, selected_details)


async def send_fighter_details(ctx, name, details, selected_details=None):
  msg = f"**{name} Details**\n"
  if selected_details:
    for detail in selected_details:
      formatted_key = detail.replace('_', ' ').title()
      if detail in details:
        msg += f"{formatted_key}: {details[detail]}\n"
      else:
        msg += f"{formatted_key}: Not Available\n"
  else:
    for key, value in details.items():
      formatted_key = key.replace('_', ' ').title()
      msg += f"{formatted_key}: {value}\n"
  await ctx.send(msg)


#Devnotes command:
@bot.command(name="devnotes")
async def response(ctx):
  try:
    with open("devnotes.md", "r", encoding="utf-8") as file:
      notes = file.read()
      await ctx.send(notes)
  except FileNotFoundError:
    await ctx.send("Error: devnotes not found.")


# keep_alive() is run.
keep_alive()
# Starts the bot.
bot.run(TOKEN)
