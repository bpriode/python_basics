# basic imports for the game
from sys import exit
from random import radint
from textwrap import dedent # lets us write our room descriptions using """ strings. It strips the white-space from the beginnings of lines in a string.

# base class for Scene
class Scene(object):

    def enter(self):
        print("This scene is not yet confirmed")
        print("Subclass it and implement enter().")
        exit(1)

# Already using the methods for Map.opening_scene and Map.next_scene
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene_map
        current_scene.enter()

# first scene is Death, which shows the simplist kind of scene you can write
class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[radient(0, len(self.quips)-1])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons Armory with a Gothan jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire it at the Gothon. His clown costume is flowing and moving around his body, which throws off your aim. Your laser hits his costume but misses him entirely. This completely ruins his brand new costume his mother bought him, which makes him fly into an insane rage and blast you repeatedly in the face until you are dead. Then he eats you.
                """))
        return 'death'

    elif action == "dodge!":
