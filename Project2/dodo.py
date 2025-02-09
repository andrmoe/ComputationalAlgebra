from theory import generate_data_for_1a

def task_compile_pdf():
    return {'actions': [['pdflatex', '-interaction=nonstopmode', 'project2report.tex']],
            'file_dep': ['project2report.tex', 'prime_trial_table.tex', 'prime.py', 'theory.py', 'test.py'],
            'targets': ['project2report.pdf']}

def generate_data():

    return {'actions': [(generate_data_for_1a, [3, "py!\n"])],
            'file_dep': ['theory.py'],
            'targets': ['prime_trial_table.tex']}