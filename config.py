import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WATERMARK = os.environ.get("WATERMARK", "...watermark...")
FONT_SIZE = os.environ.get("FONT_SIZE", 15)
FONT_NAME = "Vera_Crouz.ttf"  # check tools/fonts
TRANSPARENCY = os.environ.get("TRANSPARENCY", 0.75)
QUALITY = os.environ.get("QUALITY", 100)
