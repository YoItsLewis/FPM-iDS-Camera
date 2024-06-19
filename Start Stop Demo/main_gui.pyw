# \file    main_gui.pyw
# \author  vapivendorname
# \date    2024-02-20
#
# \brief   This sample shows how to start and stop acquisition as well as
#          how to capture images using a software trigger
#
# \version 1.0
#
# Copyright (C) 2024, vapivendorname.
#
# The information in this document is subject to change without notice
# and should not be construed as a commitment by vapivendorname.
# vapivendorname does not assume any responsibility for any errors
# that may appear in this document.
#
# This document, or source code, is provided solely as an example of how to utilize
# vapivendorname software libraries in a sample application.
# vapivendorname does not assume any responsibility
# for the use or reliability of any portion of this document.
#
# General permission to copy or modify is hereby granted.

from qt_interface import Interface

from main import main

if __name__ == "__main__":
    main(Interface())
