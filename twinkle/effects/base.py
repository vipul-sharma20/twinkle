import os
from abc import ABC, abstractmethod
from typing import Callable

import yaml
from rpi_ws281x import PixelStrip


class EffectBase(ABC):
    """
    Base class for LED effects.

    Methods:
        render(): LED effect function.
    """

    def __init__(self, **kwargs):
        """
        Initialize the effect.

        Args:
            kwargs: Keyword arguments.
        """
        # Create NeoPixel object with appropriate configuration.
        with open(os.getenv("LED_CONFIG_FILE"), "r") as config_file:
            config = yaml.load(open(config_file, "r"), Loader=yaml.FullLoader)
            self.strip = PixelStrip(**config)
            self.strip.begin()

    @abstractmethod
    def render(self, **kwargs):
        """
        LED effect function.
        """
        ...


class EffectRegistry:
    """
    Registry class for creating executors.

    Attributes:
        None

    Methods:
        register(name: str,
                 description: str): Class method to register
                                    EffectRegistry class to the internal
                                    registry.
        create_executor(name: str): registry command to create the executor.
    """

    # registry for available executors
    registry = {}

    @classmethod
    def register(cls, name: str, description: str) -> Callable:
        """
        Class method to register EffectRegistry class to the internal
        registry.

        Returns:
            Callable: The Effect class.
        """

        def inner_wrapper(wrapped_class: EffectBase) -> Callable:
            if name in cls.registry:
                print("Executor {name} already exists. Replacing it")
            cls.registry[name] = {"class": wrapped_class,
                                  "description": description,
                                  "verbose": wrapped_class.__doc__}
            return wrapped_class

        return inner_wrapper

    @classmethod
    def create_executor(cls, name: str, **kwargs) -> EffectBase:
        """
        Registry command to create the executor.  This method gets the
        appropriate Effect class from the registry and creates an
        instance of it, while passing in the parameters given in ``kwargs``.

        Returns:
            EffectBase: An instance of the executor that is created.
        """

        if name not in cls.registry:
            print(f"Executor {name} does not exist in the registry")
            return None

        exec_class = cls.registry[name].get("class")
        executor = exec_class(**kwargs)

        return executor

