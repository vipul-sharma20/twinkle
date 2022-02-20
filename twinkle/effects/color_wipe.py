import time

from twinkle.effects.base import EffectBase, EffectRegistry
import twinkle.effects.util as util


@EffectRegistry.register(name="color-wipe")
class ColorWipe(EffectBase):
    """
    Wipe color across display a pixel at a time.
    """

    def __init__(self, *args, **kwargs):
        self.color = kwargs.get("<effect>", [None, util.Color(255, 0, 0)])[1]
        super().__init__(*args, **kwargs)

    def render(self, wait_ms=50):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, self.color)
            self.strip.show()
            time.sleep(wait_ms / 1000.0)
