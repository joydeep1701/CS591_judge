import shutil
import os
import subprocess as sp
from multiprocessing import Pool
from uuid import uuid4
import time
import exceptions

class ProgramEvaluator:
    def __init__(self, folder_name):
        self._origin = folder_name
        self.dir = str(uuid4())

    def __enter__(self):
        shutil.copytree(self._origin, self.dir)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        shutil.rmtree(self.dir)

    def save_code(self, custom_code):
        with open(self.dir + "/module.c", "a") as code_file:
            code_file.write(custom_code)

    def compile(self):
        compiler = ['make', '--directory=' + self.dir]

        p = sp.run(compiler, stdout=sp.PIPE, stderr=sp.PIPE)
        stdout, stderr = p.stdout, p.stderr
        stdout = stdout.decode('utf-8')
        stderr = stderr.decode('utf-8')
        if stderr != '':
            raise exceptions.CompilationError(stderr)

        return p.returncode

    def run(self, arr):
        stdin, file_name, timeout = arr
        stdin = str.encode("".join(stdin))
        output = {}
        output['file_name'] = file_name
        start_time = time.time()
        try:
            executable_file = [self.dir + '/program']
            p = sp.run(executable_file,
                timeout=timeout,
                input=stdin,
                stdout=sp.PIPE,
                stderr=sp.PIPE,
            )
        except sp.TimeoutExpired:
            output['stdout'] = "Timeout Expired"
            return output
        end_time = time.time()
        output['time'] = end_time - start_time

        return_code = p.returncode
        stdout, stderr = p.stdout, p.stderr
        stdout = stdout.decode('utf-8')
        stderr = stderr.decode('utf-8')
        if not return_code:
            pass
        output['stdout'] = stdout

        return output

    def evaluate(self, test_data_dir, timeout=2):
        test_files = os.listdir(test_data_dir)
        test_cases = []
        for test_file in test_files:
            test_case = ""
            with open(test_data_dir + '/' + test_file) as f:
                test_case = f.readlines()
            test_cases.append([test_case, test_file, timeout])

        pool = Pool()
        result = pool.map(self.run, test_cases)
        pool.close()
        pool.join()
        return result
