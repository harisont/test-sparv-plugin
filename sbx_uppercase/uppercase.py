"""Example for a custom annotator."""

from sparv.api import Annotation, Output, annotator


@annotator("Convert every word to uppercase")
def uppercase(
    word: Annotation = Annotation("<token:word>"),
    out: Output = Output("<token>:sbx_uppercase.upper"),
    # some_config_variable: str = Config("sbx_uppercase.some_setting")
):
    """Convert to uppercase."""
    out.write([val.upper() for val in word.read()])

@annotator("Convert every word to title case (first letter uppercase)")
def titlecase(
    word: Annotation = Annotation("<token:word>"),
    out: Output = Output("<token>:sbx_uppercase.title"),
):
    """Convert to title case."""
    out.write([val.title() for val in word.read()])