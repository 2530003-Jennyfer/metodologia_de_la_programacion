def format_full_name(full_name: str):
    if full_name is None:
        print("Error: invalid input")
        return None
    normalized = full_name.strip()
    if not normalized:
        print("Error: invalid input")
        return None
    # Collapse multiple internal spaces
    parts = [p for p in normalized.split() if p]
    if len(parts) < 2:
        print("Error: invalid input")
        return None
    # Title case each part
    title_name = " ".join(p.title() for p in parts)
    # Build initials like J.C.T.
    initials = ".".join(p[0].upper() for p in parts) + "."
    print(f"Formatted name: {title_name}")
    print(f"Initials: {initials}")
    return title_name, initials
