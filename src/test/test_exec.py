import os
import shutil
import unittest
import platform

from executor.main import exec_job


def create_or_delete(p):
    if not os.path.exists(p):
        os.mkdir(p)
    else:
        shutil.rmtree(p)
        os.mkdir(p)


class TestExec(unittest.TestCase):

    def test_exec_job(self):
        test_folder = os.path.join(os.path.abspath(os.path.join(__file__, '..')), 'resources')
        test_path = os.path.join(test_folder, 'log.log')
        create_or_delete(test_folder)

        exec_job('echo 1', test_path)
        try:
            exec_job('wrong', test_path)
        except:
            pass

        if platform.system() == 'Darwin':
            expected_output = ['1\n', '\n', '/bin/sh: wrong: command not found\n', '\n']
        else:
            expected_output = ['1\n', '\n', '/bin/sh: 1: wrong: not found\n', '\n']

        with open(test_path) as f:
            output = f.readlines()

        self.assertListEqual(output, expected_output)

        # create_or_delete(test_folder)
