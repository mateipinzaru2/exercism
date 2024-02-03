"""Solution to Ellen's Alien Game exercise."""

from typing import Union, List, Tuple


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(
        self, x_coordinate: Union[int, float], y_coordinate: Union[int, float]
    ):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """
        Decrement Alien health by one point.
        """
        self.health -= 1

    def is_alive(self) -> bool:
        """
        Return a boolean for if Alien is alive (if health is > 0)

        :return: bool
        """
        return self.health > 0

    def teleport(
        self, x_coordinate: Union[int, float], y_coordinate: Union[int, float]
    ):
        """
        Move Alien object to new coordinates

        :param x_coordinate: int or float coordinate
        :param y_coordinate: int or float coordinate
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other: "Alien"):
        """
        WIP
        """


def new_aliens_collection(
    alien_collection: List[Tuple[Union[int, float], Union[int, float]]]
) -> List["Alien"]:
    """
    Create a new collection of Alien objects from a list of tuples.

    :param alien_collection: List of tuples, where each tuple contains an Alien's coordinates.
    :return: List of Alien objects.
    """
    output = []
    for alien in alien_collection:
        output.append(Alien(alien[0], alien[1]))
    return output
