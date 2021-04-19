# Dalton Stout

import time  # time module used for timestamp
from random import randint  # used to pull random strings from dictionaries

#  gives each location a map coordinate
map_locations = {
    "Aosta": [-2, 4],
    "Turin": [-2, 3],
    "Genoa": [-2, 2],
    "Cagliari": [-2, -2],
    "Palermo": [-2, -3],
    "Milan": [-1, 3],
    "Balogna": [-1, 2],
    "Florence": [-1, 1],
    "Rome": [-1, -1],
    "Naples": [-1, -2],
    "Catanzaro": [-1, -3],
    "Perugia": [0, 0],
    "Air Balloon Park": [0, -2],
    "Venice": [1, 2],
    "Acona": [1, 1],
    "L'Aquilla": [1, -1],
    "Campo Bosso": [1, -2],
    "Potenza": [1, -3],
    "Trento": [2, 3],
    "Trieste": [2, 2],
    "Bari": [2, -3],
    "Vienna": [3, 3],
    "exit": [50, 50],
    "Detention Center": [-50, -50]
}

#  for movement input, used for input validation
directions = {
    'north',
    'east',
    'south',
    'west',
    'northeast',
    'southeast',
    'southwest',
    'northwest',
    'exit',
    'deten return',
    'air balloon return to naples'
}

#  for air balloon park input validation
air_balloon_directions = {
    'northeast',
    'east',
    'southeast'
}

#  literal scripts, will be called and printed only
opening_script = [
    "Ode No!",
    "by Dalton Stout",
    "Press enter to begin.",
    "May 1824, Vienna",
    "One day, Beethoven is touring the Theater am Kärntnertor in Vienna in preparation for the premiere of his biggest",
    "work: his 9th symphony. He needed make sure everything was in order to house the biggest orchestra yet seen!",
    "After a very successful dress rehearsal with the ensemble, Beethoven departs Vienna and returns to his summer",
    "home in Aosta, Italy. Here, he will relax and prepare for the big day.",
    "Press enter to continue.",
    "May 1824, Aosta, Italy",
    "Beethoven finally returns to his house. After much traveling, he is weary and has his servo unpack his things.",
    "\"Bring me my manuscript notebook so I may study for my premiere. This audience is not going to be forgiving!\" "
    "Beethoven anxiously grumbles.",  # CONT
    "\"Signore, there was no notebook in your luggage. Perhaps it is in your bag?\" The servo says, handing Beethoven"
    " his bag.",  # CONT
    "Beethoven begins frantically searching through his bag to find... nothing!",
    "\"It must have fallen out when those birds attacked me in Perugia! "
    "Those pages are likely scattered all over Italy",
    " by now! I better start looking if I am going to make it to my premiere on time!\"",
    "Beethoven grabs his bag and sets off to find his missing manuscripts.",
    "Type your name to begin your journey: "
]

final_script = [
    "Theater am Kärntnertor, Vienna",
    "",
    "Beethoven arrives in Vienna with no time to spare! He runs in to the theater to see the ensemble waiting on the "
    "stage for him to arrive.",  # CONT
    "\"Ah signor, you made it!\" exclaims the stage manager. "
    "\"The concert master has been improvising for far too long!\"",  # CONT
    "The manager nods to the violinist, who wraps up their solo and begins tuning the ensemble. Beethoven walks on to "
    "stage and the audience roars.",
    "He bows and anxiously takes the podium. The downbeat is given and the orchestra is off!",
]

losing_scene = [
    "The choir is just about to enter when Beethoven turns the page and... he is missing pages! "
    "He cues the choir",
    "at the wrong time and the entire ensemble falls apart. The music now is unbearable. Loud booing is coming",
    " from the audience as patrons get up and leave. Beethoven bows and walks off the "
    "stage in shame.",
    "He returns home and passes away in his bed that night, forever living in the shame of a failed career.",
]

winning_scene = [
    "The energy in the room is electric. The piece comes to a dramatic end and the audience goes wild! The cheering "
    "seems to never cease.",
    "Beethoven bows many times and recognizes nearly each member of the ensemble. This is certainly a night no one will"
    " soon forget!",
    "The next day, Beethoven's name is in every newspaper. He spends the next three years touring and conducting his "
    "now most popular symphony.",
    "Beethoven passes away in his bed in 1827, having lived an extremely successful career as a musician and composer."
]

