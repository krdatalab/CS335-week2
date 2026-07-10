# undo_stack.py  Program Requirements
Create the file challenge1.md in your GitHub repo.
Create an UndoStack class.
Store user actions in a stack.
Add new actions with a method named do_action.
Undo the most recent action with a method named undo_action.
If the user tries to undo when there are no actions, return a helpful message.
Demonstrate that the most recent action is always undone first.
Do not use decorators or advanced Python features.

```python

class UndoStack:
    def __init__(self):
        # TODO: Create an empty list to store actions
        pass

    def do_action(self, action):
        """
        Add a new action to the undo history.
        Example action: "typed hello"
        """
        # TODO: Add the action to the stack
        pass

    def undo_action(self):
        """
        Remove and return the most recent action.
        If there are no actions, return "Nothing to undo."
        """
        # TODO: Check whether the stack is empty

        # TODO: Remove and return the most recent action
        pass

    def show_history(self):
        """
        Print all actions currently stored in the undo history.
        """
        # TODO: Print the current action history
        pass


# Demo code
history = UndoStack()

history.do_action("typed hello")
history.do_action("made text bold")
history.do_action("changed font size")

history.show_history()

print(history.undo_action())
print(history.undo_action())

history.show_history()

```
