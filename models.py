from datetime import datetime

log_file = 'log.txt'

def foo_logger(file):
    def foo_logger_(function):
        def new_function(*args, **kwargs):
            result = function(*args, **kwargs)
            log = f'{datetime.now()} - {function.__name__} _ {args}_{kwargs} - {result}\n'
            with open(file, 'a', encoding='utf-8') as f:
                f.write(log)
            return result
        return new_function
    return foo_logger_