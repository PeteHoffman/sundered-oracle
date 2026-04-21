import os
import random
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

ACTION_ORACLE = [
    "Abandon", "Acquire", "Advance", "Affect", "Aid", "Arrive", "Assault", "Attack", "Avenge", "Avoid",
    "Await", "Begin", "Betray", "Blockade", "Bolster", "Breach", "Break", "Capture", "Challenge", "Change",
    "Charge", "Clash", "Command", "Communicate", "Construct", "Control", "Coordinate", "Create", "Debate", "Defeat",
    "Defend", "Deflect", "Defy", "Deliver", "Demand", "Depart", "Destroy", "Distract", "Eliminate", "Endure",
    "Escalate", "Escort", "Evade", "Explore", "Falter", "Find", "Finish", "Focus", "Follow", "Fortify",
    "Gather", "Guard", "Hide", "Hold", "Hunt", "Initiate", "Inspect", "Investigate", "Journey", "Learn",
    "Leave", "Locate", "Lose", "Manipulate", "Mourn", "Move", "Oppose", "Overwhelm", "Persevere", "Preserve",
    "Protect", "Raid", "Reduce", "Refuse", "Reject", "Release", "Remove", "Resist", "Restore", "Reveal",
    "Risk", "Scheme", "Search", "Secure", "Seize", "Serve", "Share", "Strengthen", "Study", "Summon",
    "Support", "Suppress", "Surrender", "Swear", "Threaten", "Transform", "Uncover", "Uphold", "Weaken", "Withdraw"
]

THEME_ORACLE = [
    "Ability", "Advantage", "Alliance", "Authority", "Balance", "Barrier", "Belief", "Blood", "Bond", "Bounty",
    "Burden", "Commerce", "Community", "Corruption", "Creation", "Crime", "Culture", "Cure", "Curse", "Danger",
    "Death", "Debt", "Decay", "Deception", "Defense", "Destiny", "Disaster", "Discovery", "Disease", "Dream",
    "Duty", "Enemy", "Expedition", "Faction", "Fame", "Family", "Fear", "Fellowship", "Freedom", "Greed",
    "Hardship", "Hate", "Health", "History", "Home", "Honor", "Hope", "Industry", "Innocence", "Knowledge",
    "Labor", "Language", "Law", "Leadership", "Legacy", "Legend", "Life", "Love", "Memory", "Nature",
    "Navigation", "Opportunity", "Peace", "Possession", "Power", "Price", "Pride", "Prize", "Prophecy", "Protection",
    "Quest", "Relationship", "Religion", "Reputation", "Resource", "Revenge", "Rival", "Rumor", "Safety", "Sanctuary",
    "Secret", "Solution", "Spirit", "Stranger", "Strategy", "Strength", "Superstition", "Supply", "Survival", "Time",
    "Trade", "Treaty", "Truth", "Vengeance", "Vow", "War", "Warning", "Weakness", "Wealth", "Weapon"
]

DESCRIPTOR_ORACLE = [
    "Abandoned", "Abundant", "Active", "Ancient", "Barren", "Blighted", "Blocked", "Breached", "Broken", "Captured",
    "Chaotic", "Charted", "Collapsed", "Colossal", "Confined", "Conspicuous", "Constructed", "Contested", "Corrupted", "Created",
    "Cursed", "Damaged", "Dead", "Deadly", "Decaying", "Deep", "Defended", "Dense", "Depleted", "Desolate",
    "Destroyed", "Diverse", "Empty", "Ensnaring", "Expansive", "Exposed", "Fertile", "Fiery", "Flooded", "Foreboding",
    "Forgotten", "Forsaken", "Fortified", "Foul", "Fragile", "Frozen", "Functional", "Grim", "Guarded", "Haunted",
    "Hidden", "Hoarded", "Hostile", "Inaccessible", "Infested", "Inhabited", "Isolated", "Legendary", "Living", "Lost",
    "Lush", "Makeshift", "Mechanical", "Misleading", "Moving", "Mysterious", "Natural", "New", "Obscured", "Open",
    "Peaceful", "Perilous", "Pillaged", "Powerful", "Preserved", "Prominent", "Protected", "Rare", "Remote", "Rich",
    "Ruined", "Sacred", "Safe", "Sealed", "Secret", "Settled", "Shrouded", "Stolen", "Stormy", "Stranded",
    "Strange", "Sunken", "Toxic", "Trapped", "Undiscovered", "Unnatural", "Unstable", "Valuable", "Violent", "Wrecked"
]

