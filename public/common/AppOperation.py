from public.common.basepage import BasePage

class AppOperation(BasePage):

    def __init__(self) -> None:
        super.__init__()
    @staticmethod
    def Installapp(self,appInstallPath):
        self.driver.install_app(appInstallPath)
    #检查已安转的app
    def checkappInstalled(self,appname):
        self.driver.is_app_installed(appname)

    def closeApp(self):
        self.driver.close_app()