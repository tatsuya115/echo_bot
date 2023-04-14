#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "2910a492-fb66-4b63-b0c7-eedcd6ae39b2")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "gTx8Q~hRRwwgk4QgPlMuzMysswCW1nfeNOC.XbxO")
