import sys
import re
from configparser import ConfigParser
from fpdf import FPDF

# Read configuration
config = ConfigParser()
config.read('config.ini')

# Helper to read the first line from a file
def first_line(fn):
    f   = open(fn)
    str = f.readline()
    f.close()
    return str

# Convert unit strings to values
def parse_line_thickness(input_str):
    units = int(input_str)
    return units * float(config['geometry']['default_unit'])

# Read from data files given as command line arguments
sys.argv.pop(0)
for fn in sys.argv:

    # Extract short name of the data file and its content
    filehandle  = open(fn)
    fragment    = re.search('(\w+)\.data$', fn).group(1)
    line        = filehandle.readline()
    numbers     = list(map(parse_line_thickness, line.split(' ')))
    thickness   = sum(numbers)
    filehandle.close()

    # Log
    print(f'Writing {fragment}.pdf:', end = '')

    # Prepare PDF
    pdf = FPDF(
        orientation = config['papersize']['orientation'],
        format      = config['papersize']['name'],
        unit        = 'mm',
    )
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)

    # Draw lines
    start = (float(config['papersize']['width']) - thickness) / 2
    black = True
    y     = 0
    for th in numbers:
        if (black):
            pdf.rect(
                x       = 0,
                y       = start+y,
                w       = float(config['papersize']['height']),
                h       = th,
                style   = 'F',
            )
        y += th
        black = not(black)
        print(' ' + str(th), end = '')

    # Write to file
    pdf.output(f'output/pdf/{fragment}.pdf')
    print(' ...done.')
