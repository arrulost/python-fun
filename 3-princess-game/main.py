print('''
                            _____
             ,             /@@@@@=-
             \\            @@@@@@@@@@=-
             \\          _\@/\@@@@@=-
 Journey to...\\        /_ +\ \@@@@@=-
        ,      \\      (_/   )  \@@@@=-
        \\      \\     (_____)    \@@=-
        _\\_/\_ _\\__  /     \     ~~
  ____,/+-  `/\\  { \_|___(__ )
 >             \\  )_|/  ___  \
 \_/--\___/     \\.` / <-q-p-> \
    _//   )      \(\/\ <-d-b-> /___
 _____  /         \/ \  \|/  //   \__
 /     \/          /   \_____//     \_\
 | /\_  |         (_  /______\\     |||
 | \_ | |         | \|   <    \\    /||
 \_\_\ \/     ____\  |____\    \)  / ||
       /    _/  <____)\    (      / //\\
      /   _/           \    \    (  \\//
     (   /              )  / \    \  \/
     /  /              /  /   \    )
 ---/  / The Realm ---/  /-----)  /-----
  _/__/ of Chaos!   _/__/     /  /
 /__/ Again & Again/__/     _/__/
                           /__/
''')
print("Welcome to Can you save the Princess Game.")
print("Your mission is to find the princess.")

dragon = input(
    "You start the journey... and in your path you see a dragon. What do you do? Type 'hide' or 'kill'. "
).lower()
if dragon == "kill":
    print("You killed the dragon, you can continue your adventure.")
    house = input(
        "It's getting dark, you need to get some rest, you see a house in the middle of the forest. What do you do? Type 'go in' or 'keep going'."
    ).lower()
    if house == "go in":
        print(
            "The people welcomed you and they gave you warm food. You can continue your adventure."
        )
        princess = input(
            "You found the castle where the princess is hidded, you need to choose now a door. Type 'red' or 'blue' or 'yellow'."
        ).lower()
        if princess == "yellow":
            print(
                "Congratulation!!!, you saved the princess and you return to the kindom as a hero."
            )
        elif princess == "red":
            print("It's a room full of snakes and they bite you. GAME OVER.")
        else:
            print("This is the room of the bad guy, he killed you. GAME OVER.")
    else:
        print("You freezed and died outside. GAME OVER.")
else:
    print("The dragon smelled you, and killed you. GAME OVER.")