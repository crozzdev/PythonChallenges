def jbelmu(text: str) -> str:
    text_list = text.split(" ")
    new_text_list = []

    for word in text_list:
        if len(word) > 3:
            sub_letters_sorted = "".join(sorted(word[1:-1]))
            word = word[0] + sub_letters_sorted + word[-1]

        new_text_list.append(word)

    return " ".join(new_text_list)
