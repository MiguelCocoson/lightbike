# Player attributes
# _trail
# dead

# Player methods:
# is_dead()
# hide_sprite

from data.actor import Actor
from data.trail import Trail
from data.point import Point

class Player(Actor):
    """
    The Player class is used to create the players in the lightbike game
    
    Stereotype:
        Information Holder

    Methods:
        __init__(): generates the name and initializes the parent class
        get_name(): returns the name
        set_name(name): sets the name
        set_trail():sets the trail
        get_trail():gets trail
        dead_sprite(): hides sprite when dead and stops velocity
    """
    
    def __init__(self):
        """
        Class constructor, initializes private attributes for name and guess
        """
        super().__init__()
        self.__name = ""
        self._trail = Trail()
    
    def get_name(self):
        """
        Returns the player's name
        """
        return self.__name
    
    def set_name(self, name):
        """
        Sets the players name as a string

        Parameters:
        name(str): The name to be set to the private attribute
        """
        self.__name = str(name)

    def get_trail(self):
        """
        gets the Trail
        """
        return self._trail 
        
    def set_trail(self, trail):
        """
        Sets the variable to trail
        """
        self._trail = trail

    def dead_sprite(self):
        """
        hide and stop the player temporarily
        """
        self.get_sprite().scale = 0
        self.set_velocity(Point(0, 0))
