import time

from twinkle.effects.base import EffectBase, EffectRegistry
import twinkle.effects.util as util


@EffectRegistry.register(name="rainbow-cycle")
class RainbowCycle(EffectBase):
    """
    Draw rainbow that uniformly distributes itself across all pixels.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, wait_ms=20, iterations=5):
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, util.wheel(
                    (int(i * 256 / self.strip.numPixels()) + j) & 255))
            self.strip.show()
            time.sleep(wait_ms / 1000.0)
