from model.contact import Contact


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    # контакт добавляется на случай если нет ни одного контакта
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                       nickname="nickname", title="title", company="company", address="address", phone_home="1111111",
                       phone_mobile="2222222", phone_work="3333333", fax="4444444",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                       homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                       notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))
    app.navigation.return_to_home_page()
    app.contact.delete_first_contact()
    app.navigation.modal_window_ok()
    app.session.logout()


def test_delete_cancelled(app):
    app.session.login(username="admin", password="secret")
    # контакт добавляется на случай если нет ни одного контакта
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                       nickname="nickname", title="title", company="company", address="address", phone_home="1111111",
                       phone_mobile="2222222", phone_work="3333333", fax="4444444",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                       homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                       notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))
    app.navigation.return_to_home_page()
    app.contact.delete_first_contact()
    app.navigation.modal_window_cancel()
    app.session.logout()


def test_delete_all(app):
    app.session.login(username="admin", password="secret")
    # контакт добавляется на случай если нет ни одного контакта
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                       nickname="nickname", title="title", company="company", address="address", phone_home="1111111",
                       phone_mobile="2222222", phone_work="3333333", fax="4444444",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                       homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                       notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))
    app.contact.create(Contact(firstname="1", middlename="2", lastname="3",
                       nickname="4", title="5", company="6", address="7", phone_home="8",
                       phone_mobile="9", phone_work="10", fax="11",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                       homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                       notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))
    app.navigation.return_to_home_page()
    app.contact.delete_all_contacts()
    app.navigation.modal_window_ok()
    app.session.logout()

