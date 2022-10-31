"""
• جميع هذه الاوامر تستخدم بالرد على الشخص كترفيه
◂  `.رفع بقلبي`
◂  `.رفع زوجي`
◂  `.رفع علق`
◂  `.رفع مراتي`
◂  `.رفع كلب`
◂  `.رفع جاموسة`
◂  `.رفع قرد`
◂  `.رفع حيوان`
◂  `.رفع بشخة`
◂  `.رفع معرص`
◂  `.رفع بهيمة`
◂  `.رفع شبشب`
◂  `.رفع تور`
◂  `.رفع حلويات`
◂  `.نسبة الحب`
◂  `.نسبة الانوثة`
◂  `.نسبة الرجولة`
◂  `.نسبة الغباء`
◂  `.نسبة الذكاء`
◂  `.كت`
◂  `.اوصف`
◂  `.هينه`
◂  `.زواج`
◂  `.طلاق`
◂  `.شغله`
"""

import random

from razan.strings.fun import *
from . import ultroid_cmd
from . import *
from pyUltroid._misc._user import get_user_from_event

@ultroid_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه بقلبك ♥️ "
    )

@ultroid_cmd(pattern="رفع بهيمة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـها بهيمة 🐂\nهاتولها برسيم بسرعه 🌱😂 "
    )

@ultroid_cmd(pattern="رفع تور(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتور هايج ف عنبر سته  😂🦏\nحلقوا عليه 😂 "
    )

    
@ultroid_cmd(pattern="رفع زوجي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعه زوجك روحوا خلفوا 🤤😂",
    )


@ultroid_cmd(pattern="رفع علق(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفـعه علق  😂"
    )


@ultroid_cmd(pattern="رفع مراتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـها مـࢪاتك الف مبروك 😹🤤",
    )


@ultroid_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه كلب خليه يقعد يهوهو 😂🐶",
    )


@ultroid_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@ultroid_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1824749880:
        return await edit_or_reply(mention, f"اهين مين يا مره دا المطور 😏")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@ultroid_cmd(pattern="نسبة الحب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza}"
    )


@ultroid_cmd(pattern="نسبة الانوثة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1824749880:
        return await edit_or_reply(mention, f"دا ارجل من الجابوك دا")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الانوثة لـ [{muh}](tg://user?id={user.id})هـي {sos} 🥵🖤"
    )


@ultroid_cmd(pattern="نسبة الغباء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )

@ultroid_cmd(pattern="نسبة الذكاء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(ZK)
    await edit_or_reply(
        mention, f"نسبة الذكاء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )
    
@ultroid_cmd(pattern="رفع جاموسة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـها جاموسة\nوهى جاموسه اصلا 😂🦬"
    )

@ultroid_cmd(pattern="رفع شبشب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه شبشب\nحد يجى يلبسه 😂"
    )
    
@ultroid_cmd(pattern="رفع حلويات(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه حلويات\nالكيلو ب اتنين وبس 😂"
    )
    
@ultroid_cmd(pattern="رفع قرد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه قرد هاتوله موزة 🐒🍌",
    )


@ultroid_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")


@ultroid_cmd(pattern="شغله(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(rzwhat)
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )


@ultroid_cmd(pattern="نسبة الرجولة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1824749880:
        return await edit_or_reply(mention, f"ارجل من بلدك دا 😂")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} "
    )


@ultroid_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه حيوان 🐏"
    )


@ultroid_cmd(pattern="رفع بشخة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه طفل بشخه 😂\nهاتوله بامبرز بسرعه 😂💔"
    )


@ultroid_cmd(pattern="رفع معرص(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعـه معرص 😒"
    )


@bot.on(admin_cmd(pattern="زواج(?:\s|$)([\s\S]*)"))
async def rzfun(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    await edit_or_reply(mention, f"نتجوز واغسلك المواعين 🥺😂")


@bot.on(admin_cmd(pattern="طلاق(?:\s|$)([\s\S]*)"))
async def mention(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    await edit_or_reply(mention, f"انتى طالق بالعشرة 😂😭\nيلا ي بنت الكلب بره 😂")
