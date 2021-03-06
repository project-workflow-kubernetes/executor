import argparse
import time
import subprocess as sp
from executor import settings as s


def exec_job(cmd, logs_path):
    process = sp.Popen(cmd,
                       stdin=sp.PIPE,
                       stdout=sp.PIPE,
                       stderr=sp.STDOUT,
                       close_fds=True,
                       shell=True)

    while process.poll() == 0:
        time.sleep(0.1)

    out, err = process.communicate()
    out = out.decode('utf-8').split('\n') if out else out
    err = err.decode('utf-8').split('\n') if err else err

    with open(logs_path, "a") as fp:
        if out:
            for o in out:
                fp.write("%s\n" % o)
        if err:
            for e in err:
                fp.write("%s\n" % e)

    # another alternative is check_output but can not allows to write in the files
    if process.returncode != 0:
        raise Exception(out)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", help="cmd", type=str)
    args = parser.parse_args()
    cmd = args.cmd

    exec_job(cmd, s.LOGS_PATH)
