from .base import Instrument

GUITAR = Instrument(
    name="guitar",
    score_template="instruments/guitar.ly.j2",
    preamble_template="instruments/guitar_preamble.ly.j2",
)

