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
        This event is fired after user click on one task or close the app with a task started
        Take on account that this event is fired per task and one click may fire this event two times:
        one to finalize previous, other for initialize this

        In the original code only track total time per task. To sum all time inverted in a task
        you need to know when started it and with the current time you can sum time to total time
        With this hook you can know when was started and the total time in one step

        Arguments:
        * todo (todo object. See todotxt.io) Object that hold information
        * before_started_at: Unix time. Last started time
        * after_started_at (float): Unix time. If greater than 0 todo has initialized
                                               else the todo has being finalized
        * total_time: Acumulated time in todo
        * just_now: Unix time. Only one time instance accross call's
        """
        print('todo: {}, before_started_at: {}, after_started_at: {}, total_time: {}, just_now: {}'.\
              format(todo.text, before_started_at, after_started_at, total_time, just_now))