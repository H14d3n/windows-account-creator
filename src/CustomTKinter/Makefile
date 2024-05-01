# Makefile for building the application with PyInstaller

# Variables
SCRIPT_NAME = "[CustomTKinter] Windows user creation"
ICON_PATH = ./image-removebg-preview.ico

# PyInstaller options
PYINSTALLER_OPTIONS = --onefile --windowed --icon=$(ICON_PATH) --add-data "$(ICON_PATH);." --uac-admin

# Default target
all: build

# Build target
build: check_pyinstaller
	@pyinstaller $(PYINSTALLER_OPTIONS) $(SCRIPT_NAME)

# Check if PyInstaller is installed, install if not
check_pyinstaller:
	@if ! command -v pyinstaller &> /dev/null; then \
		echo "PyInstaller not found. Please install PyInstaller before proceeding."; \
		exit 1; \
	fi

# Clean target
clean:
	@rm -rf dist build $(SCRIPT_NAME).spec

# Help target
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  all       Build the application"
	@echo "  build     Build the application"
	@echo "  clean     Clean up build artifacts"
	@echo "  help      Display this help message"
