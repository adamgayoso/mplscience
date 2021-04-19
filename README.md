# mplscience
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/11ZA7lq-nFpNpFFWqXnlCphRR6_N9qXP3?usp=sharing]
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Matplotlib style for scientific publications. This style keeps things pretty simple and aims to make moderate improvements to the base matplotlib style. It also sets things like the PDF font type to make it easier to interact with figures in Adobe Illustrator.


## Usage

```python
import mplscience
mplscience.available_styles()
mplscience.set_style()
```

If you're using Seaborn, you may want to run `sns.reset_orig()` first to clear Seaborn-specific styling. You can also use the `reset_current` parameter of `mplscience` functions to reset any custom styling like this:

```python
mplscience.set_style(reset_current=True)
```


The style can also be using in a context like this:

```python
import mplscience
with mplscience.style_context():
    plt.plot(x, y)
```



