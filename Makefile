.PHONY: help build dev css-build css-watch clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: css-build ## Build the complete site for production
	hugo --gc --minify

dev: ## Start development server with CSS watching
	@echo "Starting development mode..."
	@./tailwindcss-linux-x64 -i ./themes/craftytheme/assets/css/main.css -o ./themes/craftytheme/static/css/main.css --watch &
	@hugo server -D --disableFastRender

css-build: ## Build Tailwind CSS once
	./tailwindcss-linux-x64 -i ./themes/craftytheme/assets/css/main.css -o ./themes/craftytheme/static/css/main.css --minify

css-watch: ## Watch and rebuild Tailwind CSS on changes
	./tailwindcss-linux-x64 -i ./themes/craftytheme/assets/css/main.css -o ./themes/craftytheme/static/css/main.css --watch

clean: ## Clean build artifacts
	rm -rf public/
	rm -f ./themes/craftytheme/static/css/main.css

server: ## Start Hugo server only
	hugo server -D

install-deps: ## Download Tailwind CSS CLI if not present
	@if [ ! -f tailwindcss-linux-x64 ]; then \
		echo "Downloading Tailwind CSS CLI..."; \
		curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64; \
		chmod +x tailwindcss-linux-x64; \
		echo "Tailwind CSS CLI installed!"; \
	else \
		echo "Tailwind CSS CLI already installed."; \
	fi
