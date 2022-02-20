import time

from twinkle.effects.base import EffectBase, EffectRegistry
import twinkle.effects.util as util


@EffectRegistry.register(name="theatre-chase-rainbow")
class TheatreChaseRainbow(EffectBase):
    """
    Rainbow movie theater light style chaser animation.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, wait_ms=50):
        for j in range(256):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, util.wheel((i + j) % 255))

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)


@EffectRegistry.register(name="theatre-chase")
class TheatreChase(EffectBase):
    """
    Movie theater light style chaser animation.
    """

    def __init__(self, *args, **kwargs):
        self.color = kwargs.get("<effect>", [None, util.Color(255, 0, 0)])[1]
        super().__init__(*args, **kwargs)

    def render(self, wait_ms=50, iterations=10):
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, self.color)

                self.strip.show()
                time.sleep(wait_ms / 1000.0)

                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)
