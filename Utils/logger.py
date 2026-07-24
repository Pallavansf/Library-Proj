from datetime import datetime

class Logger:

    def __init__(self):
        pass

    def info(self, message, trace_id):
        self._log("INFO", message, trace_id)

    def warning(self, message, trace_id):
        self._log("WARNING", message, trace_id)

    def error(self, message, trace_id):
        self._log("ERROR", message, trace_id)

    def _log(self, level, message, trace_id):

        current_time = datetime.now()

        log_entry = (
            f"[{current_time}] "
            f"[{level}] "
            f"[Trace:{trace_id}] "
            f"{message}"
        )

        print(log_entry)