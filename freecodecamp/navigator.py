def navigate(commands: list[str]) -> str:
    history = ["Home"]
    current = 0
    for command in commands:
        if command.startswith("Visit"):
            new_page = " ".join(command.split(" ")[1:])
            history = history[: current + 1]
            history.append(new_page)
            current += 1
        elif command == "Forward" and current < len(history) - 1:
            current += 1
        elif command == "Back" and current > 0:
            current -= 1

    return history[current]


print(
    navigate(
        [
            "Visit About Us",
            "Visit Visit Us",
            "Forward",
            "Visit Contact Us",
            "Back",
            "Forward",
        ]
    )
)
