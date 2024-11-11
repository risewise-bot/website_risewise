from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# RiseWise app data structure
rise_wise_data = {
    "app": {
        "name": "RiseWise",
        "features": [
            {
                "feature_name": "Chatbot",
                "description": "Assists users in setting routines based on different age groups.",
                "settings": {
                    "language": "English",
                    "personality": "Friendly and Supportive"
                },
                "age_groups": [
                    {
                        "group_name": "Children",
                        "age_range": "5-12",
                        "routine_suggestions": [
                            {"time": "7:00 AM", "activity": "Wake up and morning hygiene"},
                            {"time": "8:00 AM", "activity": "Breakfast"},
                            {"time": "9:00 AM", "activity": "Study time"},
                            {"time": "12:00 PM", "activity": "Lunch"}
                        ]
                    },
                    {
                        "group_name": "Teenagers",
                        "age_range": "13-18",
                        "routine_suggestions": [
                            {"time": "6:30 AM", "activity": "Morning exercise and hygiene"},
                            {"time": "7:30 AM", "activity": "Breakfast and school preparation"},
                            {"time": "8:30 AM", "activity": "School/Study"},
                            {"time": "1:00 PM", "activity": "Lunch break"}
                        ]
                    },
                    {
                        "group_name": "Adults",
                        "age_range": "19-64",
                        "routine_suggestions": [
                            {"time": "6:00 AM", "activity": "Morning exercise"},
                            {"time": "7:00 AM", "activity": "Breakfast and prepare for work"},
                            {"time": "9:00 AM", "activity": "Work/Study"},
                            {"time": "12:00 PM", "activity": "Lunch break"}
                        ]
                    },
                    {
                        "group_name": "Seniors",
                        "age_range": "65+",
                        "routine_suggestions": [
                            {"time": "6:30 AM", "activity": "Wake up and light exercise"},
                            {"time": "7:30 AM", "activity": "Breakfast"},
                            {"time": "10:00 AM", "activity": "Recreation/Relaxation"},
                            {"time": "12:00 PM", "activity": "Lunch"}
                        ]
                    }
                ]
            }
        ]
    }
}

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to RiseWise! Please choose an age group to get routine suggestions:\n"
        "1. Children (5-12)\n"
        "2. Teenagers (13-18)\n"
        "3. Adults (19-64)\n"
        "4. Seniors (65+)"
    )

# Routine suggestion handler
def get_routine(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    
    age_group_mapping = {
        "children": "Children",
        "teenagers": "Teenagers",
        "adults": "Adults",
        "seniors": "Seniors"
    }

    age_group = age_group_mapping.get(user_message)

    if age_group:
        group_data = next(item for item in rise_wise_data['app']['features'][0]['age_groups'] if item["group_name"] == age_group)
        suggestions = group_data['routine_suggestions']
        
        routine_message = f"Routine suggestions for {age_group}:\n"
        for suggestion in suggestions:
            routine_message += f"{suggestion['time']}: {suggestion['activity']}\n"
        
        update.message.reply_text(routine_message)
    else:
        update.message.reply_text("Please enter a valid age group (Children, Teenagers, Adults, Seniors).")

def main() -> None:
    # Replace 'YOUR_API_TOKEN' with your bot's API token
    updater = Updater("8085486845:AAGKOjiEIEoTbuw-_BM4ss4dL0OQHzUGAo0")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_routine))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

if _name_ == '_main_':
    main()