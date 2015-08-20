__author__ = 'admin'


class Contact:

    def __init__(self,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 phone_home=None,
                 phone_mobile=None,
                 phone_work=None,
                 fax=None,
                 email_first=None,
                 email_second=None,
                 email_third=None,
                 homepage=None,
                 birth_day_list_item=None,
                 birth_month_list_item=None,
                 birth_year=None,
                 anniversary_day_list_item=None,
                 anniversary_month_list_item=None,
                 anniversary_year=None,
                 second_address=None,
                 second_phone=None,
                 notes=None):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.fax = fax
        self.email_first = email_first
        self.email_second = email_second
        self.email_third = email_third
        self.homepage = homepage
        self.birth_day_list_item = birth_day_list_item
        self.birth_month_list_item = birth_month_list_item
        self.birth_year = birth_year
        self.anniversary_day_list_item = anniversary_day_list_item
        self.anniversary_month_list_item = anniversary_month_list_item
        self.anniversary_year = anniversary_year
        self.second_address = second_address
        self.second_phone = second_phone
        self.notes = notes
