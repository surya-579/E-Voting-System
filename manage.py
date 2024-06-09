# manage.py

import os
import sys
import warnings

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_voting.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Suppress GLib-GIO warnings
    if sys.platform == "win32":
        import ctypes
        stderr_handle = ctypes.windll.kernel32.GetStdHandle(-12)
        if stderr_handle:
            def write(data):
                written = ctypes.c_ulong()
                ctypes.windll.kernel32.WriteFile(stderr_handle, data.encode(), len(data), ctypes.byref(written), None)
            sys.stderr.write = write

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
