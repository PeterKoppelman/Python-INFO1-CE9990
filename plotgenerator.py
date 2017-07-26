"""
plotgenerator.py
by the Brothers Heimberg: Jason & Justin

Generate a movie plot.
"""

import sys
import random

S = 0   #singular
P = 1   #plural

subjects = [
    [S, "A cop who doesn't play by the rules"],
    [S, "A single mom"],
    [P, "Three naughty nurses"],
    [S, "An adorable panda cub"],
    [S, "A ruthless Mafia kingpin"],
    [S, "An ancient and powerful wizard"],
    [S, "A fraternity of lovable slobs, misfits, and drunks"],
    [S, "Adolph Hitler"],
    [S, "From a land where honor and tradition reign, "
        "comes the legend of a Samurai who"],
    [S,"A bumbling nerd"],
    [S, "Bigfoot"],
    [S, "A crackhead"],
    [S, "A flamboyantly gay hairdresser"],
    [S, "A retarded boy"],
    [P, "America's founding fathers"],
    [S, "A hockey mask-wearing psychopath"],
    [S, "A gangsta rapper"],
    [S, "An unrefined but precocious orphan girl"],
    [S, "The ultimate crime-fighting indestructible cyborg"],
    [P, "The Sesame Street puppets"],
    [S, "A small-town girl with big-time dreams"],
    [P, "A group of orthodox rabbis"],
    [S, "A burned-out hippie"],
    [S, "A Catholic priest"],
    [S, "A hooker with a heard of gold"],
    [S, "A grumpy midget"],
    [P, "A group of cantankerous senior citizens"],
    [S, "Jesus"],
    [S, "A no-nonsense Army drill sergeant"],
    [S, "A macho NFL quarterback"]
]

predicates = [
    ["fights crime", "fight crime"],
    ["raises a baby", "raise a baby"],
    ["discovers the wonders of self pleasure", "discover the wonders of self pleasure"],
    ["befriends the creatures of the forest", "befriend the creatures of the forest"],
    ["are on the run from the Mob", "is on the run from the Mob"],
    ["quests for a dragon's treasure", "quest for a dragon's treasure"],
    ["indulges in beer bashes, toga parties, "
        "and an assortment of ill-advised high junks",
     "indulge in beer bashes, toga parties, "
        "and an assortment of ill-advised high junks"],
    ["invades Poland", "invade Poland"],
    ["takes on an army of evil Ninjas", "take on an army of evil Ninjas"],
    ["becomes immersed in hip-hop culture", "become immersed in hip-hop culture"],
    ["becomes a nanny for a conservative aristocratic family", "become a nanny for a conservative aristocratic family"],
    ["coaches a hapless Little League baseball team", "coach a hapless Little League baseball team"],
    ["hits the Karaoke circuit", "hit the Karaoke circuit"],
    ["grows 50 times in size and goes on a destructive rampage", "grow 50 times in size and go on a destructive rampage"],
    ["travels through time", "travel through time"],
    ["hacks up coeds with a rusty machete", "hack up a coed with a rusty machete"],
    ["becomes a pimp", "become pimps"],
    ["challenges the social mores of upper class society", "challenge the social mores of upper class society"],
    ["commands a fleet of starships against a horde of insectoid aliens", "command a fleet of starships against a horde of insectoid aliens"],
    ["help children learn to read", "help a child learn to read"],
    ["gets transformed into gorgeous sexpots", "get transformed into a gorgeous sexpot"],
    ["competes in gritty inner-city street basketball tournaments", "compete in a gritty inner-city street basketball tournament"],
    ["goes on an LSD-induced psychedelic adventure", "go on an LSD-induced psychedelic adventure"],
    ["discovers a hidden talent for dance", "discover a hidden talent for dance"],
    ["struggles to get off heroin", "struggle to get off heroin"],
    ["tries to lose their virginity", "try to lose his/her virginity"],
    ["battles problem flatulence", "battle problem flatulence"],
    ["rises from the grave", "rise from the grave"],
    ["rescues a group of American P.O.W.'s", "rescue a group of American P.O.W.'s"],
    ["comes out of the closet", "come out of the closet"]
]

modifiers = [
    "with a mischievous orangutan",
    "while juggling work, parenthood, and finding personal fulfillment",
    "in two hours of the raunchiest hardcore porno action ever seen",
    "in this heartwarming animated adventure",
    "in the heart of the Amish country",
    "with a cunning elf, an obese ogre, and a belligerent dwarf",
    "despite being admonished by a crusty old dean",
    "in this documentary narrated by James Earl Jones",
    "in an action-packed epic filled with elaborate, "
        "acrobatic Kung-Fu fight sequences",
    "to win the heart of the high school dreamboat",
    "in the feel-good comedy of the year",
    "in order to pay off a gambling debt",
    "in a beat-up Buick",
    "in the middle of Downtown Tokyo (in Japanese with English subtitles)",
    "with a wise-cracking robot",
    "in a blood-filled teen slasher, deep in the Compton ghetto",   #Los Angeles
    "in 1954 Baltimore (based on the Pulitzer Prize winning novel)",
    "shown in spectacular 3-D Imax",
    "in this powerful after school special",
    "set to an all-star '80's soundtrack "
        "featuring Air Supply, Journey, and Survivor",
    "to save the local synagogue",
    "with a magical talking bong, "
    "in this stoner cult classic",
    "in a rousing adaptation of the Broadway musical",
    "with the help of former tennis great Ivan Lendl (based on a true story)",
    "with the help of the ghost of Elvis",
    "set against the backdrop of a Florida retirement community",
    "in the inspiring story loosely adapted from the Bible",
    "in a Vietnamese prison camp",
    "and in the process learn(s) the true meaning of Christmas"
]

# check to see if the OS is mac or linux or windows
# I found that ctrl-d worked to end the script on a windows machine so I changed the
# if elif to and if else.  PK 7/25/2017
if sys.platform.startswith("darwin") or sys.platform.startswith("linux") or sys.platform.startswith("win32"):
    print("Keep pressing return/enter, or control-d to exit.")
else:
    print("Unknown platform", sys.platform)
    sys.exit(1)

while True:
    try:
        input()
    except EOFError:
        sys.exit(1)

    s = random.choice(subjects)   #s is a list.  s[0] is a number, s[1] is a string.
    p = random.choice(predicates) #p is a list of two strings.
    print(s[1])
    n = s[0]                      #n is either 0 for singular or 1 for plural.
    print(p[n])                   #Print either p[0] or p[1].
    print(random.choice(modifiers), ".", sep = "")

    
