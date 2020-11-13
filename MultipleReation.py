import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, msg):
        super(LoggableList, self).log(msg)

log = LoggableList()
log.append('Привет Паша как дела?')