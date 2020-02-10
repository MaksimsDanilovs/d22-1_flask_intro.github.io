file_name = "data.txt"

def rewrite_file(lines):
    f = open(file_name, 'w')
    for line in lines:
        f.write(line)
    
    f.close()

def write_file(line):
    f = open(file_name, 'a')
    f.write(line + '\n')
    f.close()

def read_file():
    f = open(file_name, 'r')
    if f.mode == 'r':
        content = f.read()
    else:
        content = f"Can't read file {file_name}"

    return content

def read_lines():
    with open(file_name) as f:
        lines = f.readlines()
    
    return lines