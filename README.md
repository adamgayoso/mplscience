# mplscience

Matplotlib style for scientific publications.


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

