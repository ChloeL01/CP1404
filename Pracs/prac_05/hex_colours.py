"""
CP1404/CP5632 Hex coloring

"""

NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Alizarin crimson": "#e32636", "Amber": "#ffbf00",
                "Banana Mania": "#fae7b5", "Bright Green": "#66ff00", "Bulgarian Rose": "#480607",
                "Chocolate": "#d2691e", "Coffee": "#6f4e37", "DarkOrchid": "#9932cc", "DarkViolet": "#9400d3"}
print("The color's that are available are:")
for name in NAME_TO_CODE.keys():
    print(f"{name}", end=", ")
print("")

color_name = input("Enter name of color to get the code: ").title()
while color_name != "":
    try:
        print(color_name, "is", NAME_TO_CODE[color_name])
    except KeyError:
        print("Invalid name of color")
    color_name = input("Enter name of color to get the code: ").title()

