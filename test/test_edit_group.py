# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group1", header="header1", footer="footer1"))
    app.group.modify(Group(name="group2", header="header2", footer="footer2"))
    app.session.logout()


def test_modify_group_to_null(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group3", header="header3", footer="footer3"))
    app.group.modify(Group(name="", header="", footer=""))
    app.session.logout()


def test_modify_group_from_null(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.group.modify(Group(name="group4", header="header4", footer="footer4"))
    app.session.logout()

