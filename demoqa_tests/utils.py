def upload_source(path):
    import demoqa_tests
    demoqa_tests.__file__
    from pathlib import Path
    return str(Path(demoqa_tests.__file__)
               .parent
               .parent
               .joinpath(f'demoqa_tests/{path}')
               )
