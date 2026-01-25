while True:
    text = input("Type something(Type 'stop'  to quit):")
    if text.lower()== "stop":
        print("Loop stopped!")
        break
    print("You enterd:" , text)