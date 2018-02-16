import json

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

def intern_info(line_api, event, text):
    text = ""

# Showing internship tips
def intern_tips(line_api, event, text):
    result = "CV, etc"
    line_api.reply_message(
        event.reply_token, TextSendMessage(text=result)
    )