#  dictionary for messages based on location
location_messages = {
    # dict for storyline communication
    'dialogue': {
        "Aosta": [
            "Beethoven: I must hurry. The concert date is fast approaching!",
            "Beethoven: Those State Police were aggressive! I should stay in Italy for now.",
        ],
        "Turin": [
            "Turin is the birthplace of solid chocolate, it can be traced back to 1560."
        ],
        "Genoa": [
            "The mediterranean air and the beautiful ocean view are begging you to stay!",
        ],
        "Cagliari": [
            "The seat of the Roman Catholic archdiocese of Sardinia, from the 5th century AD."
        ],
        "Palermo": [
            "Prehistoric settlements in the area are said to date back to 8,000 BC, "
            "with the first significant civilisation being the Phoenicians."
        ],
        "Milan": [
            "The city of Milan was founded more than 2,500 years ago, in 600 BC, by a Celtic tribe from Gaul."
        ],
        "Balogna": [
            "Named after the fall of the Roman Empire before becoming a frontier outpost of the Byzantine Exarchate"
        ],
        "Florence": [
            "Leonardo da Vinci, Michelangelo, Raphael, and Galileo are all from Florence.",
        ],
        "Rome": [
            "The Romans had built a road network of 53,000 miles by the early fourth century, "
            "giving birth to the saying All roads lead to Rome."
        ],
        "Naples": [
            "Under the city, you’ll find catacombs, old burial sites located below the ground."
            " They contain more than 2,000 burial coves, and 500 sarcophagi"
        ],
        "Catanzaro": [
            "Home of the Basilica of the Immaculate. Named for its magnificent artwork and marbling."
        ],
        "Perugia": [
            "In the 15th century it was home to painter Bernardino Pinturicchio and his master Pietro Vannucci"
            ", who would later teach the Raphael."
        ],
        "Air Balloon Park": [
            "Welcome to the Air Balloon Park! "
        ],
        "Venice": [
            "The city rests on 118 islands separated by 150 canals which are mainly used used for transportation."
        ],
        "Acona": [
            "In the Middle Ages, it was one of the five cities of the Maritime Pentapolis"
            " under the Byzantine exarchate of Ravenna."
        ],
        "L'Aquilla": [
            "Notable buildings include the churches of San Bernardino, the mausoleum of St. Bernardine of Siena,"
            " and Santa Maria di Collemaggio"
        ],
        "Campo Bosso": [
            "The Castello Monforte remains in the old town, which also has the Romanesque churches"
            " of San Bartolomeo and San Giorgio."
        ],
        "Potenza": [
            "Potenza was an important road junction and became a flourishing Roman community."
        ],
        "Trento": [
            "The peaceful atmosphere is very relaxing. You almost forgot you need to keep searching for manuscripts!"
        ],
        "Trieste": [
            "A Roman city known for its wine. The Venetians were often at war with Vienna."
        ],
        "Bari": [
            "Home of Saint John's Basilica, where Saint John's body lays to rest."
        ],
        "Vienna": [
            ""
        ],
        "exit": [
            ""
        ],
        "Detention Center": [
            '',  # the Aosta message call key updates and will crash the game if this blank item is not here
            "You need a passport to leave the country!"
        ]
    },
    # dict to tell the user where they can go
    'may_go': {
        "Aosta": "You may go South to Turin.",
        "Turin": "You may go North to Aosta, South to Genoa, or East to Milan.",
        "Genoa": "You may go North to Turin or East to Balogna.",
        "Cagliari": "You may go East to Naples or South to Palermo.",
        "Palermo": "You may sail North to Cagliari or East to Catanzaro.",
        "Milan": "You may go South to Balogna, or West to Turin.",
        "Balogna": "You may go North to Milan, South to Florence, or West to Genoa.",
        "Florence": "You may go North to Balogna or Southeast to Perugia.",
        "Rome": "You may go Northeast to Perugia, or South to Naples. ",
        "Naples": "You may go North to Rome, South to Catanzaro, or West to Cagliari. "
                  "Head East to find the Air Balloon Park",
        "Catanzaro": "You may go north to Naples or sail West to Palermo.",
        "Perugia": "You may go Northwest to Florence, Northeast to Acona, "
                   "Southeast to L'Aquilla, or Southwest to Rome. ",
        "Air Balloon Park": "We offer rides Northeast to L'Aquilla, "
                            "East to Campo Bosso, and "
                            "Southeast Potenza.",
        "Venice": "You may take a gondola East to Trieste or South to Acona.",
        "Acona": "You may go Southwest to Perugia or take a gondola North to Venice.",
        "L'Aquilla": "You may go Northwest to Perugia, or South to Campo Bosso. "
                     "You may also head West to return to Naples.",
        "Campo Bosso": "You may go North to L'Aquilla, or South to Potenza. "
                       "You may also head West to return to Naples.",
        "Potenza": "You may go North to Campo Bosso, or East to Bari. "
                   "You may also head West to return to Naples.",
        "Trento": "You may go South to Trieste or East to Vienna.",
        "Trieste": "You may go North to Trento or take a gondola West to Venice.",
        "Bari": "You may go West to Potenza.",
        "Vienna": "PIANO BATTLE BOOM BOOM SLAP POW",
        "exit": "Thank you for playing!",
        "Detention Center": "The State Police have detained you and will transport you back to Aosta."
    },
    # lists messages for manuscript collection (must be a list to be iterated through)
    'manuscript': [
        ['You see the corner of a paper sticking out from under a rock.',
         'Do you investigate?',
         'You lift up the rock... and find a manuscript page!'],
        ['An old lady is calling to get your attention.',
         'Talk to her?',
         "'Beethoven! I found this in my cat house and knew it belonged to you.' "
         'The old lady hands you a manuscript page!'],
        ['A crumpled paper blows across the road.',
         'Chase it down?',
         'It blows away a few times before you catch it. You uncrumple it to find a manuscript page!'],
        ['You hear the sweet chirping of a sparrow. As you look over, you notice something strange in its nest!',
         'Check it out?',
         'The sparrow did NOT like you near its nest. You manage to wave it off and find a manuscript page!'],
        ['After stopping for food, you see something familiar in the wastebasket.',
         'Reach for it?',
         'Under a rotting banana and some old bread you find a manuscript page! People are staring...'],
        ['You pause to enjoy the babbling creek and see something floating downstream.',
         'Fish for it?',
         'You found a manuscript page! After letting it dry in the sun, you are ready to go.'],
        ['A familiar tune is coming from the church.',
         'Follow your ears?',
         'The organist is playing your music! You tell him the story and he gives you the manuscript page.'],
        ['You are appreciating some flowers when you notice something in the dirt.',
         'Start digging?',
         "You found a manuscript page! Hopefully the groundskeeper doesn't notice the missing dahlias..."],
        ['You notice something caught on a fence, blowing in the wind.',
         'Go see what it is?',
         "You carefully pull the paper off the fence. It's a manuscript page!"],
    ],
    # dialogue for boat pass scene
    'boat_pass': [
        "Old man: \"You sir! You over there! You look like a traveler. "
        "Might you be interested in helping an old man relive his glory days?\"",
        "\"There's something in it for you if you do!\" ",
        "Would you like to hear a story? ",
        "\"Alright, then. Come back if you change your mind!\" ",
        "\"I'll tell you a story but I will need your help remembering some details.\" ",
        "\"I loved going to the Saint Nicholas Basilica growing up. It's in a big port called...\" ",
        "Do you know the name of that city? ",
        "\"Ah, yes! I remember now. Saint Nicholas's body is really in there, you know!\"  ",
        "\"Thanks for your help, Beethoven! Here, this should help your travels.\" ",
        "You received a boat pass from the old man! ",
        "\"No, that doesn't seem quite right. I know it will jog my memory when I hear it!\"  ",
        "\"I know it was South of here... Come back when you find it!\"  ",
        "\"Great! What city was it?\" ",
        "That city is ",
        "Old man: \"You're back!\" ",
        "\"Have you found the Saint Nicholas Basilica yet?\" ",
    ]
}

