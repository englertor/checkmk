#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from collections.abc import Mapping


def discover(info):
    for item, *_rest in info:
        yield item, {}


_STATE_MAP: Mapping[str, tuple[int, str]] = {
    "1": (0, "UP"),
    "2": (2, "DOWN"),
    "3": (1, "DEGRADED"),
}


def dev_state_map(orig_dev_state: str) -> tuple[int, str]:
    return _STATE_MAP.get(orig_dev_state, (3, f"unknown[{orig_dev_state}]"))
