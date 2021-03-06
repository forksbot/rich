from typing import Dict

from .style import Style

DEFAULT_STYLES: Dict[str, Style] = {
    "none": Style(),
    "reset": Style(
        color="default",
        bgcolor="default",
        dim=False,
        bold=False,
        italic=False,
        underline=False,
        blink=False,
        blink2=False,
        reverse=False,
        conceal=False,
        strike=False,
    ),
    "dim": Style(dim=True),
    "bright": Style(dim=False),
    "bold": Style(bold=True),
    "strong": Style(bold=True),
    "code": Style(reverse=True, bold=True),
    "b": Style(bold=True),
    "italic": Style(italic=True),
    "emphasize": Style(italic=True),
    "i": Style(italic=True),
    "underline": Style(underline=True),
    "u": Style(underline=True),
    "blink": Style(blink=True),
    "blink2": Style(blink2=True),
    "reverse": Style(reverse=True),
    "strike": Style(strike=True),
    "s": Style(strike=True),
    "black": Style(color="black"),
    "red": Style(color="red"),
    "green": Style(color="green"),
    "yellow": Style(color="yellow"),
    "magenta": Style(color="magenta"),
    "cyan": Style(color="cyan"),
    "white": Style(color="white"),
    "log.time": Style(color="cyan", dim=True),
    "log.message": Style(),
    "log.path": Style(dim=True),
    "repr.str": Style(color="green", italic=False),
    "repr.brace": Style(bold=True),
    "repr.tag_start": Style(bold=True),
    "repr.tag_name": Style(color="bright_magenta"),
    "repr.tag_contents": Style(color="default", italic=True),
    "repr.tag_end": Style(bold=True),
    "repr.attrib_name": Style(color="yellow", italic=True),
    "repr.attrib_equal": Style(bold=True),
    "repr.attrib_value": Style(color="magenta", italic=False),
    "repr.number": Style(color="blue", bold=True, italic=False),
    "repr.bool_true": Style(color="bright_green", italic=True),
    "repr.bool_false": Style(color="bright_red", italic=True),
    "repr.none": Style(color="magenta", italic=True),
    "repr.url": Style(underline=True, color="default"),
    "rule.line": Style(color="green"),
    "rule.text": Style(),
    "table.header": Style(bold=True),
    "table.footer": Style(bold=True),
    "table.cell": Style(),
    "table.title": Style(italic=True),
    "table.caption": Style(italic=True, dim=True),
}

MARKDOWN_STYLES = {
    "markdown.paragraph": Style(),
    "markdown.text": Style(),
    "markdown.emph": Style(italic=True),
    "markdown.strong": Style(bold=True),
    "markdown.code": Style(bgcolor="black", color="bright_white"),
    "markdown.code_block": Style(dim=True, color="cyan", bgcolor="black"),
    "markdown.block_quote": Style(color="magenta"),
    "markdown.list": Style(color="cyan"),
    "markdown.item": Style(),
    "markdown.item.bullet": Style(color="yellow", bold=True),
    "markdown.item.number": Style(color="yellow", bold=True),
    "markdown.hr": Style(dim=True),
    "markdown.h1.border": Style(),
    "markdown.h1": Style(bold=True),
    "markdown.h2": Style(bold=True, underline=True),
    "markdown.h3": Style(bold=True),
    "markdown.h4": Style(bold=True, dim=True),
    "markdown.h5": Style(underline=True),
    "markdown.h6": Style(italic=True),
    "markdown.h7": Style(italic=True, dim=True),
    "markdown.link": Style(bold=True),
    "markdown.link_url": Style(underline=True),
}
DEFAULT_STYLES.update(MARKDOWN_STYLES)
