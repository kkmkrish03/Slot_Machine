import emoji

MAX_SLOTS_FOR_PAY_LINE = 3
MAX_BET = 100
MIN_BET = 1

PAYLINES = 3
REELS = 3

symbol_count = {
    emoji.emojize(':star:', language='en'): 4,
    emoji.emojize(':gem_stone:', language='en'): 4,
    emoji.emojize(':wrapped_gift:', language='en'): 5,
    emoji.emojize(':1st_place_medal:', language='en'): 5,
    emoji.emojize(':fire:', language='en'): 6,
    emoji.emojize(':bomb:', language='en'): 6,
    emoji.emojize(':pig_nose:', language='en'): 7
}

symbol_value = {
    emoji.emojize(':star:', language='en'): 20,
    emoji.emojize(':gem_stone:', language='en'): 17,
    emoji.emojize(':wrapped_gift:', language='en'): 14,
    emoji.emojize(':1st_place_medal:', language='en'): 11,
    emoji.emojize(':fire:', language='en'): 8,
    emoji.emojize(':bomb:', language='en'): 5,
    emoji.emojize(':pig_nose:', language='en'): 2
}