#  dictionary for random messages for input prompt
move_messages = [
    "Which direction should I go? ",
    "Where to next? ",
    "What way now? "
]

# misc messages for special features
misc_message = {
    "detention_message": "Press enter to return to Aosta.",
    "air_balloon_message": "Where will you take the balloon? ",
    "air_balloon_error": "We're sorry. We don't offer rides to that location. "
                         "Please choose a location from our list. ",
    "safe_keeping": 'You should put it in your bag for safe keeping.',
    "need_boat_pass": 'You need a boat pass to sail! Try a different direction. '
}

# initialize pre-function variables for the game
game_title = 'Ode No!'
manu_count = 0  # user starts with 0 manuscripts
manu_total = 9  # how many manus to collect to win the game
has_won = False  # updated when player arrives in Vienna
detained = False  # updated when player leaves the map
manu_message_key = 0  # updated randomly to pull manu prompts from the dictionary
has_boat_pass = False  # updated when the player receives the boat pass in game
boat_pass_scene = 0  # updated to control the dialogue with the old man
box_height = 10  # adjust for box height
box_width = 150  # adjust for box width
border = '|{}|'.format('-' * box_width)  # creates the top/bottom border, called to print
blank_line = '|{}|\n|{}|'.format(' ' * box_width, ' ' * box_width)  # a spacer in the HUD, called to print

