from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

# Showing info of the creator
def info(line_api, event):
    result = "This bot is created by Ahmad Fahmi Pratama.\n" \
             "Some of the contents are taken from my friend, Izzan, Cis, etc.\n" \
             "Visit my web at ahmadfahmi.me ! hehe"
    line_api.reply_message (
        event.reply_token, TextSendMessage(text=result)
    )

# Leave group
def leave(line_api, event):
    result = "Leaving group..."
    line_api.reply_message(
        event.reply_token, TextSendMessage(text=result)
    )
    try:
        line_api.leave_group(event.source.group_id)
    except:
        line_api.reply_message(
            event.reply_token, TextSendMessage(text="Failed")
        )

# Help list
def help(line_api, event):
    result = "Command lists:\n" \
             "- !intern list\n" \
             "- !tips {cv/interview/materi}\n" \
             "- !webcarikerja \n" \
             "- !beasiswa\n" \
             "- !help\n" \
             "- !leave\n" \
             "- !info\n"
    line_api.reply_message(
        event.reply_token, TextSendMessage(text=result)
    )
