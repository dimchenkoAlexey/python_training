from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    app.navigation.return_to_home_page()
    app.contact.delete_first_contact()
    app.navigation.modal_window_ok()


def test_delete_cancelled(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    app.navigation.return_to_home_page()
    app.contact.delete_first_contact()
    app.navigation.modal_window_cancel()


def test_delete_all(app):
    if app.contact.count() < 2:
        app.contact.create(Contact(firstname="firstname"))
        app.contact.create(Contact(firstname="1"))
    app.navigation.return_to_home_page()
    app.contact.delete_all_contacts()
    app.navigation.modal_window_ok()

