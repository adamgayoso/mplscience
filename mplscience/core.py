from typing import Iterable, Union

import matplotlib
import matplotlib.pyplot as plt

import mplscience._styledata
from mplscience._styledata import __all__ as _available_styles


def available_styles() -> str:
    print(_available_styles)


def set_style(name: Union[str, Iterable[str]] = ("default", "despine")) -> None:
    """Set the style.

    Parameters
    ----------
    name
        Available style name
    """

    rcparams_update = {}
    names = [name] if isinstance(name, str) else name

    # compose multiple styles
    for n in names:
        if n not in _available_styles:
            raise ValueError("Style name not understood")
        print(getattr(mplscience._styledata, n))
        rcparams_update.update(getattr(mplscience._styledata, n))

    plt.rcParams.update(rcparams_update)


def style_context(name: Union[str, Iterable[str]] = ("default", "despine")):
    """Creates a style context.

    Parameters
    ----------
    name
        Available style name

    Returns
    -------
    A context with selected style
    """

    rcparams = {}
    names = [name] if isinstance(name, str) else name

    # compose multiple styles
    for n in names:
        print(getattr(mplscience._styledata, n))
        rcparams.update(getattr(mplscience._styledata, n))

    return matplotlib.rc_context(rcparams)
