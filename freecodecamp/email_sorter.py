def sort(emails: list[str]) -> list:
    return sorted(
        emails, key=lambda email: tuple(part.lower() for part in email.split("@")[::-1])
    )


print(sort(["jill@mail.com", "john@example.com", "jane@example.com"]))
