"""
Dictionaries - More Exercises
Check your code: https://judge.softuni.bg/Contests/Practice/Index/1738#3

SUPyF2 Dict-More-Ex. - 04. Snowwhite

Problem:
Snow White loves her dwarfs, but there are so many and she doesn't know how to order them.
Does she order them by name? Or by color of their hat? Or by physics? She can't decide,
so its up to you to write a program that does it for her.
You will be receiving several input lines which contain data about dwarfs in the following format:
{dwarfName} <:> {dwarfHatColor} <:> {dwarfPhysics}
The dwarfName and the dwarfHatColor are strings. The dwarfPhysics is an integer.
You must store the dwarfs in your program. There are several rules though:
•	If 2 dwarfs have the same name but different color, they should be considered different dwarfs,
and you should store both of them.
•	If 2 dwarfs have the same name and the same color, store the one with the higher physics.
When you receive the command "Once upon a time", the input ends.
You must order the dwarfs by physics in descending order and then by total count of dwarfs with the same hat color
in descending order.
Then you must print them all.
Input
•	The input will consists of several input lines, containing dwarf data in the format, specified above.
•	The input ends when you receive the command "Once upon a time".
Output
•	As output you must print the dwarfs, ordered in the way , specified above.
•	The output format is: ({hatColor}) {name} <-> {physics}
Constraints
•	The dwarfName will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
•	The dwarfHatColor will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
•	The dwarfPhysics will be an integer in range [0, 231 – 1].
•	There will be no invalid input lines.
•	If all sorting criteria fail, the order should be by order of input.
•	Allowed working time / memory: 100ms / 16MB.

Examples:
Input:
Pesho <:> Red <:> 2000
Tosho <:> Blue <:> 1000
Gosho <:> Green <:> 1000
Sasho <:> Yellow <:> 4500
Prakasho <:> Stamat <:> 1000
Once upon a time

Output:
(Yellow) Sasho <-> 4500
(Red) Pesho <-> 2000
(Blue) Tosho <-> 1000
(Green) Gosho <-> 1000
(Stamat) Prakasho <-> 1000

Input:
Pesho <:> Red <:> 5000
Pesho <:> Blue <:> 10000
Pesho <:> Red <:> 10000
Gosho <:> Blue <:> 10000
Once upon a time

Output:
(Blue) Pesho <-> 10000
(Blue) Gosho <-> 10000
(Red) Pesho <-> 10000
"""


class Dwarf:
    def __init__(self, name: str, hat_color: str, physics: int):
        self.name = name
        self.hat_color = hat_color
        self.physics = physics
        self.color_count = 0


all_dwarfs = []
colors = {}

while True:
    data = input().split(" <:> ")
    if data[0] == "Once upon a time":
        break
    dwarf_name = data[0]
    dwarf_hat_color = data[1]
    dwarf_physics = int(data[2])

    dwarf_is_present = False
    for dwarf in all_dwarfs:
        if dwarf.name == dwarf_name and dwarf.hat_color == dwarf_hat_color:
            dwarf_is_present = True
            if dwarf_physics > dwarf.physics:
                dwarf.physics = dwarf_physics
    if not dwarf_is_present:
        new_dwarf = Dwarf(name=dwarf_name, hat_color=dwarf_hat_color, physics=dwarf_physics)
        all_dwarfs.append(new_dwarf)
    if dwarf_hat_color not in colors:
        colors[dwarf_hat_color] = 1
    elif dwarf_hat_color in colors and not dwarf_is_present:
        colors[dwarf_hat_color] += 1

for dwarf in all_dwarfs:
    for color, value in colors.items():
        if dwarf.hat_color == color:
            dwarf.color_count = value

for dwarf in sorted(all_dwarfs, key=lambda x: (-x.physics, -x.color_count)):
    print(f"({dwarf.hat_color}) {dwarf.name} <-> {dwarf.physics}")