FOCUS_ORACLE = [
    "Ammunition", "Anchorage", "Animal", "Apparition", "Art", "Artifact", "Battleground", "Beast", "Blockade", "Boat",
    "Book", "Boundary", "Cache", "Cargo", "Commander", "Commodity", "Confinement", "Connection", "Container", "Contraband",
    "Corpse", "Creation", "Creature", "Crew", "Debris", "Derelict", "Discovery", "Enclosure", "Energy", "Equipment",
    "Faction", "Flag", "Fleet", "Force", "Fortification", "Gadget", "Grave", "Habitat", "Hazard", "Hideaway",
    "Home", "Illusion", "Island", "Lair", "Land", "Leader", "Machine", "Map", "Material", "Medicine",
    "Message", "Mist", "Monument", "Obstacle", "Outbreak", "Outpost", "Path", "People", "Person", "Pirate",
    "Port", "Provisions", "Reef", "Refuge", "Relic", "Remains", "Rendezvous", "Resource", "Rock", "Ruins",
    "Sail", "Salvage", "Sea", "Shelter", "Ship", "Shore", "Shortcut", "Sound", "Storage", "Storm",
    "Structure", "Supply", "Symbol", "Terrain", "Territory", "Threshold", "Tool", "Town", "Trap", "Treasure",
    "Vault", "Vegetation", "Vessel", "Village", "Void", "Water", "Weapon", "Weather", "Wind", "Wreckage"
]

ORACLE_CHOICES = [
    app_commands.Choice(name="Scene Prompt", value="scene"),
    app_commands.Choice(name="Detail", value="detail"),
]

def roll_table(table):
    return random.choice(table)

def format_output(title, entries, final_result):
    lines = [f"__{title}__", ""]
    for label, value in entries:
        lines.append(f"{label}:")
        lines.append(f"**{value}**")
        lines.append("")
    lines.append("--------------------")
    lines.append("RESULT:")
    lines.append(f"**{final_result}**")
    return "\n".join(lines)

def build_scene_prompt():
    action = roll_table(ACTION_ORACLE)
    theme = roll_table(THEME_ORACLE)
    final_result = f"{action.upper()} {theme.upper()}"
    return format_output(
        "Scene Prompt",
        [
            ("Action Oracle", action),
            ("Theme Oracle", theme),
        ],
        final_result,
    )

def build_detail():
    descriptor = roll_table(DESCRIPTOR_ORACLE)
    focus = roll_table(FOCUS_ORACLE)
    final_result = f"{descriptor.upper()} {focus.upper()}"
    return format_output(
        "Detail",
        [
            ("Descriptor Oracle", descriptor),
            ("Focus Oracle", focus),
        ],
        final_result,
    )

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="oracle", description="Roll on a Sundered Isles oracle")
@app_commands.describe(kind="Choose the oracle type")
@app_commands.choices(kind=ORACLE_CHOICES)
async def oracle(interaction: discord.Interaction, kind: app_commands.Choice[str]):
    if kind.value == "scene":
        result = build_scene_prompt()
    elif kind.value == "detail":
        result = build_detail()
    else:
        result = "Unknown oracle."
    await interaction.response.send_message(result)

@bot.tree.command(name="help", description="Show SunderedOracle commands")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "__SunderedOracle Help__\n\n"
        "/oracle kind:Scene Prompt\n"
        "Rolls on the Action Oracle and Theme Oracle.\n\n"
        "/oracle kind:Detail\n"
        "Rolls on the Descriptor Oracle and Focus Oracle.\n"
    )

bot.run(TOKEN)
