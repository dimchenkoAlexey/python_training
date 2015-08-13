__author__ = 'admin'


class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # open home page
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
