class Attorney:
    def __init__(self):
        self.admintool = '//*[@id="RadMenu1"]/ul/li[8]/a/span[1]'
        self.attorney = '//*[@id="RadMenu1"]/ul/li[8]/div/ul/li[1]/a/span[2]'
        self.attorneyiframe = '/html/body/form/div[1]/table/tbody/tr[2]/td[2]/iframe'
        self.attorneyPage = 'ctl00_ContentPlaceHolder1_Label1'
        self.add = 'ctl00_ContentPlaceHolder1_btnAdd'
        self.firstName = 'ctl00_ContentPlaceHolder1_EditPanel_C_tbFirstName'
        self.lastName = 'ctl00_ContentPlaceHolder1_EditPanel_C_tbLastName'
        self.save = 'ctl00_ContentPlaceHolder1_EditPanel_C_btnSave_input'
        self.cancelBtn = 'ctl00_ContentPlaceHolder1_EditPanel_C_btnCancel_input'
        self.attorneySearch = 'ctl00_ContentPlaceHolder1_ddAttorneyLookup_Input'
        self.list = '/html/body/form/div[1]/div/div[1]/ul/li'
        self.table = 'ctl00_ContentPlaceHolder1_AttorneyGrid'
        self.noMatch = '//*[@id="ctl00_ContentPlaceHolder1_ddAttorneyLookup_MoreResultsBox"]/span'
        self.editBtn = '/html/body/form/div[4]/div[1]/div/div[1]/div/div[1]/table/tbody/tr[2]/td[6]/a'
        self.email = 'ctl00_ContentPlaceHolder1_EditPanel_C_tbEmail'
        self.alter = 'ctl00_ContentPlaceHolder1_lblHighlightedRecords'