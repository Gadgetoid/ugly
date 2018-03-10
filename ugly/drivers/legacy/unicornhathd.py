# * Copyright 2018 Alistair Buxton <a.j.buxton@gmail.com>
# *
# * License: This program is free software; you can redistribute it and/or
# * modify it under the terms of the GNU General Public License as published
# * by the Free Software Foundation; either version 3 of the License, or (at
# * your option) any later version. This program is distributed in the hope
# * that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# * GNU General Public License for more details.

from ugly.buffer import Drawable
from ugly.drivers.base import Driver

import unicornhathd


class UnicornHatHD(Driver, Drawable):
    """
    Legacy driver. Passes through calls to some other driver.
    Does not need its own framebuffer as the legacy driver has one.
    """
    # TODO: may need multiple versions of this
    # as the legacy drivers are all slightly different.

    def __init__(self):
        super().__init__(unicornhathd._buf, 8, name='UnicornHatHD')

    def __enter__(self):
        return super().__enter__()

    def show(self):
        unicornhathd.show()
        super().show()

    def __exit__(self, exc_type, exc_val, exc_tb):
        unicornhathd.off()
        super().__exit__(exc_type, exc_val, exc_tb)