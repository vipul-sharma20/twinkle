import time

from twinkle.effects.base import EffectBase, EffectRegistry
import twinkle.effects.util as util


@EffectRegistry.register(name="rainbow")
class Rainbow(EffectBase):
    """
    Draw rainbow that fades across all pixels at once.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, wait_ms=20, iterations=1):
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, util.wheel((i + j) & 255))
            self.strip.show()
            time.sleep(wait_ms / 1000.0)
