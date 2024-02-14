def emoji_conv():
    message=input('>')
    words=message.split(" ")
    struct={
        ":(":"sadEmoji",
        ":)":"laughing emoji",
        ":|":"poatan"
    }
    output=""

    for word in words:
        output+=struct.get(word,word)+" "
    print(output)


emoji_conv();
