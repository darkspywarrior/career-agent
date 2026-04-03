import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

    NAME = os.getenv("NAME")
    EMAIL = os.getenv("EMAIL")
    PHONE = os.getenv("PHONE")

config = Config()
