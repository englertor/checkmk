#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.base.plugins.agent_based import prtconf
from cmk.base.plugins.agent_based.agent_based_api.v1 import Attributes, TableRow

INFO = [
    ["System Model", " IBM,8231-E2D"],
    ["Machine Serial Number", " 06AAB2T"],
    ["Processor Type", " PowerPC_POWER7"],
    ["Processor Implementation Mode", " POWER 7"],
    ["Processor Version", " PV_7_Compat"],
    ["Number Of Processors", " 8"],
    ["Processor Clock Speed", " 4284 MHz"],
    ["CPU Type", " 64-bit"],
    ["Kernel Type", " 64-bit"],
    ["LPAR Info", " 1 wiaix001"],
    ["Memory Size", " 257792 MB"],
    ["Good Memory Size", " 257792 MB"],
    ["Platform Firmware level", " AL770_076"],
    ["Firmware Version", " IBM,AL770_076"],
    ["Console Login", " enable"],
    ["Auto Restart", " true"],
    ["Full Core", " false"],
    ["Network Information"],
    ["Host Name", " example1"],
    ["IP Address", " 192.168.0.1"],
    ["Sub Netmask", " 255.255.255.128"],
    ["Gateway", " 192.168.0.2"],
    ["Name Server", " 192.168.0.3"],
    ["Domain Name", " example1.example.com"],
    ["Volume Groups Information"],
    ["Inactive VGs"],
    ["=============================================================================="],
    ["appvg"],
    ["=============================================================================="],
    ["Active VGs"],
    ["=============================================================================="],
    ["cow-daag0cvg", ""],
    ["PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION"],
    ["hdisk663          active            3218        0           00..00..00..00..00"],
    ["hdisk664          active            3218        0           00..00..00..00..00"],
    ["hdisk665          active            3218        0           00..00..00..00..00"],
    ["hdisk666          active            3218        0           00..00..00..00..00"],
    ["=============================================================================="],
    ["p2zgkbos4vg", ""],
    ["PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION"],
    ["hdisk5            active            643         0           00..00..00..00..00"],
    ["hdisk18           active            643         0           00..00..00..00..00"],
    ["=============================================================================="],
    ["INSTALLED RESOURCE LIST"],
]

EXPECTED = [
    Attributes(
        path=["hardware", "cpu"],
        inventory_attributes={
            "arch": "ppc64",
            "model": "PowerPC_POWER7",
            "implementation_mode": "POWER 7",
            "max_speed": 4284000000.0,
            "cpus": 8,
        },
    ),
    Attributes(
        path=["hardware", "system"],
        inventory_attributes={
            "serial": "06AAB2T",
            "product": "8231-E2D",
            "manufacturer": "IBM",
        },
    ),
    Attributes(
        path=["hardware", "memory"],
        inventory_attributes={
            "total_ram_usable": 270314504192,
        },
    ),
    Attributes(
        path=["software", "firmware"],
        inventory_attributes={
            "version": "AL770_076",
            "vendor": "IBM",
            "platform_level": "AL770_076",
        },
    ),
    Attributes(
        path=["networking"],
        inventory_attributes={
            "domain_name": "example1.example.com",
            "gateway": "192.168.0.2",
            "ip_address": "192.168.0.1",
            "name_server": "192.168.0.3",
            "sub_netmask": "255.255.255.128",
        },
    ),
    Attributes(
        path=["software", "os"],
        inventory_attributes={"arch": "ppc64"},
    ),
    TableRow(
        path=["hardware", "volumes", "physical_volumes"],
        key_columns={
            "volume_group_name": "cow-daag0cvg",
            "physical_volume_name": "hdisk664",
        },
        inventory_columns={
            "physical_volume_status": "active",
            "physical_volume_total_partitions": "3218",
            "physical_volume_free_partitions": "0",
        },
    ),
    TableRow(
        path=["hardware", "volumes", "physical_volumes"],
        key_columns={
            "volume_group_name": "cow-daag0cvg",
            "physical_volume_name": "hdisk665",
        },
        inventory_columns={
            "physical_volume_status": "active",
            "physical_volume_total_partitions": "3218",
            "physical_volume_free_partitions": "0",
        },
    ),
    TableRow(
        path=["hardware", "volumes", "physical_volumes"],
        key_columns={
            "volume_group_name": "cow-daag0cvg",
            "physical_volume_name": "hdisk666",
        },
        inventory_columns={
            "physical_volume_status": "active",
            "physical_volume_total_partitions": "3218",
            "physical_volume_free_partitions": "0",
        },
    ),
    TableRow(
        path=["hardware", "volumes", "physical_volumes"],
        key_columns={
            "volume_group_name": "p2zgkbos4vg",
            "physical_volume_name": "hdisk18",
        },
        inventory_columns={
            "physical_volume_status": "active",
            "physical_volume_total_partitions": "643",
            "physical_volume_free_partitions": "0",
        },
    ),
    TableRow(
        path=["hardware", "volumes", "physical_volumes"],
        key_columns={
            "volume_group_name": "appvg",
            "physical_volume_name": "",
        },
        inventory_columns={
            "physical_volume_status": "Inactive",
            "physical_volume_total_partitions": "",
            "physical_volume_free_partitions": "",
        },
    ),
]


def test_inv_prtconf() -> None:
    assert list(prtconf.inv_prtconf(prtconf.parse_prtconf(INFO))) == EXPECTED
