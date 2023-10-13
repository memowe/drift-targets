PHOTOS_DIR=photos
OUTPUT_DIR=output
VENV=venv
REQUIREMENTS=requirements.txt
PYTHON=$(VENV)/bin/python
TARGETS:=$(patsubst $(PHOTOS_DIR)/%.png,%, $(wildcard $(PHOTOS_DIR)/*.png))
TARGET_DIR=$(OUTPUT_DIR)/pdf
TARGET_PDFS:=$(patsubst %,$(TARGET_DIR)/%.pdf, $(TARGETS))

.PHONY: all
all: clean $(OUTPUT_DIR)/index.html

.PHONY: prepare_venv
prepare_venv: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || python3 -m venv $(VENV)
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -r requirements.txt
	touch $@

$(OUTPUT_DIR)/index.html: prepare_venv $(TARGET_PDFS)
	@mkdir -p $(@D)
	$(PYTHON) generate_list_html.py $(TARGETS) > $@

$(TARGET_DIR)/%.pdf: prepare_venv config.ini
	@mkdir -p $(@D)
	$(PYTHON) generate_pdf.py $*

.PHONY: clean
clean:
	@find $(OUTPUT_DIR) \
					-not -name $(OUTPUT_DIR) \
		-and 	-not -name .gitkeep \
		-and 	-not -wholename $(OUTPUT_DIR)/pdf \
		-and 	-type f \
		-delete

.PHONY: realclean
realclean: clean
	-@rm -r $(VENV)
