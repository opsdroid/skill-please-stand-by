from opsdroid.matchers import match_regex

@match_regex(r'[Pp]lease stand by')
async def hello(opsdroid, config, message):
    await message.respond("https://images.informaticslab.co.uk/misc/5f4150385b713c61a4019c0e60198e75.gif")
