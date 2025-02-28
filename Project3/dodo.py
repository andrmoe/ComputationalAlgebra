

def task_compile_pdf():
    report_name = 'project3report'
    return {'actions': [['pdflatex', '-interaction=nonstopmode', '-output-directory=temp', f'{report_name}.tex']],
            'file_dep': [f'{report_name}.tex'],
            'targets': [f'temp/{report_name}.pdf']}
