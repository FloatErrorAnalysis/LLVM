# 一个专门用于提取ll文件double类型变量和相关函数以及double类型的函数的工具类
'''  全局标识符（函数，全局变量）以“@”字符开头。
     本地标识符（注册名称，类型）以'％'字符开头  '''


class DoubleValExtractor:
    source_file_path = ''
    ll_file_content_list = []
    vm_module = []
    double_vars = []
    double_functions = []
    double_statements = []

    def __init__(self, source_file_path):
        self.source_file_path = source_file_path
        with open(self.source_file_path, 'r') as ll_file:
            ll_file_content = ll_file.read()
        tmp_list = ll_file_content.split('\n')
        for line in tmp_list:
            self.ll_file_content_list.append(line.strip())
            if 'double' in line:
                self.double_statements.append(line)

    def extract_double_functions(self):
        # 定义的double函数，以 define double标识开头 '}'结尾
        flag = False
        for line in self.ll_file_content_list:
            if 'define double' in line:
                flag = True

            if flag:
                self.double_functions.append(line)
            if '}' in line:
                flag = False
            # 申明
            if 'declare double' in line:
                self.double_functions.append(line)

        return self.double_functions

    # TODO
    def extract_double_vars(self):
        for statement in self.double_statements:
            # 列出所有double型临时寄存器
            if statement.find('%') != -1:
                idx = statement.find('%')
                if statement[idx + 1: idx + 2].isalnum():
                    self.double_vars.append('%' + statement[idx + 1: idx + 2])

        return list(set(self.double_vars))

    def extract_double_concerned_statements(self):
        return list(set(self.double_statements + self.extract_double_functions()))


extractor = DoubleValExtractor('/Users/py/GitHub/LLVM/functions/ll_file/sqrt_minus.ll')
with open('double_ll', 'w') as f:
    f.writelines(extractor.extract_double_concerned_statements())

