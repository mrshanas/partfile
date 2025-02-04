""" Module for managing file reads in memory """

def chunk_file_read(page: int, filepath:str, chunk_size = 100):
    """
        Reads and loads only specified file chunk in memory
    """
    start_line = (page - 1) * chunk_size
    end_line = start_line + chunk_size
    lines = []

    try:
        # open function does not load an entire file into memory instead it returns a file object
        with open(filepath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if start_line <= i < end_line:
                    lines.append(line)
                elif i >= end_line:
                    break
    except FileNotFoundError:
        return {'error': 'File not found'}
    
    return {'page': page, 'lines': lines}