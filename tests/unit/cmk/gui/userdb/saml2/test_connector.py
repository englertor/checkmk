#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
import copy
from typing import Any, Iterable

import pytest

from cmk.utils.type_defs import UserId

from cmk.gui.type_defs import Users, UserSpec
from cmk.gui.userdb.htpasswd import HtpasswdUserConnector
from cmk.gui.userdb.saml2.connector import Connector, SAML2_CONNECTOR_TYPE
from cmk.gui.userdb.store import OpenFileMode, UserStore


class TestConnector:
    @pytest.fixture(autouse=True)
    def patch_metadata_from_idp(self, metadata_from_idp: None) -> None:
        return metadata_from_idp

    @pytest.fixture
    def users_pre_edit(self) -> Users:
        return {
            UserId("Moss"): UserSpec({"connector": "ldap", "email": "moss@helloit.com"}),
            UserId("Roy"): UserSpec({"connector": "htpasswd", "email": "roy@helloit.com"}),
            UserId("Richmond"): UserSpec(
                {"connector": SAML2_CONNECTOR_TYPE, "email": "richmond@helloit.com"}
            ),
        }

    @pytest.fixture
    def user_store(self, monkeypatch: pytest.MonkeyPatch, users_pre_edit: Users) -> Iterable[Users]:
        users = copy.deepcopy(users_pre_edit)

        class MockedUserStore(UserStore):
            def __init__(self, mode: OpenFileMode) -> None:
                super().__init__(mode)
                self.users = users

            def __exit__(self, *exc_info):
                return True

        monkeypatch.setattr("cmk.gui.userdb.saml2.connector.UserStore", MockedUserStore)
        yield users

    @pytest.fixture
    def connections_saml_connection(
        self, monkeypatch: pytest.MonkeyPatch, raw_config: dict[str, Any]
    ) -> None:
        monkeypatch.setattr(
            "cmk.gui.plugins.userdb.utils.get_connection", lambda i: (i, Connector(raw_config))
        )

    @pytest.fixture
    def connections_nonsaml_connection(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(
            "cmk.gui.plugins.userdb.utils.get_connection", lambda i: HtpasswdUserConnector({})
        )

    def test_connector_properties(self, raw_config: dict[str, Any]) -> None:
        connector = Connector(raw_config)
        assert connector.interface
        assert connector.type() == SAML2_CONNECTOR_TYPE
        assert connector.id == "uuid123"
        assert connector.identity_provider_url() == "https://myidp.com/some/path/to/metadata.php"

    def test_connector_is_enabled_config(self, raw_config: dict[str, Any]) -> None:
        config = {**raw_config, **{"disabled": False}}
        connector = Connector(config)
        assert connector.is_enabled() is True

    def test_connector_is_disabled_config(self, raw_config: dict[str, Any]) -> None:
        config = {**raw_config, **{"disabled": True}}
        connector = Connector(config)
        assert connector.is_enabled() is False

    def test_edit_user_does_not_create_new_user(
        self,
        raw_config: dict[str, Any],
        users_pre_edit: Users,
        user_store: Users,
    ) -> None:
        config = {**raw_config, **{"create_users_on_login": False}}
        connector = Connector(config)

        new_user_id = UserId("Paul")
        new_user_spec = UserSpec({})

        connector.create_and_update_user(new_user_id, new_user_spec)

        assert user_store == users_pre_edit

    def test_edit_user_creates_new_user(
        self,
        raw_config: dict[str, Any],
        users_pre_edit: Users,
        user_store: Users,
    ) -> None:
        config = {**raw_config, **{"create_users_on_login": True}}
        connector = Connector(config)

        new_user_id = UserId("Paul")
        new_user_spec = UserSpec({})
        new_user = {new_user_id: new_user_spec}

        connector.create_and_update_user(new_user_id, new_user_spec)

        assert user_store == {**users_pre_edit, **new_user}

    def test_edit_user_creates_new_user_with_default_profile(
        self,
        raw_config: dict[str, Any],
        users_pre_edit: Users,
        user_store: Users,
    ) -> None:
        config = {**raw_config, **{"create_users_on_login": True}}
        connector = Connector(config)

        new_user_id = UserId("Paul")

        connector.create_and_update_user(new_user_id)

        assert user_store == {
            **users_pre_edit,
            UserId("Paul"): UserSpec(
                {
                    "alias": "Paul",
                    "connector": "uuid123",
                    "contactgroups": [],
                    "force_authuser": False,
                    "roles": ["user"],
                }
            ),
        }

    def test_edit_user_does_not_overwrite_existing_user_in_different_namespace(
        self,
        raw_config: dict[str, Any],
        connections_nonsaml_connection: None,
        users_pre_edit: Users,
        user_store: Users,
    ) -> None:
        """Ensure SAML2 connector does not edit users that exist for a different connection (LDAP/HTPASSWD/...)."""

        config = {**raw_config, **{"create_users_on_login": True}}
        connector = Connector(config)

        new_user_id = UserId("Roy")
        new_user_spec = UserSpec({})

        connector.create_and_update_user(new_user_id, new_user_spec)

        assert user_store == users_pre_edit

    def test_edit_user_updates_user_profile(
        self,
        raw_config: dict[str, Any],
        connections_saml_connection: None,
        users_pre_edit: Users,
        user_store: Users,
    ) -> None:
        connector = Connector(raw_config)

        user_id = UserId("Richmond")
        new_user_spec = UserSpec({"email": "richmond@hellonerds.com", "connector": connector.id})

        connector.create_and_update_user(user_id, new_user_spec)

        assert user_store == {**users_pre_edit, **{user_id: new_user_spec}}
