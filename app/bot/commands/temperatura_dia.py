from telegram import Update
from telegram.ext import ContextTypes

from app.app_log import get_logger
from app.settings import Config
from app.core import ClimaScrap

scraper = ClimaScrap()
logger = get_logger(f"[{Config().APP_NAME}: Command Module]")

async def temperatura_del_dia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        clima = scraper.get_temperature_average()
        logger.info("Enviando temperatura del día")

        clima_message = f"""
Hola sexys... debo informarte que el día de hoy la temperatura está a *{str(clima)}*... ¿estás prevenid@? 🌡️😏
"""

        await update.message.reply_text(clima_message, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Error al tratar de ejecutar el comando: {e}")