# variables for manuscripts, will be set to true when collected
manuscripts = {
    'Turin': False,
    'Milan': False,
    'Balogna': False,
    'Florence': False,
    'Rome': False,
    'Naples': False,
    'Palermo': False,
    'Potenza': False,
    'Campo Bosso': False,
    'Acona': False,
    'Venice': False,
    'Trento': False
}


# stopwatch program, called only in timestamp()
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    if hours <= 1:
        time_stamp = f"Time Lapsed: {int(mins):02d}:{int(sec):02d}"
    else:
        time_stamp = f"Time Lapsed: {int(hours):02d}:{int(mins):02d}:{int(sec):02d}"
    return time_stamp


# duration of gameplay timestamp, called every time player_update() is called
def timestamp():
    time_lapsed = (time.time()) - start_time
    time_stamp = time_convert(time_lapsed)
    return time_stamp


# allows us to do math to the key values before calling the key, used for movement
def get_key(val):
    for key, value in map_locations.items():
        if val == value:
            return key
    return "key doesn't exist"


# updates the player's location based on the directional input
def move(direction):
    global location
    if direction == "north":
        location[1] += 1
    if direction == "south":
        location[1] -= 1
    if direction == "east":
        location[0] += 1
    if direction == "west":
        location[0] -= 1
    if direction == "northeast":
        location[0] += 1
        location[1] += 1
    if direction == "southeast":
        location[0] += 1
        location[1] -= 1
    if direction == "southwest":
        location[0] -= 1
        location[1] -= 1
    if direction == "northwest":
        location[0] -= 1
        location[1] += 1
    if direction == 'exit':
        location = [50, 50]
    if direction == 'deten_return':
        location = [-2, 4]
    if direction == 'air_balloon_return_to_naples':
        location[0] = -1
        location[1] = -2


# gets the user input for next move and passes it to move()
def move_input():
    move_key = randint(0, (len(move_messages) - 1))  # pulls a random string from the move_messages list
    #  dicts used for input validation
    air_balloon_destinations = {
        "L'Aquilla",
        "Campo Bosso",
        "Potenza"
    }
    cant_sail = {  # referenced to check boat pass
        "Naples": ['west'],
        "Catanzaro": ['west'],
        "Acona": ['north']
    }

    if map_key == "Detention Center":  # force the player to Aosta with any input
        input(f"|{misc_message['detention_message']}")
        player_move = "deten_return"
        move(player_move)
        return
    if map_key in air_balloon_destinations:  # lets the player ride the air balloon back to Naples
        player_move = (input(f"|{move_messages[move_key]}").strip().lower().replace(" ", ""))
        if player_move == 'west':  # set location to Naples because Air Balloon
            player_move = "air_balloon_return_to_naples"
        move(player_move)
        return
    if map_key == "Air Balloon Park":  # extra input valid. for air balloon park
        player_move = (input(f"|Where would you like to ride? ").strip().lower().replace(" ", ""))
        while player_move not in air_balloon_directions:
            player_move = (input(f"|{misc_message['air_balloon_error']}").strip().lower().replace(" ", ""))
        move(player_move)
        return
    if not has_boat_pass:  # requires boat pass to sail, this is the one part of code I am not happy with
        if map_key in cant_sail:
            if cant_sail[map_key][0] == 'west':
                player_move = (input(f"|{move_messages[move_key]}").strip().lower().replace(" ", ""))
                while player_move == 'west':
                    player_move = (input(f"|{misc_message['need_boat_pass']}").strip().lower().replace(" ", ""))
                while player_move not in directions:
                    player_move = (input("|Maybe I should check my map again... ").strip().lower().replace(" ", ""))
                    if not has_boat_pass:  # requires boat pass to sail
                        while player_move == 'west':
                            player_move = (input(f"|{misc_message['need_boat_pass']}").strip().lower().replace(" ", ""))
                move(player_move)
                return
            if cant_sail[map_key][0] == 'north':
                player_move = (input(f"|{move_messages[move_key]}").strip().lower().replace(" ", ""))
                while player_move == 'north':
                    player_move = (input(f"|{misc_message['need_boat_pass']}").strip().lower().replace(" ", ""))
                while player_move not in directions:
                    player_move = (input("|Maybe I should check my map again... ").strip().lower().replace(" ", ""))
                    if not has_boat_pass:  # requires boat pass to sail
                        while player_move == 'north':
                            player_move = (input(f"|{misc_message['need_boat_pass']}").strip().lower().replace(" ", ""))
                move(player_move)
                return
    player_move = (input(f"|{move_messages[move_key]}").strip().lower().replace(" ", ""))
    while player_move not in directions:  # input validation
        player_move = (input("|Maybe I should check my map again... ").strip().lower().replace(" ", ""))
    move(player_move)
    return


