"""Example for a custom text-level annotator."""

from sparv.api import Annotation, Output, annotator

@annotator("Annotate each text with the number of nouns it contains")
def tnouns(
    text_annot: Annotation = Annotation("<text>"),
    nnouns_per_sent_annot: Annotation = Annotation("<sentence>:sbx_examples.snouns"),
    out: Output = Output("<text>:sbx_examples.tnouns"),
):
    """Count nouns at the text level, using sentence-level counts"""
    texts,_ = text_annot.get_children(nnouns_per_sent_annot)
    counts = list(nnouns_per_sent_annot.read())
    all_nnouns = []
    for text in texts:
        text_nnouns = 0
        for i in text:
            text_nnouns += int(counts[i])
        all_nnouns.append(str(text_nnouns))
    out.write(all_nnouns)
        