'''
sys:
    list called argv # stores all command line arguments
    exit()
    list called path
    standard file like stdin, stdout and stderr
    variables storing Python(version), Platform(platform like nt, posix)
    modules loaded (dictionary called modules)
'''
import sys

print(f'args: {sys.argv}\t\tNum: {len(sys.argv)}')
print(f'version: {sys.version}')
print(f'platform: {sys.platform}')
print(f'Modules: {sys.modules.keys()}')
print('This is the output Message')#default
print('This is the Error Message', file = sys.stderr)
