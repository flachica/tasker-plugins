#!/usr/bin/env python
try:
    import logging
    FORMAT = "%(asctime)-15s %(message)s"
    logging.basicConfig(level=logging.INFO, filename='log.log', format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S')

    import json
    from config_browser_integration import Configurator
    from messenger import Messenger
    import todotxtio
    import time

    messenger = Messenger()
    def searchTodo(todoToSearch):
        conf = Configurator()
        list_of_todos = todotxtio.from_file(conf.todo)
        for todo in list_of_todos:
            if todo.text == todoToSearch:
                return todo

    def getTagsAfterChangeState(beforeTags):
        started_at = float(beforeTags.get('started_at', 0))
        just_now = time.time()
        newTags = beforeTags
        if started_at:
            total_time = float(beforeTags.get('total_time', 0)) + time.time() - started_at
            newTags['started_at'] = '0'
            newTags['total_time'] = str(total_time)
            # self.hook.after_track_time(
            #     todo=self.todo,
            #     before_started_at=started_at,
            #     after_started_at=0,
            #     total_time=total_time,
            #     just_now=just_now
            # )
        else:
            newTags['started_at'] = str(just_now)
        return newTags

    def changeState(todoText):
        todo = searchTodo(todoText)
        todo.tags = getTagsAfterChangeState(todo.tags)
        saveTodo(todo)
        messenger.sendMessage({'type': 'stateChanged', 'todo': todoText})

    def saveTodo(todoToSearch):
        conf = Configurator()
        list_of_todos = todotxtio.from_file(conf.todo)
        for i in range(len(list_of_todos)):
            if list_of_todos[i].text == todoToSearch.text:
                list_of_todos[i].tags = todoToSearch.tags
        todotxtio.to_file(conf.todo, list_of_todos)

    def sendState(todoText):
        todo = searchTodo(todoText)
        if not todo:
            messenger.sendMessage({'type': 'stateGetted', 'todo': todoText, 'state': 'paused'})
        else:
            if todo.text == todoText and todo.tags['started_at'] and float(todo.tags['started_at']) > 0:
                messenger.sendMessage({'type': 'stateGetted', 'todo': todoText, 'state': 'started'})
            else:
                messenger.sendMessage({'type': 'stateGetted', 'todo': todoText, 'state': 'paused'})

    while True:
        receivedMessage = messenger.getMessage()
        if receivedMessage:
            dictMessage = json.loads(receivedMessage)
            logging.info('Received: ' + receivedMessage)
            todoText = dictMessage['payload']['todo']
            if dictMessage['type'] == 'getState':
                sendState(todoText)
            elif dictMessage['type'] == 'changeState':
                changeState(todoText)

except Exception as e:
    logging.exception("Uncaught exception")

