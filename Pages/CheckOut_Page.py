class CheckInOut:

    def __init__(self):
        self.admintool = '//*[@id="RadMenu1"]/ul/li[8]/a/span[1]'
        self.checkInout = '//*[@id="RadMenu1"]/ul/li[8]/div/ul/li[4]/a/span[2]'
        self.tooliframe = '/html/body/form/div[1]/table/tbody/tr[2]/td[2]/iframe'
        self.containLabel = '//*[@id="lblCaseNumber"]'
        self.contain = 'tbFilterByCaseNumber'
        self.case_verify ='/html/body/form/div[4]/div[1]/div/div[2]/span/div/div/div[1]/div[3]/table/tbody/tr[1]/td[1]'
        self.selectOption = 'ddCriteria'
        self.table = 'gvCheckInOut'
        self.badge = 'ctl00_ContentPlaceHolder1_btnCreateBadge_input'
        self.cancel = 'ctl00_ContentPlaceHolder1_btnCancelBadge_input'