# to be called every time the player completes an action, updates HUD
def player_update(item='none'):

    global manuscripts
    global manu_count
    global manu_total
    global manu_message_key
    global has_boat_pass
    x = 0

    # This stuff looks scary but it's just formatting the 'HUD'
    global box_height
    global box_width
    global border
    global blank_line
    manu_print = f"|{'Collected Manuscripts: ' + str(manu_count) + '/9':>{box_width - 1}} |"
    boat_pass_print = f"|{'Boat Pass':>{box_width - 1}} |"
    loc_display = '{}, Italy'.format(map_key)
    loc_key = 0
    if detained:  # displays a different message in Aosta if player was just detained
        loc_key = 1
    time_display = str(timestamp())
    header = f'|{game_title:<{len(game_title)}}{player_name:>{box_width - len(game_title)}}|'
    subheader = f"| {time_display:<{len(time_display)}}{'BAG':>{(box_width - 2) - len(time_display)}} |"
    loc_line = f'|{loc_display:^{box_width}}|'
    loc_message = f"| {location_messages['dialogue'][map_key][loc_key]:<{box_width - 1}}|"
    next_loc = f"| {location_messages['may_go'][map_key]:<{box_width - 1}}|"
    bag = [
        manu_print
    ]
    if len(location_messages['manuscript']) <= 1:  # if randint(0, 0) is called below it returns an error
        get_manu_message_key = 0
    else:
        get_manu_message_key = randint(0, (len(location_messages['manuscript']) - 1))  # pulls a random string from dict

    # The order in which to build the HUD, extended with decision branching below
    print_list = [
        border,
        header,
        subheader,
        blank_line,
        loc_line,
        blank_line,
    ]
    # handles HUD for bag
    if has_boat_pass:
        bag.extend([boat_pass_print])
    thing = 0
    bag.reverse()  # because of .insert, it needs to loop backwards through the bag
    while thing < len(bag):
        print_list.insert(3, bag[thing])
        thing += 1

    # HUD code for collecting items, passed when func is called in has_won loop
    if item == 'none':
        print_list.extend([loc_message, blank_line, next_loc])
    elif item == 'manu':
        # get_manu_message_key will update every time player_update() is called
        # This only updates manu_message_key when a new manu is discovered
        manu_message_key = get_manu_message_key
        manu_message = f"| {(location_messages['manuscript'][manu_message_key][0]):<{box_width - 1}}|"
        print_list.extend([manu_message])
    elif item == 'manu_collected':
        manu_collected_message1 = f"| {(location_messages['manuscript'][manu_message_key][2]):<{box_width - 1}}|"
        manu_collected_message2 = f"| {(misc_message['safe_keeping']):<{box_width - 1}}|"
        print_list.extend([manu_collected_message1, manu_collected_message2])
    if item == 'boat_pass':
        if boat_pass_scene == 0:  # first time meeting old man
            pass_key = 0
            while pass_key < 2:
                boat_pass_dialogue = f"| {(location_messages['boat_pass'][pass_key]):<{box_width - 1}}|"
                print_list.extend([boat_pass_dialogue])
                pass_key += 1
        if boat_pass_scene == 1:  # accepted quest
            pass_key = 4
            while pass_key < 6:
                boat_pass_dialogue = f"| {(location_messages['boat_pass'][pass_key]):<{box_width - 1}}|"
                print_list.extend([boat_pass_dialogue])
                pass_key += 1
        if boat_pass_scene == 2:  # yes the players knows the answer
            pass_key = 12
            boat_pass_dialogue = f"| {(location_messages['boat_pass'][pass_key]):<{box_width - 1}}|"
            print_list.extend([boat_pass_dialogue])
        if boat_pass_scene == 3:  # wrong answer
            pass_key = 10
            while pass_key < 12:
                boat_pass_dialogue = f"| {(location_messages['boat_pass'][pass_key]):<{box_width - 1}}|"
                print_list.extend([boat_pass_dialogue])
                pass_key += 1
            print_list.extend([blank_line, next_loc])
        if boat_pass_scene == 4:  # right answer
            pass_key = 7
            while pass_key < 10:
                boat_pass_dialogue = f"| {(location_messages['boat_pass'][pass_key]):<{box_width - 1}}|"
                print_list.extend([boat_pass_dialogue])
                pass_key += 1
            boat_pass_dialogue = f"| {(misc_message['safe_keeping']):<{box_width - 1}}|"
            print_list.extend([boat_pass_dialogue])
        if boat_pass_scene == 5:  # player left and returned
            pass_key = 14
            boat_pass_dialogue = f"| {(location_messages['boat_pass'][pass_key]):<{box_width - 1}}|"
            print_list.extend([boat_pass_dialogue])
        if boat_pass_scene == 6:  # player answers no
            pass_key = 11
            boat_pass_dialogue = f"| {(location_messages['boat_pass'][pass_key]):<{box_width - 1}}|"
            print_list.extend([boat_pass_dialogue, blank_line, next_loc])
        if boat_pass_scene == 7:  # player answers no in first question
            pass_key = 3
            boat_pass_dialogue = f"| {(location_messages['boat_pass'][pass_key]):<{box_width - 1}}|"
            print_list.extend([boat_pass_dialogue, blank_line, next_loc])

    # loops through the print list to print it
    while x < len(print_list):
        print(print_list[x])
        x += 1

    # fills the rest of the HUD box
    while x < box_height:
        print(blank_line)
        x += 2
    print(border)

    # 'under the hood' stuff for features, calls respective funcs
    if item == 'none':
        move_input()
    elif item == 'manu':
        manu_collect(manu_message_key)
    elif item == 'manu_collected':
        input("|Press enter to put it in your bag.")
        manu_count += 1
        del location_messages['manuscript'][manu_message_key]
    elif item == 'boat_pass':
        play_boat_pass_scene(boat_pass_scene)
    print('\n\n')


