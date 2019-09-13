import sys
import re

# Prepare output file
filehandle = open('output/index.md', 'w')

# Read from data files given as command line arguments
sys.argv.pop(0)
for fn in sys.argv:

    # Extract short name of the data file
    fragment = re.search('(\w+)\.data$', fn).group(1)

    # Generate markdown link to PDF file
    filehandle.write(f"- [{fragment}.pdf](pdf/{fragment}.pdf)\n")

filehandle.close()
