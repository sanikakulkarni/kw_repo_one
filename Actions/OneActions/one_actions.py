import Framework.Utils as Utils
import time
from Framework.Utils.testcase_Utils import pNote, pSubStep, report_substep_status


class OneActions(object):
    """One Actions Class """

    def __init__(self):
        self.resultfile = Utils.config_Utils.resultfile
        self.datafile = Utils.config_Utils.datafile
        self.logsdir = Utils.config_Utils.logsdir
        self.filename = Utils.config_Utils.filename
        self.logfile = Utils.config_Utils.logfile

    def one_actions_timeout(self, timeout):
        """
	One Actions timeout keyword doc strings
        """
        wdesc = "One Actions Keyword times out for 5 seconds"
        pSubStep(wdesc)
        status = True
        
        time.sleep(5)
        
        report_substep_status(status)
        return status
