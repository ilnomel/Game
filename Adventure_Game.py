room_list = []

# [["room description"], [north], [west], [south], [east]]

# Starting room: Bedroom 2
room = ["Bedroom 2", 3, None,None,1]
room_list.append(room)

# South hall
room = ["South Hall",4,0,None,2]
room_list.append(room)

# Dining room
room = ["Dining Room",5,1,None,None]
room_list.append(room)

# Bedroom 1
room = ["Bedroom 1",None,None,0,4]
room_list.append(room)

# North hall
room = ["North Hall",6,3,1,5]
room_list.append(room)

# Kitchen
room = ["Kitchen",None,4,2,None]
room_list.append(room)

# Balcony
room = ["Balcony",None,None,4,None]
room_list.append(room)

current_room = 0
next_room = 0
user_input = 0
done = False

print("\nYou are in a room in a castle. There is a passage to the north.")


# dictionary.com xD
room_desc = {"Balcony": "You are on the balcony, looking out to the garden",
             "Bedroom 2": "You are in a nice bedroom. But there are no windows",
             "Bedroom 1": "You are in a nice bedroom. It has a big window that looks out to the garden",
             "North Hall": "You are in a well lit hallway. There is passage to the north, west, south, and east",
             "South Hall": "You are in a well lit hallway. There is passage to the north, west, and east",
             "Kitchen": "You are in the kitchen. It's not very neat",
             "Dining Room": "You are in a big dining room. The chandalier looks beautiful"}

while not done:
    # match room to desription
    print(room_desc[room_list[current_room][0]])
    
    user_input = input("Which way do you want to go? " ) 

    # Starting from Bedrooom 2
    # going to bedroom 1
    if user_input == "n":
        next_room = room_list[current_room][1] #3
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print("You are in %s." %room_list[current_room][0])
            
            
    elif user_input == "w":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print("You are in %s." %room_list[current_room][0])
        
    elif user_input == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room 
            print("You are in %s." %room_list[current_room][0])
    
    # go to the south hall    
    elif user_input == "e":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
            print("You are in %s." %room_list[current_room][0])
            
    