from lilypy.instruments.registry import INSTRUMENTS
from lilypy.templates.render import render_template
from lilypy.converters.absolute_to_relative import convert_absolute_to_relative

def new_file(args):
    instrument = INSTRUMENTS.get(args.instrument)

    if not instrument:
        raise ValueError(f"Unknown instrument: {args.instrument}")

    content = render_template(
        instrument=instrument,
        instrument_header=instrument.name,
        title=args.title,
        subtitle=args.subtitle,
        composer=args.composer,
        arranger=args.arranger,
        opus=args.opus,
        key=args.key,
        mode=args.mode,
        concert=args.concert,
        lyrics=args.lyrics,
    )

    with open(args.output, "w") as f:
        f.write(content)

    print(f"Created {args.output}")

def convert_file(args):
    if args.mode == "relative":
        convert_absolute_to_relative(args.file)

