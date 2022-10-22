#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

# Ported Plugin

"""
✘ Commands Available -

• `{i}تفعيل الساعه`
   لبدء الساعه .

• `{i}تعطيل الساعه`
   لايقاف الساعه .

• `{i}تفعيل البايو`
   لبدء ساعه البايو .

• `{i}تعطيل البايو`
   لايقاف ساعه البايو .
"""

import random

from telethon.tl.functions.account import UpdateProfileRequest

from . import *

CHANGE_TIME = int(udB.get_key("CHANGE_TIME")) if udB.get_key("CHANGE_TIME") else 60

RR7PP = udB.get_key("TI_EM") or "|"
RR7PB = udB.get_key("TI_EMJ") or "|"

normzltext = "0123456789"
namerzfont = udB.get_key("TI_IT") or "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"

@ultroid_cmd(pattern="(تفعيل|تعطيل) الساعه$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "تعطيل":
        udB.del_key("AUTONAME")
        await event.eor("• تم تعطيل الساعه ✓")
        return
    udB.set_key("AUTONAME", "True")
    await eod(event, "• تم تفعيل الساعه ✓")
    while True:
        getn = udB.get_key("AUTONAME")
        if not getn:
            return
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{RR7PB} {HM} {RR7PP}"
        await event.client(UpdateProfileRequest(first_name=name))
        await asyncio.sleep(CHANGE_TIME)
        


@ultroid_cmd(pattern="(تفعيل|تعطيل) البايو$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "تعطيل":
        udB.del_key("AUTOBIO")
        await event.eor("• تم تعطيل ساعه البايو ✓")
        return
    udB.set_key("AUTOBIO", "True")
    await eod(event, "• تم تفعيل ساعه البايو ✓")
    BIOS = [
        "Busy Today !",
        "ULTROID USER",
        "Enjoying Life!",
        "Unique as Always!" "Sprinkling a bit of magic",
        "Intelligent !",
    ]
    while True:
        getn = udB.get_key("AUTOBIO")
        if not getn:
            return
        BIOMSG = random.choice(BIOS)
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{RR7PB} {HM} {RR7PP}"
        await event.client(
            UpdateProfileRequest(
                about=name,
            )
        )
        await asyncio.sleep(CHANGE_TIME)
