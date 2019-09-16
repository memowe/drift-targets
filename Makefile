generate_pdf:
	@mkdir -p output/pdf
	python3 generate_pdf.py

generate_index:
	@mkdir -p output
	python3 generate_index_md.py
	pandoc -t html5 -so output/index.html output/index.md
	rm output/index.md

init:
	pip3 install -r requirements.txt
