from importlib import resources
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

def _get_template_environment():
    """
    Create a Jinja2 environment pointing to the installed
    lilypy/templates directory.
    """

    templates_path = resources.files("lilypy") / "templates"

    return Environment(
        loader=FileSystemLoader(str(templates_path)),
        autoescape=select_autoescape(enabled_extensions=()),
        trim_blocks=True,
        lstrip_blocks=True,
    )

def render_template(
    *,
    instrument,
    title: str,
    composer: str,
    arranger: str,
    key: str,
    mode: str,
    **options,
) -> str:
    """
    Render a LilyPond score using the base score template.
    """

    env = _get_template_environment()
    template = env.get_template("base.ly.j2")

    return template.render(
        title=title,
        instrument=instrument,
        composer=composer,
        arranger=arranger,
        key=key,
        mode=mode,
        score_template=instrument.score_template,
        preamble_template=instrument.preamble_template,
        **options,
    )

