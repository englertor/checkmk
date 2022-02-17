#!/bin/bash
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


TESTEE="${UNIT_SH_AGENTS_DIR}/scripts/super-server/0_systemd/setup"


setUp() {
    # shellcheck source=../../agents/scripts/super-server/0_systemd/setup
    MK_SOURCE_ONLY="true" source "$TESTEE"

    RESOURCES="/systemd-resources"
    ROOT="${SHUNIT_TMPDIR}"
    export RESOURCES ROOT

    mkdir -p "${SHUNIT_TMPDIR}${RESOURCES}"

}


test_destination_fail() {
    ERRMSG="$(_destination 2>&1)"

    assertFalse $?
    assertContains "${ERRMSG}" "Unable to figure out where to put the systemd units"
}

test_destination_ok() {
    mkdir -p "${SHUNIT_TMPDIR}/usr/lib/systemd/system"
    touch "${SHUNIT_TMPDIR}/usr/lib/systemd/system/1"
    touch "${SHUNIT_TMPDIR}/usr/lib/systemd/system/2"
    mkdir -p "${SHUNIT_TMPDIR}/lib/systemd/system"
    touch "${SHUNIT_TMPDIR}/lib/systemd/system/1"
    touch "${SHUNIT_TMPDIR}/lib/systemd/system/2"
    touch "${SHUNIT_TMPDIR}/lib/systemd/system/3"

    assertEquals "/lib/systemd/system" "$(_destination)"
    assertEquals $'/lib/systemd/system\n/usr/lib/systemd/system' "$(_destination --all)"

}

test_systemd_version() {

    systemctl() {
        cat <<HERE
systemd 245 (245.4-4ubuntu3.15)
+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=hybrid
HERE
    }

    assertEquals "245" "$(_systemd_version)"
}

test_need_exec_stop_post_yes() {
    echo "ExecStopPost=/usr/bin/agent-updater-for-example" > "${SHUNIT_TMPDIR}${RESOURCES}/check-mk-agent@.service"
    assertTrue "_need_exec_stop_post"
}

test_need_exec_stop_post_no() {
    echo "something else" > "${SHUNIT_TMPDIR}${RESOURCES}/check-mk-agent@.service"
    assertFalse "_need_exec_stop_post"
}

test_systemd_sufficient_fail_for_219() {
    systemctl() { echo "systemd 219 (foobar)"; }
    echo "ExecStopPost=/usr/bin/agent-updater-for-example" > "${SHUNIT_TMPDIR}${RESOURCES}/check-mk-agent@.service"
    _systemd_present() { :; }
    _destination() { :; }

    ERRMSG=$(_systemd_sufficient 2>&1)

    assertFalse "$?"
    assertContains "${ERRMSG}" "ExecStopPost is buggy in systemd version 219"
}

# shellcheck disable=SC1090
. "$UNIT_SH_SHUNIT2"
