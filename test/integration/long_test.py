#!/usr/bin/python
import os
from test_common import *
def test_function(opts, port):
    stress_client = opts['stress']
    os.system(stress_client + ' -s localhost:%d -d infinity -c 16' % port)

if __name__ == "__main__":
    op = make_option_parser()
    auto_server_test_main(test_function, op.parse(sys.argv), timeout = None)
