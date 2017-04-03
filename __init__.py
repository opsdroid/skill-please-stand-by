from opsdroid.matchers import match_regex

@match_regex(r'[Pp]lease stand by')
async def hello(opsdroid, config, message):
    await message.respond("https://images.informaticslab.co.uk/misc/192a5b498a93370cd662b0c9292e56ef.gif")
