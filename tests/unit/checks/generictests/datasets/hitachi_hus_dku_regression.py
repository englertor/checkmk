#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# fmt: off
# mypy: disable-error-code=var-annotated

checkname = "hitachi_hus_dku"

info = [["210221", "1", "1", "1", "1"]]

discovery = {"": [("210221", None)]}

checks = {
    "": [
        (
            "210221",
            {},
            [
                (
                    0,
                    "OK: Power Supply: no error, Fan: no error, Environment: no error, Drive: no error",
                    [],
                )
            ],
        )
    ]
}
