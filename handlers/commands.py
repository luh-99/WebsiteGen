from telebot import types

# Commands Handlers
def start_handler(message):
    bot.reply_to(message, "Welcome to the bot! Use /help to see available commands.")

def help_handler(message):
    help_text = (
        "Here are the commands you can use:\n"
        "/start - Welcome message\n"
        "/help - List of commands"
    )
    bot.reply_to(message, help_text)
