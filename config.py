import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = os.environ.get("22594398")
    API_HASH = os.environ.get("3a2408d97d6a222d87766dac2da302df")
    VIP_USER = os.environ.get('VIP_USERS', '').split(',')
    VIP_USERS = [int(5357048091) for user_id in VIP_USER]
