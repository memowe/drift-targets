generate_pdf:
	@mkdir -p output/pdf
	find data -name '*.data' | xargs python3 generate_pdf.py

generate_index:
	@mkdir -p output
	find data -name '*.data' | xargs python3 generate_index_md.py
	pandoc -t html -so output/index.html output/index.md
	rm output/index.md

init:
	pip3 install -r requirements.txt
