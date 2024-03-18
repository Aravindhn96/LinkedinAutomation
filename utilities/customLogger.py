import inspect
import logging

def customLogger(loglevel = logging.DEBUG):

#getting the funtion or class name so that we know where it is running
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)  #this will record every thing we can also change the log level

    fileHandler = logging.FileHandler("filelogs.log", mode="a")
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s -%(name)s-%(levelname)s:%(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger


    