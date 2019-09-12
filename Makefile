generate_pdf:
	find data -name '*.dat' | xargs python3 generate_pdf.py

init:
	pip3 install -r requirements.txt
