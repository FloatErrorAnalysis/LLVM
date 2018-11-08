class DoubleValExtractor:
    source_file_path = ''
    ll_file_content = []
    vm_module = []
    double_var_list = []
    double_func_list = []

    def __init__(self, source_file_path):
        self.source_file_path = source_file_path
        with open(self.source_file_path, 'r') as ll_file:
            self.ll_file_content = ll_file.read()


    def extract_double_functions(self):
        return False


    # TODO
    def extract_double_var(self):
        return False


extractor = DoubleValExtractor('/Users/py/GitHub/LLVM/functions/ll_file/sqrt_minus.ll')
print(extractor.ll_file_content)


        