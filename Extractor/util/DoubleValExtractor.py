# 一个专门用于提取ll文件double类型变量和相关函数以及double类型的函数的工具类
class DoubleValExtractor:
    source_file_path = ''
    ll_file_content_list = []
    vm_module = []
    double_var_list = []
    double_func_list = []

    def __init__(self, source_file_path):
        self.source_file_path = source_file_path
        with open(self.source_file_path, 'r') as ll_file:
            ll_file_content = ll_file.read()
        tmp_list = ll_file_content.split('\n')
        for line in tmp_list:
            self.ll_file_content_list.append(line.strip())


    def extract_double_functions(self):

        return False


    # TODO
    def extract_double_var(self):
        return False


    def is_variable(self, line):
        
        return False


    def is_block_end(self, line):
        return line == '\n'


extractor = DoubleValExtractor('/Users/py/GitHub/LLVM/functions/ll_file/sqrt_minus.ll')
for line in extractor.ll_file_content_list:
    print(line)

        