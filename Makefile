NAME = shellAI
SOURCE = $(NAME).py
DIST_DIR = dist
REQUIREMENTS = requirements.txt

.PHONY: all install build clean

all: install build

install:
	pip install --upgrade pip
	pip install -r $(REQUIREMENTS)

build: $(DIST_DIR)/$(NAME)

$(DIST_DIR)/$(NAME): $(SOURCE)
	pyinstaller $(SOURCE) --name $(NAME) --console --onefile
	rm -rf build
	mv $(NAME).spec $(DIST_DIR)/

clean:
	rm -rf build $(DIST_DIR) __pycache__ *.spec
