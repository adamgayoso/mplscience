# mplscience

Matplotlib style for scientific publications. This style keeps things pretty simple and aims to make moderate improvements to the base matplotlib style. It also sets things like the PDF font type to make it easier to interact with figures in Adobe Illustrator.


## Usage

```python
import mplscience
mplscience.available_styles()
mplscience.set_style()
```

If you're using Seaborn, you may want to run `sns.reset_orig()` first to clear Seaborn-specific styling.

The style can also be using in a context like this:

```python
import mplscience
with mplscience.style_context():
    plt.plot(x, y)
```

