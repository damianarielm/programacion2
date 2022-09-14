PANDOC=pandoc
INCLUDE=./include.sh
PANDOCFLAGS=-s -t beamer -V aspectratio=169 -V theme=Warsaw
SLIDES=intro.pdf unidad0.pdf unidad0-repaso.pdf unidad1-recursion.pdf unidad1-1.pdf unidad1-2.pdf
MAKEFLAGS+=j

all: $(SLIDES)

%.pdf : %.md
	@mkdir -p output
	$(INCLUDE) $< | $(PANDOC) $(PANDOCFLAGS) -o output/$@

.PHONY: clean
clean:
	rm -rf output/*.pdf
