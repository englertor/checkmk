#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# fmt: off
# mypy: disable-error-code=var-annotated


checkname = "cmctc_state"


info = [["1", "3"]]


discovery = {"": [(None, {})]}


checks = {"": [(None, {}, [(2, "Status: failed, Units connected: 3", [])])]}
