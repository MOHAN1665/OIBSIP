import emoji

def convert_emoji(text):
    return emoji.emojize(text, use_aliases=True)

def display_with_emoji(text):
    return emoji.demojize(text)
