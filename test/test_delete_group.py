from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    # группа добавляется на случай если нет ни одной группы
    app.group.create(Group(name="group4", header="header4", footer="footer4"))
    app.group.delete_first_group()
    app.session.logout()


def test_delete_all_groups(app):
    app.session.login(username="admin", password="secret")
    # группа добавляется на случай если нет ни одной группы
    app.group.create(Group(name="group5", header="header5", footer="footer5"))
    app.group.create(Group(name="group6", header="header6", footer="footer6"))
    app.group.delete_all_groups()
    app.session.logout()
