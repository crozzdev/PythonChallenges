def format(seconds:int) -> str:


    if seconds < 60:
        return f"0:{seconds:02d}"
    elif seconds < 3600:
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"
    else:
        hours = seconds // 3600
        remaining_seconds = seconds % 3600
        minutes = remaining_seconds // 60
        secs = remaining_seconds % 60
        return f"{hours}:{minutes:02d}:{secs:02d}"

