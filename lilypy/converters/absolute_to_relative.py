import ly.document
import ly.music
import ly.music.items

def collect_notes(node, notes):
    for child in node:
        if isinstance(child, ly.music.items.Note):
            notes.append(child)

        # recurse into children that can contain music
        if hasattr(child, "__iter__"):
            collect_notes(child, notes)


def convert_absolute_to_relative(path: str):
    """
    Parse LilyPond file and group notes per Staff.
    (Conversion logic not yet implemented.)
    """

    with open(path, "r") as f:
        content = f.read()

    doc = ly.document.Document(content)
    music = ly.music.document(doc)

    staff_notes = []
    current_staff = None

    # for node in music.iter_music():
        # if isinstance(node, ly.music.items.Context):
            # if node.context() == "Staff":
                # print("Found a Staff context")

    # breakpoint()
    for node in music.iter_music():

        # Detect entering a Staff context
        if isinstance(node, ly.music.items.Context) and node.context() == "Staff":
            current_staff = []
            staff_notes.append(current_staff)
            continue

        # Collect notes under current staff
        if isinstance(node, ly.music.items.Note) and current_staff is not None:
            current_staff.append(node)

    # Print results
    for i, notes in enumerate(staff_notes, start=1):
        print(f"Staff {i}: Found {len(notes)} notes.")

    # for i, notes in enumerate(staff_notes, start=1):
        # print(f"\nStaff {i}:")
        # for n in notes:
            # p = n.pitch
            # print("Pitch object:", p)
            # print("Dir:", dir(p))
            # break  # only inspect first note to avoid clutter

    for i, notes in enumerate(staff_notes, start=1):
        print(f"\nStaff {i}:")

        if not notes:
            continue

        anchor = notes[0].pitch.copy()

        print("Anchor:", anchor)

        for n in notes[1:]:
            print("Before:", n.pitch)
            n.pitch.makeRelative(anchor)
            print("After: ", n.pitch)
            anchor = n.pitch.copy()

    # for i, notes in enumerate(staff_notes, start=1):
        # print(f"\nStaff {i}:")
        # for n in notes:
            # p = n.pitch
            # print(
                # "  step:", p.step,
                # "alter:", p.alter,
                # "octave:", p.octave
            # )

