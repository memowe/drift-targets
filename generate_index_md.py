from configparser import ConfigParser

# Read configuration
config = ConfigParser()
config.read('config.ini')

# Prepare output file
filehandle = open('output/index.md', 'w')
filehandle.write("# Drift Targets\n\n")

# Write strip data names to PDF file
for name in config['strips']:
    filehandle.write(f"- [{name}.pdf](pdf/{name}.pdf)\n")

filehandle.close()
