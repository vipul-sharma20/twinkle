"""
twinkle: ws2812x effects library

Usage:
    twinkle render <effect>
"""

from docopt import docopt

from twinkle import __version__
from twinkle.effects.base import EffectRegistry


def main():
    args = docopt(__doc__, version=__version__)

    if args["render"]:
        try:
            effect_name = args["<effect>"][0]
        except KeyError:
            print("No effect specified")

        effect = EffectRegistry.create_executor(effect_name, **args)
        effect.render()
