"""
Central configuration for the bot.
Set your BOT_TOKEN via environment variable before running:

    export BOT_TOKEN="8857677089:AAGN57W0U0VYPhZopRySa7DViyLtZ-2mAKM"
    python bot.py

Or just replace the default string below (not recommended for production).
"""

import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8857677089:AAGN57W0U0VYPhZopRySa7DViyLtZ-2mAKM")

DB_PATH = os.getenv("DB_PATH", "game.db")

# --- Gameplay tuning ---
EXPLORE_COOLDOWN_SECONDS = 20          # cooldown between /hunt uses
DAILY_BASE_REWARD = 50                 # base gold for /daily
DAILY_STREAK_BONUS = 15                # extra gold per streak day (capped)
DAILY_STREAK_CAP = 10                  # max streak days counted for bonus
XP_PER_LEVEL_BASE = 100                # xp needed = level * XP_PER_LEVEL_BASE
STARTING_GOLD = 100
STARTING_HP = 100
STARTING_ATTACK = 10
STARTING_DEFENSE = 5

LEADERBOARD_SIZE = 10