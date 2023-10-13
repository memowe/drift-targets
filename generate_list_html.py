import sys

print(
"""<!doctype html>
<html lang="en"><head><title>Drift target list</title></head><body>
<ul>""")
for target in sys.argv[1:]:
  print(f'  <li><a href="pdf/{target}.pdf">{target}</a></li>')
print(
"""</ul>
</body></html>""")
