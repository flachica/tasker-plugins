import codecs
import json
import logging
import os
from pathlib import Path

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".config/tasker")
CONFIG_FILE = os.path.join(CONFIG_DIR, "tasker.conf")
FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    format=FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Configurator(object):
    def __init__(self):
        self.read()

    def read(self):
        try:
            f = codecs.open(CONFIG_FILE, "r", "utf-8")
        except IOError as e:
            print(e)
            f = codecs.open(CONFIG_FILE, "r", "utf-8")
        try:
            self.params = json.loads(f.read())
        except ValueError as e:
            print(e)
        f.close()

        try:
            self.todo_histoy = (
                Path(
                    os.path.expanduser(self.params["preferences"]["todo-file"])
                ).parent.as_posix()
                + os.sep
                + "todo.history.txt"
            )
            todo_histoy_path = Path(self.todo_histoy)
            if not todo_histoy_path.exists():
                todo_histoy_path.touch()

            self.todo = Path(
                os.path.expanduser(self.params["preferences"]["todo-file"])
            ).as_posix()
            todo_path = Path(self.todo)
            if not todo_path.exists():
                todo_path.touch()
        except KeyError as e:
            print(e)
