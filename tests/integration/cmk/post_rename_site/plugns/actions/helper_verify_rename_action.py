#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.post_rename_site.main import load_plugins

load_plugins()
from cmk.post_rename_site.registry import rename_action_registry

print("test" in rename_action_registry)
