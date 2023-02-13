# Time : 2023/2/10 11:20
# import os
# import time
import pytest

from conftest import cFromCsvToJson, dEnvReplaceYaml, bget_encoding

if __name__ == '__main__':
    bget_encoding()
    cFromCsvToJson(csv_path='csvdata/company_moddle.csv')
    dEnvReplaceYaml(yaml_file='testcases/Companies/company_list.yml', new_yaml_file='hotdata/new_yaml_files/nyf.yaml')
    pytest.main()
    # time.sleep(3)
    # os.system('allure generate ./temps -o reports --clean') # -o output到reports目录