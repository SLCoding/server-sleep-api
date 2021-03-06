from abc import ABC, abstractmethod
from enum import Enum


class AbstractCheckPlugin(ABC):

    """Initialize your Plugin Class"""
    @abstractmethod
    def __init__(self):
        pass

    """Check if the device should go to Sleep"""
    @abstractmethod
    def check(self):
        pass

    """Perform tasks that should be done before the device is set to sleep"""
    @abstractmethod
    def pre_sleep(self):
        pass

    """Perform tasks that should be done after wake up"""
    @abstractmethod
    def post_sleep(self):
        pass

    """Return a list of Configurable values for the Plugin"""
    @abstractmethod
    def configurables(self):
        pass


class CheckReturn(Enum):
    SLEEP_READY = 1
    DONT_SLEEP = 2
    FORCE_SLEEP = 3
    UNKNOWN = 9


class Configurable(object):

    def ___init___(self, identifier, displayname, examplevalue, description):
        self.identifier = identifier
        self.displayname = displayname
        self.examplevalue = examplevalue
        self.description = description
