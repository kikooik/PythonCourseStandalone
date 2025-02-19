def generate_report(name, *args, **kwargs):
    l = [f"Отчёт для {name}"]
    z = ", ".join(args)
    l.append(f"Выполненные задачи: {z}")
    for key, value in kwargs.items():
        l.append(f"{key}: {value}")
    return "\n".join(l)