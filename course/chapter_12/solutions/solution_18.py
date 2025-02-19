def user_info(name, **kwargs):
    l = [f"Имя: {name}"]
    for key, value in kwargs.items():
        l.append(f"{key}: {value}")
    return "\n".join(l)