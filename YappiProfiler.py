import yappi
from UM.Extension import Extension
from UM.Message import Message


class YappiProfiler(Extension):
    def __init__(self):
        super().__init__()
        self._is_profiling = False
        self.addMenuItem("Start", self.startProfiling)
        self.addMenuItem("Stop", self.stopProfiling)

        self._profiling_stopped_message = Message("Results were saved to curaProfile.out")


    def startProfiling(self):
        if not self._is_profiling:
            self._is_profiling = True
            yappi.start()

    def stopProfiling(self):
        if self._is_profiling:
            yappi.stop()
            self._is_profiling = False

            func_stats = yappi.get_func_stats()
            func_stats.save("curaProfile.out", "CALLGRIND")
            self._profiling_stopped_message.show()
            yappi.stop()
            yappi.clear_stats()