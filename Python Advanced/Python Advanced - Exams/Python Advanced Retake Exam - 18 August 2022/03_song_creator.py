def add_songs(*args):
    result = {}
    for data in args:
        title = data[0]
        info = data[1]
        if title not in result:
            result[title] = []
        for lyrics in info:
            result[title].append(lyrics)

    output = ''
    for song_title, lyrics in result.items():
        output += f"- {song_title}"'\n'
        for lyric in lyrics:
            output += f"{lyric}"'\n'

    return output