# called when collecting manus
def manu_collect(key):
    global manu_count
    manu_responses = ['yes', 'no']  # input validation
    manu_message = f"|{(location_messages['manuscript'][key][1])} "
    player_response = (input(manu_message).strip().lower().replace(" ", ""))
    while player_response not in manu_responses:
        player_response = (input("|I'm in a hurry. "
                                 "It's best to make a decision now! ").strip().lower().replace(" ", ""))
    else:
        if player_response == 'yes':
            print('\n\n\n')
            player_update(item='manu_collected')
            manuscripts[map_key] = True
        if player_response == 'no':
            print('\n\n\n')
            player_update()


# called when talking to the old man about boat pass
def play_boat_pass_scene(scene):
    global boat_pass_scene
    global has_boat_pass
    boat_pass_scene_accept = ['yes', 'no']
    answer = 'bari'

    if scene == 0:  # first meet old man
        player_response = input(f"|{location_messages['boat_pass'][2]}").strip().lower().replace(" ", "")
        print('\n\n\n')
        while player_response not in boat_pass_scene_accept:
            player_response = input("|Hm. I don't understand. What was that again? ").strip().lower().replace(" ", "")
        else:
            if player_response == 'yes':
                boat_pass_scene = 1
                player_update(item='boat_pass')
            if player_response == 'no':
                boat_pass_scene = 7
                player_update(item='boat_pass')
    if scene == 1:  # accepted quest
        player_response = input(f"|{location_messages['boat_pass'][6]}").strip().lower().replace(" ", "")
        print('\n\n\n')
        while player_response not in boat_pass_scene_accept:
            player_response = input("|Hm. I don't understand. What was that again? ").strip().lower().replace(" ", "")
        else:
            if player_response == 'yes':
                boat_pass_scene = 2
                player_update(item='boat_pass')
            if player_response == 'no':
                boat_pass_scene = 6
                player_update(item='boat_pass')
    if scene == 2:  # yes the players knows the answer
        player_response = input(f"|{location_messages['boat_pass'][13]}").strip().lower().replace(" ", "")
        print('\n\n\n')
        if player_response == answer:
            boat_pass_scene = 4
            player_update(item='boat_pass')
        if player_response != answer:
            boat_pass_scene = 3
            player_update(item='boat_pass')
    if scene == 3:  # wrong answer
        player_response = (input(f"|Which way should I start looking? ").strip().lower().replace(" ", ""))
        print('\n\n\n')
        move(player_response)
        boat_pass_scene = 5
    if scene == 4:  # right answer
        input("|Press enter to put it in your bag.")
        print('\n\n\n')
        has_boat_pass = True
        player_update()
    if scene == 5:  # player left and came back
        player_response = input(f"|{location_messages['boat_pass'][15]}").strip().lower().replace(" ", "")
        while player_response not in boat_pass_scene_accept:
            player_response = input("|Hm. I don't understand. What was that again? ").strip().lower().replace(" ", "")
        if player_response == 'yes':
            boat_pass_scene = 2
            player_update(item='boat_pass')
        if player_response == 'no':
            boat_pass_scene = 6
            player_update(item='boat_pass')
    if scene == 6:  # player answers no
        player_response = (input(f"|Which way should I start looking? ").strip().lower().replace(" ", ""))
        print('\n\n\n')
        move(player_response)
        boat_pass_scene = 5
    if scene == 7:  # only player answers no to first question
        player_response = (input(f"|Which way? ").strip().lower().replace(" ", ""))
        print('\n\n\n')
        move(player_response)
        boat_pass_scene = 0
    print('\n\n\n')


