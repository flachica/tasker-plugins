import pluggy

# Decorator for hook. The function that was decorated with this
# will be called from de master source if it in Hookspecks availables
list_box_todospec = pluggy.HookimplMarker("list_box_todo")

# Custom featured needed
from src.hooks import ListBoxRowTodoSpec

class ListBoxRowTodoPlugin1(ListBoxRowTodoSpec):
    """A hook implementation namespace.
    """

    @list_box_todospec
    def after_track_time(self, todo, before_started_at, after_started_at, total_time, just_now):
        """
        todo (todo object. See todotxt.io) Object that hold information
        started_at (float): Unix time. When 0 the todo has being finalizted
        total_time: Acumulated time in todo
        """
        print('todo: {}, before_started_at: {}, after_started_at: {}, total_time: {}, just_now: {}'.\
              format(todo.text, before_started_at, after_started_at, total_time, just_now))