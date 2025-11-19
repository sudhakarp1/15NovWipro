import configparser

config =  configparser.ConfigParser()
config.read('setup.ini')

print(config)
print(config['database'])
print(config['database']['host'])
print('*' * 60)
for section in config.sections():
    print(f'Section: {section}')
    for key, value in config[section].items():
        print(f'{key} --> {value}')
    print('=' * 50)
