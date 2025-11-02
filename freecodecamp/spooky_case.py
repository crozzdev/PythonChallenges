import re


def spookify(s: str) -> str:
    s = re.sub(r"[_-]", "~", s)
    new_s_list = []
    should_upper = True

    for char in s:
        if char == "~":
            new_s_list.append(char)
        else:
            new_s_list.append(char.upper() if should_upper else char.lower())
            should_upper = not should_upper

    return "".join(new_s_list)


print(spookify("hello_world"))
