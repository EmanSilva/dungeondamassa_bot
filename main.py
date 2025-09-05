from bot.commands import *
from telegram.ext import Application, CommandHandler
from config import *

TOKEN = TELEGRAM_TOKEN


def main():
    print(TOKEN)
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("roll", roll))
    app.add_handler(CommandHandler("list_skills", list_skills))
    app.add_handler(CommandHandler("list_rules", list_rules))
    app.add_handler(CommandHandler("list_races", list_races))
    app.add_handler(CommandHandler("list_classes", list_classes))
    app.add_handler(CommandHandler("list_conditions", list_conditions))
    app.add_handler(CommandHandler("list_spells", list_spells))
    app.add_handler(CommandHandler("list_monsters", list_monsters))
    app.add_handler(CommandHandler("spell", spell_desc))
    app.add_handler(CommandHandler("monster", monster_desc))

    app.run_polling()

if __name__ == '__main__':
    main()

