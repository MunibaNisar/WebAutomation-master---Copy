from Tests.LoginTCs import LoginTcs

login = LoginTcs()


class commonMethod:

    def test_logincms(self):
        # use in all other function
        driver = login.test_login()
        return driver
