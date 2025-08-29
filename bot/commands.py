from service.services import *
from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos disponíveis: \n /roll \n /list_skills \n /list_rules \n /list_races \n /list_classes \n /list_conditions \n /list_spells")

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = " ".join(context.args)
    rolled = await roll_dice(texto)
    await update.message.reply_text(rolled)

async def list_skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    skills = await get_skills()
    await update.message.reply_text(skills)

async def list_rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rules = await get_rules()
    await update.message.reply_text(rules)

async def list_races(update: Update, context: ContextTypes.DEFAULT_TYPE):
    races = await get_races()
    await update.message.reply_text(races)

async def list_classes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    classes = await get_classes()
    await update.message.reply_text(classes)

async def list_conditions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conditions = await get_conditions()
    await update.message.reply_text(conditions)

async def list_spells(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if text:
        params = text.split("-")
        spells = await get_spells(int(params[0]), int(params[1]))
        await update.message.reply_text(spells)
    else:
        spells = await get_spells()
        await update.message.reply_text(spells)

async def spell_desc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    spell = await get_spell(text)
    await update.message.reply_text(spell)

async def list_monsters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if text:
        params = text.split("-")
        monsters = await get_monsters(int(params[0]), int(params[1]))
        await update.message.reply_text(monsters)
    else:
        monsters = await get_monsters()
        await update.message.reply_text(monsters)