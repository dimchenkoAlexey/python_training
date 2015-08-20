# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create(Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                       nickname="nickname", title="title", company="company", address="address", phone_home="1111111",
                       phone_mobile="2222222", phone_work="3333333", fax="4444444",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                       homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                       notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                       nickname="", title="", company="", address="", phone_home="",
                       phone_mobile="", phone_work="", fax="",email_first="", email_second="",email_third="",
                       homepage="", second_address="", second_phone="",
                       notes="", birth_day_list_item="1", birth_month_list_item="1", birth_year="", anniversary_day_list_item="1", anniversary_month_list_item="1", anniversary_year=""))


