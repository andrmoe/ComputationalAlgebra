import inspect
import importlib


def extract_function_to_file(module_name: str, function_names: [str]) -> bool:
    module = importlib.import_module(module_name)
    for function_name in function_names:
        func = getattr(module, function_name, None)
        source_code = inspect.getsource(func)
        with open(f"temp/temp_{function_name}.py", "w") as f:
            f.write(source_code)
    return True