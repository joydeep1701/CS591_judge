class CompilationError(Exception):
    def __init__(self, stderr):
        self.stderr = stderr
    def __repr__(self):
        return self.stderr

class RuntimeError(Exception):
    pass
