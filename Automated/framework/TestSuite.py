from unittest import runner
from Automated.framework.GetConfig import GetConfig
import unittest
import HTMLReport
import time




if __name__ == "__main__":

    reportPath = GetConfig().get_Path('report_path')
    reportTime = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    reportFile = reportTime + "report" 
    
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().discover(
        start_dir=r"E:\python_jenkins\workspace\python_project001\Automated\testsuites",
        pattern="*Case.py",
        top_level_dir=None
    ))

    runner = HTMLReport.TestRunner(
        report_file_name=reportFile,
        output_path=reportPath,
        thread_count=3
    )

    runner.run(suite)

