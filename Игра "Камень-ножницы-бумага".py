def winner(p1, p2):
    match (p1, p2):
        case (a, b) if a == b:
            return "Ничья"
        case ("камень", "ножницы") | ("ножницы", "бумага") | ("бумага", "камень"):
            return "Игрок 1"
        case _:
            return "Игрок 2"

print(winner("камень", "ножницы"))  # Игрок 1
print(winner("бумага", "бумага"))   # Ничья