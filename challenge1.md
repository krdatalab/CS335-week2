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
        actions_list = []
        pass
        


    def do_action(self, action):
        """
        Add a new action to the undo history.
        Example action: "typed hello"
        """
        # TODO: Add the action to the stack
        actions_list.append(action)

        pass

    def undo_action(self):
        """
        Remove and return the most recent action.
        If there are no actions, return "Nothing to undo."
        """
        # TODO: Check whether the stack is empty. When a user clicks undo on an empty list, nothing is returned. 
        if len(actions_list) is == o:
            return None

        # TODO: Remove and return the most recent action
         action = self.actions_list.remove()
            return action

        pass

    def show_history(self):
        """
        Print all actions currently stored in the undo history.
        """
        # TODO: Print the current action history
        for action in actions_list:
            print (action)
        pass





# create an undo stach object which is dtored in history
history = UndoStack()

# this is storing the past three actions
history.do_action("typed hello")
history.do_action("made text bold")
history.do_action("changed font size")

history.show_history()

print(history.undo_action())
print(history.undo_action())

history.show_history()


# a queue removes the oldest item first and a stack removes the last actin first therefore, a stach is used here. 

```
