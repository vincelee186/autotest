from seleniumbase import BaseCase
import uuid

class MyTestClass(BaseCase):

    def test_add_inactive(self):
        p_uuid = uuid.uuid4()

        #login
        url = "https://pncdn-qa-admin.pentium.network/"
        self.open(url)
        self.type('input#username', "admin")
        self.type('input#password', "admin")
        self.click('button[type="submit"]')
        self.assert_text("Client list", ".ant-page-header-heading-left")

    #addclient
        #Clientsetting
        self.click('button[class="ant-btn"]')
        self.assert_text("Add client", ".ant-page-header-heading-title")
        
        self.type('input#username', (str(p_uuid)))
        self.type('input#password', (str(p_uuid)))
        self.type('input#email', f"{(str(p_uuid))}@gmail.com")
        self.type('input#phone', "0987654321")
        self.click('span[class="ant-radio"]')
        self.click('button[type="submit"]')

        #Finish
        self.assert_text("Successfully added client!", ".ant-result-title")
        self.click('button[class="ant-btn ant-btn-primary"]')

    #確認有無創建成功
        self.assert_text("Client list", ".ant-page-header-heading-left")
        n = len(self.find_elements('tr'))-1
        self.assert_text((str(p_uuid)),f'//tbody/tr[{n}]/td[1]')

        # self.assert_element_present('button[aria-checked="false"]',f"//tbody/tr[{n}]/td[4]")

    def test_login_error(self):
        #login
        url = "https://pncdn-qa-admin.pentium.network/"
        self.open(url)
        self.type('input#username', "test")
        self.type('input#password', "test")
        self.click('button[type="submit"]')
        self.assert_text("Invalid email or password", ".irPtrP")
        # assa









     