#  called when the player arrives in Vienna without enough manu pages, prints script
def lost():
    end_script = [
        border,
        blank_line
    ]
    for key in final_script:
        end_line = f'|{key:^{box_width}}|'
        end_script.extend([end_line])
    for key in losing_scene:
        end_line = f'|{key:^{box_width}}|'
        end_script.extend([end_line])
    for L in end_script:
        print(L)
    print(blank_line)
    print(border)
    input("|Press enter to exit.")
    return


#  called when the player arrives in Vienna without all manu pages, prints script
def won():
    end_script = [
        border,
        blank_line
    ]
    for key in final_script:
        end_line = f'|{key:^{box_width}}|'
        end_script.extend([end_line])
    for key in winning_scene:
        end_line = f'|{key:^{box_width}}|'
        end_script.extend([end_line])
    for L in end_script:
        print(L)
    print(blank_line)
    print(border)
    print("|Congratulations on successfully completing 'Ode No!'")
    return


# opening title!
player_name = ''
has_started = False  # updated after title page
opening_scene1 = False  # updated to progress opening scenes
opening_scene2 = False

#  Title Page
while not has_started:
    # This stuff looks scary but it's just formatting the 'HUD'
    title = f'|{game_title:^{box_width}}|'
    signature = f'|{opening_script[1]:^{box_width}}|'
    begin = f'|{opening_script[2]}'
    i = 0
    opening_print = [
        border,
        blank_line,
        title,
        signature,
        blank_line,
    ]
    print('\n\n\n')
    for line in opening_print:
        print(line)
        i += 1
    while i < box_height:
        print(blank_line)
        i += 2
    print(border)
    input(begin)
    print('\n\n\n')
    has_started = True
    opening_scene1 = True

# Scenes to set up backstory and gameplay
while opening_scene1:
    title = f'|{opening_script[3]:^{box_width}}|'
    script = [
        border,
        blank_line,
        title
    ]
    i = 4
    while i < 8:
        line = f'|{opening_script[i]:^{box_width}}|'
        script.append(line)
        i += 1
    for line in script:
        print(line)
    i = len(script)
    while i < box_height:
        print(blank_line)
        i += 2
    print(border)
    input(f'|{opening_script[8]}')
    print("\n\n\n")
    opening_scene1 = False
    opening_scene2 = True
while opening_scene2:
    title = f'|{opening_script[9]:^{box_width}}|'
    script = [
        border,
        blank_line,
        title
    ]
    i = 10
    while i < 17:
        line = f'|{opening_script[i]:^{box_width}}|'
        script.append(line)
        i += 1
    for line in script:
        print(line)
    i = len(script)
    while i < box_height:
        print(blank_line)
        i += 2
    print(border)
    player_name = input(f'|{opening_script[17]}')
    print("\n\n\n")
    opening_scene2 = False

