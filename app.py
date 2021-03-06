import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

#from Creator import help, info, leave
from command import input

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = 'IF+3kDg6rVn7d/mqWaoxV6fgKPdcoc8741H10GDiIu60d4Zdvm4BMEtJOd/zllm2RKas/nOb+rgpwZL6R0evIfCJRWD2trc5FO6Ju1Lj+G4V84gJr+JK/jhZmIk5v9lmUaxZbhb7BmBc6r7ycnO/MwdB04t89/1O/w1cDnyilFU='
YOUR_CHANNEL_SECRET = 'a0cd332e19192d201ca07610f32cbf8a'
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    input(line_bot_api, event, text)
    # if text == '!info':
    #     info(line_bot_api, event)
    # elif text == '!help':
    #     help(line_bot_api, event)
    # elif text == '!leave':
    #     leave(line_bot_api, event)
    # else:
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text=event.message.text)
    #     )


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
