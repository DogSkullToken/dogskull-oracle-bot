import tweepy
import time
import json
import os
from datetime import datetime
from bot.config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET,
    TWITTER_BEARER_TOKEN
)
from bot.oracle import gerar_profecia

LOG_FILE = "tweet_log.json"
LIMIT_PER_MONTH = 500

def carregar_log():
    if not os.path.exists(LOG_FILE):
        return {"month": datetime.now().month, "count": 0}
    
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def salvar_log(data):
    with open(LOG_FILE, "w") as f:
        json.dump(data, f)

def iniciar_twitter_bot():
    try:
        client = tweepy.Client(
            bearer_token=TWITTER_BEARER_TOKEN,
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_SECRET
        )

        print("✅ Twitter bot authenticated and running.")

        # Obtem ID do bot
        try:
            bot_user = client.get_user(username="DogSkullOracle").data
            bot_id = bot_user.id
        except Exception as e:
            print("❌ Erro ao obter ID do bot:", e)
            return

        since_id = None

        while True:
            log = carregar_log()
            current_month = datetime.now().month

            if log["month"] != current_month:
                log = {"month": current_month, "count": 0}

            # POSTA nova profecia se não atingiu limite
            if log["count"] < LIMIT_PER_MONTH:
                try:
                    texto = gerar_profecia()
                    tweet = f"🔮 DogSkull Oracle says:\n\n{texto}"
                    response = client.create_tweet(text=tweet)
                    print(f"🕊️ Tweet sent: {response.data['id']}")
                    log["count"] += 1
                    salvar_log(log)
                except Exception as e:
                    print(f"⚠️ Failed to post prophecy: {e}")

            # VERIFICA menções a cada 65s durante 12h
            for _ in range(664):  # 65s * 664 ≈ 12 horas
                try:
                    mentions = client.get_users_mentions(id=bot_id, since_id=since_id, max_results=5)
                    if mentions and mentions.data:
                        for mention in reversed(mentions.data):
                            texto = gerar_profecia()
                            client.create_tweet(
                                in_reply_to_tweet_id=mention.id,
                                text=f"💀 A vision appears:\n{texto}"
                            )
                            print(f"🧠 Responded to mention: {mention.id}")
                            since_id = mention.id
                except Exception as e:
                    print(f"⚠️ Failed to handle mentions: {e}")

                time.sleep(65)

    except Exception as e:
        print(f"❌ Twitter authentication failed: {e}")
