hex_colour_code = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000",
               "brown": "#a52a2a", "CadetBlue": "#5f9ea0", "chocolate": "#d2691e", "DarkSalmon": "#e9967a",
                "DarkKhaki": "#bdb76b", "CornflowerBlue": "#6495ed"}


colour = input("Enter colour: ")
while colour != "":
    if colour in hex_colour_code:
        print("Hex of ",colour, "is", hex_colour_code[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")
