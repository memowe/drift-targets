generate_pdf:
	mkdir -p output/pdf
	find data -name '*.data' | xargs python3 generate_pdf.py

init:
	pip3 install -r requirements.txt
