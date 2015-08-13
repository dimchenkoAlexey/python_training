# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="group3", header="header3", footer="footer3"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()
