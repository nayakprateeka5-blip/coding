data = {"a": 1, "b": 2, "c": 3, "d": 4}

result = {key: value for key, value in data.items() if value > 2}

print(result)
