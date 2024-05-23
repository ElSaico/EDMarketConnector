"""
theme.py - Theme support.

Copyright (c) EDCD, All Rights Reserved
Licensed under the GNU General Public License.
See LICENSE file.

Because of various ttk limitations this app is an unholy mix of Tk and ttk widgets.
So can't use ttk's theme support. So have to change colors manually.
"""
from __future__ import annotations

import tkinter as tk
from typing import Callable
from EDMCLogging import get_main_logger

logger = get_main_logger()


class _Theme:

    # Enum ?  Remember these are, probably, based on 'value' of a tk
    # RadioButton set.  Looking in prefs.py, they *appear* to be hard-coded
    # there as well.
    THEME_DEFAULT = 0
    THEME_DARK = 1
    THEME_TRANSPARENT = 2

    def register(self, widget: tk.Widget | tk.BitmapImage) -> None:  # noqa: CCR001, C901
        ...

    def button_bind(
        self, widget: tk.Widget, command: Callable, image: tk.BitmapImage | None = None
    ) -> None:
        widget.bind('<Button-1>', command)
        # TODO either check what of _enter and _leave is necessary, or replace
        #  this with a direct call to widget.bind if none of it is

    def update(self, widget: tk.Widget) -> None:
        ...

    def apply(self, root: tk.Tk) -> None:  # noqa: CCR001, C901
        ...


# singleton
theme = _Theme()
