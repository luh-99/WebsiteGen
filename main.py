from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext
import random

# Your existing list of websites
strange_websites = [
    "http://runthegauntlet.org",
    "http://kekma.net",
    "http://mrdeepfakes.com",
    "http://lomando.com",
    # Add more old websites here if you want
]

new_websites = [
    "http://hosanna1.com",
    "http://pointerpointer.com",
    "http://hashima-island.co.uk",
    "http://skywaybridge.com",
    "http://thisman.org",
    "http://internetlivestats.com",
    "http://acolumbinesite.com",
    "http://hackertyper.com",
    "http://essaytyper.com",
    "http://theworldsworstwebsiteever.com"
]

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Generate Website", callback_data='generate')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Welcome! Press the button below to generate a strange or unusual website link.",
        reply_markup=reply_markup
    )

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    website = random.choice(strange_websites + new_websites)

    if website == "http://runthegauntlet.org":
        warning_message = (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website contains graphic content and gore!\n"
            "Visit at your own risk!\n\n"
            f"Website: {website}"
        )
    elif website == "http://kekma.net":
        warning_message = (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website contains graphic content and gore!\n"
            "Visit at your own risk!\n\n"
            f"Website: {website}"
        )
    elif website == "http://mrdeepfakes.com":
        warning_message = (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website is for NSFW Deepfakes!\n"
            "Visit at your own risk!\n\n"
            f"Website: {website}"
        )
    elif website == "http://lomando.com":
        warning_message = (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website features a horror game and contains jumpscares!\n"
            "Visit if you dare!\n\n"
            f"Website: {website}"
        )
    elif website == "http://acolumbinesite.com":
        warning_message = (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website contains graphic details of the Columbine school shooting.\n"
            "Viewer discretion is advised!\n\n"
            f"Website: {website}"
        )
    elif website == "http://skywaybridge.com":
        warning_message = (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website contains details of every suicide committed on the bridge.\n"
            "Please refrain from visiting if you are in a poor state of mind.\n\n"
            f"Website: {website}"
        )
    else:
        warning_message = (
            f"Generated Website: {website}\n\n"
            "<b>WARNING! SOME WEBSITES ARE GRAPHIC AND/OR SCARY! "
            "TAKE CAUTION BEFORE CLICKING ON THE GENERATED LINK!</b>"
        )

    query.edit_message_text(
        text=warning_message,
        parse_mode='HTML'
    )


if __name__ == "__main__":
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()
