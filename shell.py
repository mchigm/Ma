import m

while True:
    text = input("basic > ")
    result, error = m.run(text)

    if error: print(error.as_string())
    else: print(result)
