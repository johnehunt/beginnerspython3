# Illustrates printing out a traceback of
# the call stack when the exception was raised
import traceback

try:
    print(6 / 0)
except Exception as exp:
    print('oops')
    print(exp)
    traceback.print_exc()
