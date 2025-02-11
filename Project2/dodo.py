from theory import *
from extract_function_to_file import extract_function_to_file

def task_compile_pdf():
    return {'actions': [['pdflatex', '-interaction=nonstopmode', '-output-directory=temp', 'project2report.tex']],
            'file_dep': ['project2report.tex', 'temp/prime_trial_table.tex', 'temp/range_size_table.tex',
                         'temp/sieve_table.tex', 'prime.py', 'theory.py', 'test.py', 'experiment.py',
                         'temp/fermat_test.py', 'temp/find_prime_generic.py', 'temp/find_prime.py',
                         'temp/trial_division_test.py', 'temp/prime_sieve.py'],
            'targets': ['temp/project2report.pdf']}

def task_generate_data_1a():
    return {'actions': [(generate_data_1a, )],
            'file_dep': ['theory.py'],
            'targets': ['temp/prime_trial_table.tex']}

def task_generate_data_1b():
    return {'actions': [(generate_data_1b, )],
            'file_dep': ['theory.py'],
            'targets': ['temp/range_size_table.tex']}

def task_generate_data_1c():
    return {'actions': [(generate_data_1c, )],
            'file_dep': ['theory.py'],
            'targets': ['temp/sieve_table.tex']}

def task_generate_prime_func_code():
    return {'actions': [(extract_function_to_file, [], {
                            'module_name': 'prime', 'function_names': ['fermat_test', 'find_prime_generic',
                                                                       'find_prime', 'trial_division_test',
                                                                       'prime_sieve']
                        })],
            'file_dep': ['prime.py'],
            'targets': ['temp/fermat_test.py', 'temp/find_prime_generic.py', 'temp/find_prime.py',
                        'temp/trial_division_test.py', 'temp/prime_sieve.py']}
