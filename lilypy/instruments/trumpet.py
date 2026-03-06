from .base import Instrument

TRUMPET = Instrument(
    name="trumpet",
    score_template="instruments/trumpet.ly.j2",
    supported_options={"concert"},
#    clef="treble",
#    transposition="bes",  # Bb trumpet
)

