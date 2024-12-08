# List of dangerous functions to blacklist
dangerous_functions = [
    'open', 'exec', 'eval', 'compile', 'globals', 'locals', 'del', 'exit', 'quit', 
    'system', 'os', 'subprocess', 'socket', 'popen', 'getattr', 'setattr', 'delattr', 
    'os.system', 'os.remove', 'os.rename', 'os.rmdir', 'os.remove', 'shutil', 'sys', 
    'traceback', 'importlib', 'input'
    
    # File and System Interaction
    'mkdir', 'rmdir', 'chdir', 'chmod', 'chown', 'link', 'symlink', 
    'unlink', 'pipe', 'mkfifo', 'mknod',
    
    # Reflection and Introspection
    'vars', 'dir', 'id', 'type', 'hasattr', 'callable', 
    'issubclass', 'isinstance',
    
    # Module and Import Related
    'reload', 'breakpoint', 
    'module', 'NamespaceModule', 'runpy',
    
    # Networking and Remote Execution
    'asyncio', 'http', 'telnetlib', 'urllib', 'xmlrpc', 
    'threading', 'multiprocessing', 'ctypes',
    
    # Potentially Dangerous Standard Libraries
    'pickle', 'marshal', 'shelve', 'tempfile', 
    'secrets', 'random', 'crypto', 'hmac'
]
