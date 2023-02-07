import seaborn as sns

import mplscience


def test_mplscience():
    mplscience.available_styles()
    mplscience.set_style("default")

    with mplscience.style_context(reset_current=True):
        df = sns.load_dataset("anscombe")
        sns.scatterplot(x="x", y="y", hue="dataset", data=df)
