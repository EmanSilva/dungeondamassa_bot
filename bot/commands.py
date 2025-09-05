from service.services import *
from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    Comandos disponíveis: \n /roll \n /list_skills \n /list_rules \n /list_races 
    \n /list_classes \n /list_conditions \n /list_spells
    
    """)

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
    # level=5, class=sorcerer
    if text:
        params = text.split(",")
        var = {}
        for param in params:
            if 'level' in param:
                var['level'] = int(param.strip().split('=')[1])
            elif 'class' in param:
                var['class'] = param.strip().split('=')[1]
        spells = await get_spells(var)
        await update.message.reply_text(spells)
    else:
        spells = await get_spells({})
        await update.message.reply_text(spells)

async def spell_desc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    spell = await get_spell(text)
    await update.message.reply_text(spell)

async def monster_desc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    monster = await get_monster(text)
    await update.message.reply_text(monster)

async def list_monsters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    print(text)
    if text:
        params = text.split(",")
        var = {}
        for param in params:
            if 'name' in param:
                var['name'] = param.strip().split('=')[1]
            elif 'type' in param:
                var['type'] = param.strip().split('=')[1]
            elif 'size' in param:
                var['size'] = param.strip().split('=')[1]
            elif 'range' in param:
                var['challengeRating'] = {'range':{}}
                var['challengeRating']["range"]['gte'] = int(param.strip().split('=')[1].strip().split('-')[0])
                var['challengeRating']["range"]['lte'] = int(param.strip().split('=')[1].strip().split('-')[1])
        monsters = await get_monsters(var)
        await update.message.reply_text(monsters)
    else:
        monsters = await get_monsters({})
        await update.message.reply_text(monsters)