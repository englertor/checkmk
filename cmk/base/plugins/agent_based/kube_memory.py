#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
import json
from typing import Literal, Optional, Tuple, TypedDict, Union

from cmk.base.plugins.agent_based.utils.k8s import Memory
from cmk.base.plugins.agent_based.utils.kube import ExceptionalResource, Resources

from .agent_based_api.v1 import Metric, register, render, Result, Service, State
from .agent_based_api.v1.type_defs import CheckResult, DiscoveryResult, StringTable
from .utils.memory import check_element


def parse_memory_resources(string_table: StringTable) -> Resources:
    """
    >>> parse_memory_resources([['{"request": 23120704.0, "limit": 28120704.0}']])
    Resources(request=23120704.0, limit=28120704.0)
    >>> parse_memory_resources([['{"request": "unspecified", "limit": "unspecified"}']])
    Resources(request=<ExceptionalResource.unspecified: 'unspecified'>, limit=<ExceptionalResource.unspecified: 'unspecified'>)
    >>> parse_memory_resources([['{"request": 0.0, "limit": "zero"}']])
    Resources(request=0.0, limit=<ExceptionalResource.zero: 'zero'>)
    """
    return Resources(**json.loads(string_table[0][0]))


def parse_performance_memory(string_table: StringTable) -> Memory:
    """
    >>> parse_performance_memory([['{"memory_usage_bytes": 18120704.0}']])
    Memory(memory_usage_bytes=18120704.0)
    """
    return Memory(**json.loads(string_table[0][0]))


register.agent_section(
    name="kube_memory_resources_v1",
    parse_function=parse_memory_resources,
    parsed_section_name="kube_memory_resources",
)


register.agent_section(
    name="k8s_live_memory_v1",
    parse_function=parse_performance_memory,
    parsed_section_name="k8s_live_memory",
)


# TODO Add different logic, service should always be discovered, but instead be pending
# (not unknown)
def discovery_kube_memory(
    section_kube_memory_resources, section_k8s_live_memory
) -> DiscoveryResult:
    if section_k8s_live_memory is not None and section_kube_memory_resources is not None:
        yield Service()


Modes = Literal["perc_used", "abs_used"]
Param = Union[Literal["ignore"], Tuple[Modes, Tuple[float, float]]]


class Params(TypedDict):
    request: Param
    limit: Param


_DEFAULT_PARAMS = Params(
    request="ignore",
    limit=("perc_used", (80.0, 90.0)),
)


# TODO This should be moved to utils, and used jointly by kube_container_memory and kube_container_cpu
# TODO Add Perf-O-Meter
def check_kube_memory(
    params: Params,
    section_kube_memory_resources: Optional[Resources],
    section_k8s_live_memory: Optional[Memory],
) -> CheckResult:
    if section_k8s_live_memory is None or section_kube_memory_resources is None:
        return

    total_usage = section_k8s_live_memory.memory_usage_bytes
    yield Result(state=State.OK, summary=f"Usage: {render.bytes(total_usage)}")
    yield Metric("kube_memory_usage", total_usage)

    for requirement_name, requirement in section_kube_memory_resources:
        if requirement == 0:
            yield Result(
                state=State.OK,
                summary=f"{requirement_name.title()}: n/a",
                details=f"{requirement_name.title()}: set to zero for all containers",
            )
        elif isinstance(requirement, float):
            param = params[requirement_name]  # type: ignore
            result, metric = check_element(
                f"{requirement_name.title()} utilization",
                used=total_usage,
                total=requirement,
                levels=param if param != "ignore" else None,
                create_percent_metric=True,
            )

            assert isinstance(metric, Metric)

            yield result
            yield Metric(
                name=f"kube_memory_{requirement_name}_utilization",
                value=metric.value,
                levels=metric.levels,
                boundaries=metric.boundaries,
            )
            yield Metric(f"kube_memory_{requirement_name}", requirement)
        else:
            # TODO Add new logic to reduce code duplication.
            summary = f"{requirement_name.title()}: n/a"
            if requirement == ExceptionalResource.unspecified:
                yield Result(
                    state=State.OK,
                    summary=summary,
                    details=f"{requirement_name.title()}: not specified for at least one container",
                )
            if requirement == ExceptionalResource.zero:
                yield Result(
                    state=State.OK,
                    summary=summary,
                    details=f"{requirement_name.title()}: set to zero for at least one container",
                )
            if requirement == ExceptionalResource.zero_unspecified:
                yield Result(
                    state=State.OK,
                    notice=f"{requirement_name.title()}: not specified for at least one container",
                )
                yield Result(
                    state=State.OK,
                    summary=summary,
                    details=f"{requirement_name.title()}: set to zero for at least one container",
                )


register.check_plugin(
    name="kube_memory",  # TODO change this plugin name
    service_name="Container memory",  # TODO change this service name
    sections=["kube_memory_resources", "k8s_live_memory"],
    discovery_function=discovery_kube_memory,
    check_function=check_kube_memory,
    check_ruleset_name="kube_memory",
    check_default_parameters=_DEFAULT_PARAMS,
)
