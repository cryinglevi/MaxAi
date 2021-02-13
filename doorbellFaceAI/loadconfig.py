import json

with open('config.json') as config_file:
    jsonconfigdata = json.load(config_file)

telebotid = jsonconfigdata['telegram-bot-key']
telechatid = jsonconfigdata['telegram-chat-id']