# initialize variables for the main game loop
location = [-2, 4]  # presets location to Aosta
map_key = get_key(location)  # called when the players location needs displayed
start_time = time.time()  # starts the timer when the main loop runs

# the main game loop
while not has_won:

    # set boundary for game map
    if map_key not in map_locations:
        detained = True
        location = [-50, -50]
        map_key = get_key(location)

    # AOSTA: player start
    if map_key == "Aosta":
        player_update()
        # this message update changes the aosta dialogue after the player leaves home for the first time
        location_messages['dialogue']['Aosta'][0] = "Beethoven: Ah, home sweet home... " \
                                                    "I should get going if I am going to get to my concert in time!"
        map_key = get_key(location)  # updates the map_key when location coords change
        detained = False

    # TURIN: has  manuscript
    if map_key == "Turin":
        # every time this appears, it checks to see if player collected this locations manu
        if not manuscripts[map_key]:
            player_update(item='manu')
        else:
            player_update()
        map_key = get_key(location)

    # GENOA
    if map_key == "Genoa":
        player_update()
        map_key = get_key(location)

    # MILAN: has  manuscript
    if map_key == "Milan":
        if not manuscripts[map_key]:
            player_update(item='manu')
        else:
            player_update()
        map_key = get_key(location)

    # BALOGNA: has  manuscript
    if map_key == "Balogna":
        if not manuscripts[map_key]:
            player_update(item='manu')
        else:
            player_update()
        map_key = get_key(location)

    # FLORENCE: has  manuscript
    if map_key == "Florence":
        if not manuscripts[map_key]:
            player_update(item='manu')
        else:
            player_update()
        map_key = get_key(location)

    # PERUGIA
    if map_key == "Perugia":
        #  checks to see if player has collected boat pass
        if not has_boat_pass:
            player_update(item='boat_pass')
        else:
            player_update()
        map_key = get_key(location)

    # ROME
    if map_key == "Rome":
        player_update()
        map_key = get_key(location)

    # NAPLES: has  manuscript
    if map_key == "Naples":
        if not manuscripts[map_key]:
            player_update(item='manu')
        else:
            player_update()
        map_key = get_key(location)

    # AIR BALLOON PARK
    if map_key == "Air Balloon Park":
        player_update()
        map_key = get_key(location)

    # L'AQUILLA
    if map_key == "L'Aquilla":
        player_update()
        map_key = get_key(location)

    # ACONA: has  manuscript
    if map_key == "Acona":
        if not manuscripts[map_key]:
            player_update(item='manu')
        else:
            player_update()
        map_key = get_key(location)

    # VENICE
    if map_key == "Venice":
        player_update()
        map_key = get_key(location)

    # CAMPO BOSSO
    if map_key == "Campo Bosso":
        player_update()
        map_key = get_key(location)

    # POTENZA: has  manuscript
    if map_key == "Potenza":
        if not manuscripts[map_key]:
            player_update(item='manu')
        else:
            player_update()
        map_key = get_key(location)

    # BARI
    if map_key == "Bari":
        player_update()
        map_key = get_key(location)

    # CAGLIARI
    if map_key == "Cagliari":
        player_update()
        map_key = get_key(location)

    # PALERMO: has  manuscript
    if map_key == "Palermo":
        if not manuscripts[map_key]:
            player_update(item='manu')
        else:
            player_update()
        map_key = get_key(location)

    # CATANZARO
    if map_key == "Catanzaro":
        player_update()
        map_key = get_key(location)

    # TRIESTE
    if map_key == "Trieste":
        player_update()
        map_key = get_key(location)

    # TRENTO: has  manuscript
    if map_key == "Trento":
        if not manuscripts[map_key]:
            player_update(item='manu')
        else:
            player_update()
        map_key = get_key(location)

    # VIENNA
    if map_key == "Vienna":
        # checks is player has won or lost by comparing collects manus to total manus
        if manu_count == manu_total:
            won()
            print(f"|{timestamp()}  Can you do better? Play again soon!")
            input("|Press enter to exit.")
            break
        else:
            lost()
            print("|Thank you for playing! Try again soon.")
            break

    # DETENTION CENTER
    if map_key == "Detention Center":
        detained = True
        player_update()
        map_key = "Aosta"

    # EXIT game code
    if map_key == 'exit':
        print('Thank you for playing!')
        break
