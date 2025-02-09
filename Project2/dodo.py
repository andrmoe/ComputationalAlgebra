from theory import *

def task_compile_pdf():
    return {'actions': [['pdflatex', '-interaction=nonstopmode', 'project2report.tex']],
            'file_dep': ['project2report.tex', 'prime_trial_table.tex', 'range_size_table.tex', 'prime.py', 'theory.py',
                         'test.py'],
            'targets': ['project2report.pdf']}

def task_generate_data_1a():
    return {'actions': [(generate_data_1a, )],
            'file_dep': ['theory.py'],
            'targets': ['prime_trial_table.tex']}

def task_generate_data_1b():
    return {'actions': [(generate_data_1b, )],
            'file_dep': ['theory.py'],
            'targets': ['range_size_table.tex']}

