class Bondsman:
    def __init__(self):
        self.admintool = '//*[@id="RadMenu1"]/ul/li[8]/a/span[1]'
        self.bondsman = '//*[@id="RadMenu1"]/ul/li[8]/div/ul/li[2]/a/span[2]'
        self.bondsmaniframe = '/html/body/form/div[1]/table/tbody/tr[2]/td[2]/iframe'
        self.bondsmanSearch = 'ctl00_ContentPlaceHolder1_Label1'
        self.addBtn = 'ctl00_ContentPlaceHolder1_btnAdd_input'
        self.firstName = 'ctl00_ContentPlaceHolder1_EditPanel_C_tbFirstName'
        self.lastName = 'ctl00_ContentPlaceHolder1_EditPanel_C_tbLastName'
        self.save = 'ctl00_ContentPlaceHolder1_EditPanel_C_btnSave_input'
        self.cancelBtn = 'ctl00_ContentPlaceHolder1_EditPanel_C_btnCancel_input'
        self.bondsmanSearchField = 'ctl00_ContentPlaceHolder1_ddBondsmanLookup_Input'
        self.listBondsman = '/html/body/form/div[1]/div/div[1]/ul'
        self.table = 'ctl00_ContentPlaceHolder1_BondsmanGrid'
        self.matches = "/html/body/form/div[1]/div/div[2]/span"
        self.editBtn = "/html/body/form/div[4]/div[1]/div/div/div/div/table/tbody/tr[2]/td[2]/a"
        self.email = "ctl00_ContentPlaceHolder1_EditPanel_C_tbEmail"
        self.deleteBtbn = "/html/body/form/div[4]/div[1]/div/div/div/div/table/tbody/tr[2]/td[3]/a"