import os
from inspect import getframeinfo, stack, getfile

# file name to which sequence diagram will be written
seq_f_name = "lock.puml"
is_seq_on = True

def writeSeqFile(content=""):
    with open(seq_f_name, 'a+') as file:
        file.write(content)

def seq():
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            if is_seq_on:
                i_stack = stack()
                caller = getframeinfo(i_stack[1][0])
                # caller_func = i_stack[1][3]
                caller_f = caller.filename
                caller_f = get_filename(caller_f)
                current_f = getfile(f)
                current_f = get_filename(current_f)
                writeSeqFile("\n" + caller_f + " -> " + current_f + " : " + f.__name__)
                writeSeqFile("\nactivate " + current_f)
                ret = f(*args, **kwargs)
                writeSeqFile("\n" + current_f + " --> " + caller_f + " : " + f.__name__ + " response")
                writeSeqFile("\ndeactivate " + current_f)
            else:
                ret = f(*args, **kwargs)
            return ret
        return wrapped_f
    return wrap

# Example
# @seq()
# def testb(b, bb):
#     # print(b, bb)
#     pass
#
# @seq()
# def sayHello(a1, a2, a3, a4):
#     testb(a1, a2)
#
#
# sayHello("say", "hello", "argument", "list")

def get_filename(f_path):
    f_name_full = os.path.basename(f_path)
    f_name = f_name_full[:-3]
    return f_name