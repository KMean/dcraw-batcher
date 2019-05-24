import Queue
from PySide2 import QtCore, QtGui, QtWidgets


class TaskManager(QtCore.QObject):
    messageChanged = QtCore.Signal(str)
    numbersTaskRunningChanged = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(TaskManager, self).__init__(parent)
        self._max_task = 1
        self._queue = Queue.Queue()
        self._numbers_task_running = 0
        self._running = False

    def setMaxTask(self, max_task):
        self._max_task = max_task
        if self._running:
            self.call_task()

    def maxTask(self):
        return self._max_task

    def appendTask(self, task):
        self._queue.put(task)
        self.call_task()

    def start(self):
        self._running = True
        self.call_task()

    def stop(self):
        self._running = False

    def call_task(self):
        if self._numbers_task_running < self.maxTask() and not self._queue.empty() and self._running:
            cmd = self._queue.get()
            process = QtCore.QProcess(self)
            process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
            process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
            process.finished.connect(self.on_finished)
            process.started.connect(self.on_started)
            process.errorOccurred.connect(self.on_errorOccurred)
            process.start(cmd)


    def on_readyReadStandardOutput(self):
        codec = QtCore.QTextCodec.codecForLocale()
        decoder_stdout = codec.makeDecoder()
        process = self.sender()
        text = decoder_stdout.toUnicode(process.readAllStandardOutput())
        self.messageChanged.emit(text)

    def on_errorOccurred(self, error):
        process = self.sender()
        print("error: ", error, "-", " ".join([process.program()] + process.arguments()))
        self.call_task()

    def on_finished(self):
        process = self.sender()
        self._numbers_task_running -= 1
        self.numbersTaskRunningChanged.emit(self._numbers_task_running)
        self.call_task()
        self.messageChanged.emit('Job Done!')

    def on_started(self):
        process = self.sender()
        print("started: ", " ".join([process.program()] + process.arguments()))
        self._numbers_task_running += 1
        self.numbersTaskRunningChanged.emit(self._numbers_task_running)
        self.call_task()



