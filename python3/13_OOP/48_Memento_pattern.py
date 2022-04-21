#!/usr/bin/python
"""
Purpose: Memento Design Pattern example
    https://en.wikipedia.org/wiki/Memento_pattern
"""


class Memento(object):
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state


class Originator(object):
    _state = ""

    def set(self, state):
        print("Originator: Setting state to", state)
        self._state = state

    def save_to_memento(self):
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()
        print("Originator: State after restoring from Memento:", self._state)


saved_states = []
originator = Originator()
originator.set("State1")
originator.set("State2")
saved_states.append(originator.save_to_memento())

originator.set("State3")
saved_states.append(originator.save_to_memento())

originator.set("State4")

originator.restore_from_memento(saved_states[0])
