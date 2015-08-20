# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.group.create(Group(name="group1", header="header1", footer="footer1"))
    app.group.modify(Group(name="group2", header="header2", footer="footer2"))


def test_modify_group_to_null(app):
    app.group.create(Group(name="group3", header="header3", footer="footer3"))
    app.group.modify(Group(name="", header="", footer=""))


def test_modify_group_from_null(app):
    app.group.create(Group(name="", header="", footer=""))
    app.group.modify(Group(name="group4", header="header4", footer="footer4"))


def test_modify_group_with_one_attribute(app):
    app.group.create(Group(name="group5", header="header5", footer="footer5"))
    app.group.modify(Group(name="group55555"))
