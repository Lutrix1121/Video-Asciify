import os
import shutil


def create_directories(directories):
    """Create multiple directories if they don't exist."""
    for directory in directories:
        if not os.path.exists(directory):
            os.mkdir(directory)


def cleanup_directories(directories):
    """Remove directories and all their contents."""
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)


def ensure_directory_exists(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.mkdir(directory)
        return True
    return False


def safe_remove_directory(directory):
    """Safely remove directory if it exists."""
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            return True
    except OSError as e:
        print(f"Error removing directory {directory}: {e}")
        return False
    return False
