import sys
import re
from configparser import ConfigParser
from fpdf import FPDF

# Read configuration
config = ConfigParser()
config.read('config.ini')

# Convert unit strings to values
def parse_strips(s):
    factor = float(config['geometry']['default_unit'])
    return list(map(lambda s: factor * float(s), s.split(' ')))

# Process strip data
for name, numbers in config['strips'].items():

    # Log
    print(f'Writing {name}.pdf:', end = '')

    # Prepare PDF
    pdf = FPDF(
        orientation = config['papersize']['orientation'],
        format      = config['papersize']['name'],
        unit        = 'mm',
    )
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)

    # Parse data
    strips      = parse_strips(numbers)
    thickness   = sum(strips)

    # Draw lines
    start = (float(config['papersize']['width']) - thickness) / 2
    black = True
    y     = 0
    for th in strips:
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

    # Add target name
    pdf.set_font('Helvetica', 'B', 8)
    pdf.text(x = 20, y = start + y + 10, txt = name)

    # Write to file
    pdf.output(f'output/pdf/{name}.pdf')
    print(' ...done.')
