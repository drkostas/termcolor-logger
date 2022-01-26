# pip install termcolor-logger
from termcolor_logger import ColorLogger

fancy_logger = ColorLogger(logger_name='FancyMain',
                           color='blue',
                           on_color='on_red',
                           attrs=['underline', 'reverse', 'bold'])

ColorLogger.setup_logger(log_path="hi.log", debug=True, clear_log=True)

fancy_logger.info("You can customize the logger like this")
fancy_logger.info("You can customize each log message differently",
                  color="green", on_color="on_white", attrs=[])
