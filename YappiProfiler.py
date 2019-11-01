import yappi
from UM.Extension import Extension
from UM.Message import Message


class YappiProfiler(Extension):
    def __init__(self):
        super().__init__()
        self._is_profiling = False
        self.addMenuItem("Start", self.startProfiling)
        self.addMenuItem("Stop", self.stopProfiling)

        self._profiling_stopped_message = Message("Results were saved to curaProfile.out", title = "YappiProfiler")
        self._profiling_started_message = Message("Started profiling...", title = "YappiProfiler")

    def startProfiling(self):
        if not self._is_profiling:
            self._is_profiling = True
            self._profiling_stopped_message.hide()
            self._profiling_started_message.show()
            yappi.start()

    def stopProfiling(self):
        if self._is_profiling:
            yappi.stop()
            self._is_profiling = False

            func_stats = yappi.get_func_stats()
            func_stats.save("curaProfile.out", "CALLGRIND")
            yappi.clear_stats()
            self._profiling_started_message.hide()
            self._profiling_stopped_message.show()