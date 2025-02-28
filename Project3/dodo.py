import os
from typing import Generator
import inspect
import importlib
import re
from doit.tools import create_folder


def extract_function_to_file(module_name: str, function_name: str) -> bool:
    module = importlib.import_module(module_name)
    func = getattr(module, function_name, None)
    source_code = inspect.getsource(func)
    with open(f"temp/func-{module_name}-{function_name}.py", "w") as f:
        f.write(source_code)
    return True


def get_file_refs(file_path: str) -> Generator[str, None, None]:
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    with open(file_path, "r") as f:
        file_content = f.read()
        for file in files:
            ext = file.split(".")[-1]
            file_no_ext = file.replace("."+ext, "")
            if (
                file in file_content
                or "{" + file_no_ext in file_content
                or f"import {file_no_ext}" in file_content
                or f"from {file_no_ext}" in file_content
            ):
                yield file


def get_func_code_refs(file_path: str) -> Generator[tuple[str, str], None, None]:
    with open(file_path, 'r') as f:
        content = f.read()
        regex = 'temp\/func-([a-zA-Z0-9_]+)-([a-zA-Z0-9_]+)\.py'
        matches = re.findall(regex, content)
        for match in matches:
            yield match[0], match[1]


def task_temp_folder():
    return {'actions': [(create_folder, ['temp'])], 'targets': ['temp']}


def task_compile_pdf():
    report_name = "project3report"
    return {
        "actions": [
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-output-directory=temp",
                f"{report_name}.tex",
            ]
        ],
        "file_dep": [f"{report_name}.tex"] + list(get_file_refs(f"{report_name}.tex")) +
        [f'temp/func-{module}-{func}.py' for module, func in get_func_code_refs(f"{report_name}.tex")],
        "targets": [f"temp/{report_name}.pdf"],
    }


def task_check_python_dependencies():
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for file in files:
        if file.split('.')[-1] != 'py':
            continue
        dependencies = list(get_file_refs(file))
        if len(dependencies):
            yield {'name': file, 'actions': [], 'file_dep': dependencies, 'targets': [file]}


def task_generate_func_code():
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for file in files:
        if file.split('.')[-1] != 'tex':
            continue
        for module, func in get_func_code_refs(file):
            yield {'name': f'func-{module}-{func}.py',
                   'actions': [(extract_function_to_file, [], {'module_name': module, 'function_name': func})],
                   'file_dep': [f'{module}.py'],
                   'targets': [f'temp/func-{module}-{func}.py']}
