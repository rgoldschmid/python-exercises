def type_name(value):
    return type(value).__name__


def group(*members):
    joined = ", ".join(members)
    print(f"Members given as {type_name(members)}: {joined}")


def log(**parameters):
    tokens = []
    for key, value in parameters.items():
        tokens.append(f"{key}: {value}")
    print(f"Arguments given as {type_name(parameters)}: " + ", ".join(tokens))


if __name__ == '__main__':
    group("Tina", "Katharina", "Sarah")
    log(name="Yoda", height=66)
