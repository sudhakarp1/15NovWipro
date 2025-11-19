import os 

def dirContents(path):
    for base, dir, files in os.walk(path):
        print(f'Current Directory: {base}')
        print(f'Sub Directories: {dir}')
        print(f'files: {files}')
        print('*' * 40)

def dirContentsIteratively(path):
    stack = [path]
    while stack:
        currPath = stack.pop()
        for entry in os.listdir(currPath):
            fullPath = os.path.join(currPath, entry)
            if os.path.isdir(fullPath):
                print(f'Directory: {fullPath}')
                stack.append(fullPath)
            else:
                print(f'file: {fullPath}')

dirContentsIteratively('.')

