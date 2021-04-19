from typing import Iterable, Union

import matplotlib
import matplotlib.pyplot as plt
from seaborn import reset_orig

import mplscience._styledata
from mplscience._styledata import __all__ as _available_styles


def available_styles() -> str:
    print(_available_styles)


def set_style(
    name: Union[str, Iterable[str]] = ("default", "despine"),
    reset_current: bool = False,
) -> None:
    """Set the style.

    Parameters
    ----------
    name
        Available style name
    reset_current
        Reset any custom styling before applying style
    """

    rcparams_update = {}
    names = [name] if isinstance(name, str) else name

    if reset_current:
        reset_orig()

    # compose multiple styles
    for n in names:
        if n not in _available_styles:
            raise ValueError("Style name not understood")
        rcparams_update.update(getattr(mplscience._styledata, n))

    plt.rcParams.update(rcparams_update)


def style_context(
    name: Union[str, Iterable[str]] = ("default", "despine"),
    reset_current: bool = False,
):
    """Creates a style context.

    Parameters
    ----------
    name
        Available style name
    reset_current
        Reset any custom styling before applying context

    Returns
    -------
    A context with selected style
    """

    rcparams = {}
    names = [name] if isinstance(name, str) else name

    if reset_current:
        reset_orig()

    # compose multiple styles
    for n in names:
        rcparams.update(getattr(mplscience._styledata, n))

    return matplotlib.rc_context(rcparams)
