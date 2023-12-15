import os

from pysapscript.src.pysapscript import Sapscript
from pysapscript.src.types.types import NavigateAction


class TestRuns:
    def __init__(self):
        self.pss = Sapscript()

        pwd = os.getenv("sap_sq8_006_robot01_pwd"),

        # Turns on
        self.pss.launch_sap(
            sid="SQ8",
            client="006",
            user="robot01_t",
            password=str(pwd)
        )

        self.window = self.pss.attach_window(0, 0)

    def test_runs(self):
        # Basic actions
        self.window.start_transaction("se16")
        self.window.write("wnd[0]/usr/ctxtDATABROWSE-TABLENAME", "LFA1")
        self.window.navigate(NavigateAction.enter)

        self.window.press("wnd[0]/tbar[1]/btn[31]")
        value = self.window.read("wnd[1]/usr/txtG_DBCOUNT")
        print("Element value: " + value)
        self.window.press("wnd[1]/tbar[0]/btn[0]")

        # Table
        self.window.write("wnd[0]/usr/txtMAX_SEL", "20")
        self.window.press("wnd[0]/tbar[1]/btn[8]")
        table = self.window.read_shell_table("wnd[0]/usr/cntlGRID1/shellcont/shell")
        print(table.head())

        self.window.navigate(NavigateAction.back)
        self.window.navigate(NavigateAction.back)
        self.window.navigate(NavigateAction.back)

        # New window
        self.pss.open_new_window(window_to_handle_opening=self.window)
        window2 = self.pss.attach_window(0, 1)
        window2.start_transaction("SQVI")
        window2.close_window()


if __name__ == "__main__":
    TestRuns().test_runs()