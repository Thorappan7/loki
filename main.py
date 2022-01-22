from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import asyncio
from info import Jk

SESSION="BQBzgywsSTNH2U9KVbjHrGrvJoZM98iq4OfaE3dNDthLv_j_8QvDqf7uVLW1Rpno4FFci7YcgZZxwbuPflnjzuE36e3s4-CrCXnWPGzG180vFa5QxhmIUTZ25X_9E_jPUFad6Aoz2eXb5W3SLkihHbdvkAip45zmAe53Uy-RPVDd-h5nM-iv2pX1h2WcrH05fbJ9yTOn5GnAq6XQyunc5wDsOIfqtmrMpAU8QXHM2sld9ljYAHNMmH7ow2iV8EJQuVctr59Vv7iOmae2rv5qfSjPaVQ3e6yfIkGPu-ArsPHAd1DCGakhs9Jm_bRMDdm_SHW3b59PcI2Vfl2oVKdXAja-ImTMYQA"

class Bot(Client):

    def __init__(self):
        super().__init__(
        api_id=502966,
        api_hash="ba91c94ee88658b8702befa528544df3",
        bot_token="5153914057:AAGnHPEtgNYctk-zgoluy1PatigpuN65WD0",
        session_name =SESSION,
        plugins = {"root": "bot" },
        sleep_threshold=5
        )

 

app = Bot()
app.run()

