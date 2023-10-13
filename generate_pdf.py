import sys
from configparser import ConfigParser
from fpdf import FPDF

# Read configuraton
config = ConfigParser()
config.read('config.ini')

# Read target name from command line
if len(sys.argv) != 2:
  sys.exit('Target name expected as the program\'s (only) argument')
name = sys.argv[1]
if name not in config['strips']:
  sys.exit(f'Unknown target name: "{name}"')

file_name = f'output/pdf/{name}.pdf'
print(f'Writing {name} to {file_name}...', end='')

# Calculate strips
widths    = config['strips'][name]
factor    = float(config['geometry']['default_unit'])
strips    = [factor * float(s) for s in widths.split(' ')]
thickness = sum(strips)

# Prepare PDF
paper = config['papersize']
pdf = FPDF(
  orientation = paper['orientation'],
  format      = paper['name'],
  unit        = 'mm',
)
pdf.add_page()
pdf.set_fill_color(0, 0, 0)

# Draw lines
start = (float(paper['width']) - thickness) / 2
black = True
y     = 0
for th in strips:
  if black:
    pdf.rect(
      x=0, y=start+y, h=th, style='F',
      w=float(paper['height']))
  y += th
  black = not black
  print(' ' + str(th), end = '')

# Add target name
pdf.set_font('Helvetica', 'B', 8)
pdf.text(x=20, y=start+y+10, txt=name)

# Add arrow, if neccessary
if name == 'finish':
  pdf.text(x=17, y=start+y+10, txt='^')

# Write to file
pdf.output(file_name)
print(' ... done.')
