
import traceback

class Logger():
    @staticmethod
    def log_exception(msg=''):
        print(traceback.format_exc())
