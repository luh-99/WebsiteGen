from telegram import Update
from telegram.ext import CallbackContext
def button(update: Update, context: CallbackContext) -> None:
    """Handle button presses."""
    query = update.callback_query
    query.answer()

    if query.data == 'generate':
        website = choice(strange_websites + new_websites)  # Assuming new_websites contains your new URLs

        # Check for websites that need special warning messages
        if website == "http://runthegauntlet.org":
            warning_message = (
                "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
                "This website contains graphic content and gore!\n"
                "Visit at your own risk!\n\n"
                "Website: " + website
            )
        elif website == "http://kekma.net":
            warning_message = (
                "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
                "This website contains graphic content and gore!\n"
                "Visit at your own risk!\n\n"
                "Website: " + website
            )
        elif website == "http://mrdeepfakes.com":
            warning_message = (
                "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
                "This website is for NSFW Deepfakes!\n"
                "Visit at your own risk!\n\n"
                "Website: " + website
            )
        elif website == "http://lomando.com":
            warning_message = (
                "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
                "This website features a horror game and contains jumpscares!\n"
                "Visit if you dare!\n\n"
                "Website: " + website
            )
        elif website == "http://acolumbinesite.com":
            warning_message = (
                "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
                "This website contains graphic details of the Columbine school shooting.\n"
                "Viewer discretion is advised!\n\n"
                "Website: " + website
            )
        elif website == "http://skywaybridge.com":
            warning_message = (
                "🚨🚨🚨 ATTENTION! 🚨🚨🚨\n\n"
                "This website contains details of every suicide committed on the bridge.\n"
                "Please refrain from visiting if you are in a poor state of mind.\n\n"
                "Website: " + website
            )
        else:
            warning_message = f"Generated Website: {website}\n\n"
            warning_message += "<b>WARNING! SOME WEBSITES ARE GRAPHIC AND/OR SCARY! "
            warning_message += "TAKE CAUTION BEFORE CLICKING ON THE GENERATED LINK!</b>"

        query.edit_message_text(
            text=warning_message,
            parse_mode='HTML'
        )

# List of new websites to add (to be combined with strange_websites)
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
