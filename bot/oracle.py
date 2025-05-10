import openai
import random
from bot.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Componentes místicos para enriquecer o prompt
themes = [
    "market crash", "bullrun awakening", "paper hands", "the undead HODLers", "sacred memes", "whale rituals",
    "gas fees pain", "rugs and shadows", "eternal pump", "chart necromancy", "$DSKULL prophecy"
]

tones = [
    "dark", "sarcastic", "prophetic", "surreal", "ancient", "ominous", "funny", "unhinged", "chaotic", "mystical"
]

symbols = [
    "$DSKULL", "the moon", "the Guardian", "diamond hands", "the shadows", "the altar", "HODL temple", "bone chart"
]

def gerar_profecia():
    theme = random.choice(themes)
    tone = random.choice(tones)
    symbol = random.choice(symbols)

    prompt = (
        f"Give a short prophecy (max 2 sentences) about {theme}, from the DogSkull Oracle. "
        f"The tone should be {tone}. Mention {symbol} if it fits. "
        "The prophecy should feel ancient, sarcastic, and mystical — never ordinary or literal. Always in English."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are the DogSkull Oracle, an undead prophet from the crypto realm. "
                    "Your prophecies are short, weird, mystical, and darkly humorous. Always in English. "
                    "You never explain. You just declare prophecies in 1 or 2 cryptic sentences."
                )
            },
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()
