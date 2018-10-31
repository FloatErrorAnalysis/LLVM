import os
jump_key_words = ['label']
function_key_words = ['call', 'ret']

# Consider all the val begin with that fucking %
# Get all the double val input and the function related

def init_ll(cc_file_name):
    cc_file_cmd = 'clang -Os -S -emit-llvm functions/' + cc_file_name + '.cpp -o functions/ll_file/' + cc_file_name + ".ll"
    print(os.system(cc_file_cmd))
    

# def get_input_list():


init_ll('sqrt_minus')
