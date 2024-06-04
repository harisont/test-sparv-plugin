"""Example for a custom sentence-level annotator."""

from sparv.api import Annotation, Output, annotator

@annotator("Annotate each sentence with the number of nouns it contains")
def snouns(
    pos_annot: Annotation = Annotation("<token:pos>"),
    sent_annot: Annotation = Annotation("<sentence>"),
    out: Output = Output("<sentence>:sbx_examples.snouns"),
):
    """Count nouns"""
    sents,_ = sent_annot.get_children(pos_annot)
    pos = list(pos_annot.read())
    all_nnouns = []
    for sent in sents:
        sent_nnouns = 0
        for i in sent:
            if pos[i] == "NN":
                sent_nnouns += 1
        # str conversion not needed in newer sparv versions
        all_nnouns.append(str(sent_nnouns))
    out.write(all_nnouns)
            