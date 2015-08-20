__author__ = 'admin'


class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # open home page
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        # open home page
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/")):
            wd.find_element_by_link_text("home").click()

    def modal_window_ok(self):
        wd = self.app.wd
        wd.switch_to.alert.accept()

    def modal_window_cancel(self):
        wd = self.app.wd
        wd.switch_to.alert.dismiss()
