from dataclasses import dataclass, field

@dataclass
class Instrument:
    name: str
    score_template: str
    preamble_template: str | None = None
    supported_options: set[str] = field( default_factory=set )
#    clef: str
#    transposition: str | None = None
#    supports_left_fingering: bool = False
#    supports_right_fingering: bool = False
