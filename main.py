from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from random import choice
from telegram.constants import ParseMode

strange_websites = [
    "http://runthegauntlet.org",
    "http://kekma.net",
    "http://mrdeepfakes.com",
    "http://lomando.com",
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

def generate_warning(website: str) -> str:
    if website == "http://runthegauntlet.org":
        return (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website contains graphic content and gore!\n"
            "Visit at your own risk!\n\n"
            f"Website: {website}"
        )
    elif website == "http://kekma.net":
        return (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website contains graphic content and gore!\n"
            "Visit at your own risk!\n\n"
            f"Website: {website}"
        )
    elif website == "http://mrdeepfakes.com":
        return (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website is for NSFW Deepfakes!\n"
            "Visit at your own risk!\n\n"
            f"Website: {website}"
        )
    elif website == "http://lomando.com":
        return (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website features a horror game and contains jumpscares!\n"
            "Visit if you dare!\n\n"
            f"Website: {website}"
        )
    elif website == "http://acolumbinesite.com":
        return (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website contains graphic details of the Columbine school shooting.\n"
            "Viewer discretion is advised!\n\n"
            f"Website: {website}"
        )
    elif website == "http://skywaybridge.com":
        return (
            "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
            "This website contains details of every suicide committed on the bridge.\n"
            "Please refrain from visiting if you are in a poor state of mind.\n\n"
            f"Website: {website}"
        )
    else:
        return (
            f"Generated Website: {website}\n\n"
            "<b>WARNING! SOME WEBSITES ARE GRAPHIC AND/OR SCARY! "
            "TAKE CAUTION BEFORE CLICKING ON THE GENERATED LINK!</b>"
        )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome! Use /gen to generate a random website.")

async def gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    website = choice(strange_websites + new_websites)
    warning_message = generate_warning(website)

    await update.message.reply_text(
        text=warning_message,
        parse_mode=ParseMode.HTML
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    website = choice(strange_websites + new_websites)
    warning_message = generate_warning(website)

    await query.edit_message_text(
        text=warning_message,
        parse_mode=ParseMode.HTML
    )

async def main():
    application = ApplicationBuilder().token("TOKEN_ID").build()

    application.add_handler(CommandHandler("start", start))  # Added start handler
    application.add_handler(CommandHandler("gen", gen))
    application.add_handler(CallbackQueryHandler(button))

    await application.run_polling()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    import asyncio
    asyncio.run(main())