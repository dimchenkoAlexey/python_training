# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact_from_null(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                       nickname="", title="", company="", address="", phone_home="",
                       phone_mobile="", phone_work="", fax="",email_first="", email_second="",email_third="",
                       homepage="", second_address="", second_phone="",
                       notes="", birth_day_list_item="1", birth_month_list_item="1", birth_year="", anniversary_day_list_item="1", anniversary_month_list_item="1", anniversary_year=""))
    app.navigation.return_to_home_page()
    app.contact.modify(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                       nickname="nickname", title="title", company="company", address="address", phone_home="1111111",
                       phone_mobile="2222222", phone_work="3333333", fax="4444444",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                       homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                       notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))


def test_edit_contact_to_null(app):
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                       nickname="nickname", title="title", company="company", address="address", phone_home="1111111",
                       phone_mobile="2222222", phone_work="3333333", fax="4444444",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                       homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                       notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))
    app.navigation.return_to_home_page()
    app.contact.modify(Contact(firstname="", middlename="", lastname="",
                       nickname="", title="", company="", address="", phone_home="",
                       phone_mobile="", phone_work="", fax="",email_first="", email_second="",email_third="",
                       homepage="", second_address="", second_phone="",
                       notes="", birth_day_list_item="1", birth_month_list_item="1", birth_year="", anniversary_day_list_item="1", anniversary_month_list_item="1", anniversary_year=""))


def test_edit_contact_to_not_null(app):
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                       nickname="nickname", title="title", company="company", address="address", phone_home="1111111",
                       phone_mobile="2222222", phone_work="3333333", fax="4444444",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                       homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                       notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))
    app.navigation.return_to_home_page()
    app.contact.modify(Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2",
                       nickname="nickname2", title="title2", company="company2", address="address2", phone_home="22222222",
                       phone_mobile="333333", phone_work="444444", fax="555555",email_first="e1-mail@mail.ru2", email_second="e2-mail@mail.ru2",email_third="e3-mail@mail.ru2",
                       homepage="http://homepage.ru2", second_address="St-Petersburg, street, building, 12", second_phone="1232",
                       notes="go2", birth_day_list_item="6", birth_month_list_item="7", birth_year="20002", anniversary_day_list_item="5", anniversary_month_list_item="4", anniversary_year="2016"))


def test_edit_contact_with_one_attribute(app):
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                       nickname="nickname", title="title", company="company", address="address", phone_home="1111111",
                       phone_mobile="2222222", phone_work="3333333", fax="4444444",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                       homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                       notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))
    app.navigation.return_to_home_page()
    app.contact.modify(Contact(firstname="firstname1000"))
