import yaml
import os
from InternetSpeedTwitterBot import InternetSpeedTwitterbot

def read_yaml(yaml_path):
    # print(os.path.exists(yaml_path))
    with open(yaml_path, 'r',encoding='utf-8') as f:
        yaml_content = yaml.safe_load(f)
    return yaml_content

config_path = "configs/config.yaml"
configs = read_yaml(config_path)

PROMISED_DOWN = 400
PROMISED_UP = 40
TWITTER_EMAIL = configs["TWITTER_EMAIL"]
PASSWORD = configs["PASSWORD"]

bot = InternetSpeedTwitterbot()

bot.get_internet_speed()
download_speed = bot.down
upload_speed = bot.up

if download_speed < PROMISED_DOWN or upload_speed < PROMISED_UP:
    print(f'Internet speed is to low, sending twitter message to complain')
    bot.tweet_at_provider(TWITTER_EMAIL, PASSWORD, PROMISED_DOWN, PROMISED_UP)
else:
    print(f'Internet speed is fine. Not sending twitter message')

print(f'internet speed evaluation succesful')