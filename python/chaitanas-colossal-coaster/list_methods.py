"""Functions to manage and organize queues at Chaitana's roller coaster."""

from typing import List, Union


def is_valid_queue(queue: List[str]) -> bool:
    """Check if the queue is a valid list of names."""
    return isinstance(queue, list) and all(
        isinstance(name, str) and len(name) > 0 for name in queue
    )


def is_valid_ticket_type(ticket_type: int) -> bool:
    """Check if the ticket type is valid."""
    return ticket_type in (0, 1)


def is_valid_person_name(person_name: str) -> bool:
    """Check if the person name is valid."""
    return isinstance(person_name, str) and len(person_name) > 0


def add_me_to_the_queue(
    express_queue: List[str],
    normal_queue: List[str],
    ticket_type: int,
    person_name: str,
) -> List[str]:
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    if (
        not is_valid_ticket_type(ticket_type)
        or not is_valid_person_name(person_name)
        or not is_valid_queue(express_queue)
        or not is_valid_queue(normal_queue)
    ):
        raise ValueError(
            """
            ticket_type must be 1 or 0 
            person_name must be string 
            express_queue must be a list of strings
            normal_queue must be a list of strings
            """
        )

    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue: List[str], friend_name: str) -> Union[int, None]:
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """

    if not is_valid_person_name(friend_name) or not is_valid_queue(queue):
        raise ValueError(
            """
            friend_name must be string 
            queue must be a list of strings
            """
        )
    if friend_name not in queue:
        return None
    return queue.index(friend_name)


def add_me_with_my_friends(queue: List[str], index: int, person_name: str) -> List[str]:
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """

    if (
        not is_valid_person_name(person_name)
        or not is_valid_queue(queue)
        or not isinstance(index, int)
    ):
        raise ValueError(
            """
            person_name must be string 
            queue must be a list of strings
            index must be a valid quque index
            """
        )

    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: List[str], person_name: str) -> List[str]:
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """

    if (
        not is_valid_person_name(person_name)
        or not is_valid_queue(queue)
        or person_name not in queue
    ):
        raise ValueError(
            """
            person_name must be string 
            queue must be a list of strings
            person_name must be in the queue
            """
        )

    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: List[str], person_name: str) -> int:
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """

    if not is_valid_person_name(person_name) or not is_valid_queue(queue):
        raise ValueError(
            """
            person_name must be string 
            queue must be a list of strings
            """
        )

    return queue.count(person_name)


def remove_the_last_person(queue: List[str]) -> str:
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """

    if not is_valid_queue(queue) or len(queue) == 0:
        raise ValueError("queue must be a list of at least one string")

    return queue.pop()


def sorted_names(queue: List[str]) -> List[str]:
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

    if not is_valid_queue(queue):
        raise ValueError("queue must be a list of strings")

    return sorted(queue)
