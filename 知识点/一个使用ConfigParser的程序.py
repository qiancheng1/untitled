from configparser import ConfigParser

CONFIGFILE = 'area.ini'

config = ConfigParser()
config.read(CONFIGFILE)

print(config['messages'].get("greeting"))

radis = float(input(config['messages'].get('question')))
print(radis)

print(config['messages'].get('result_message'), end=' ')