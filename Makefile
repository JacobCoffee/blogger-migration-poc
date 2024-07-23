install:
	@rye sync -f
	@echo "Ready to go..."

fmt:
	@ruff format
	@ruff check --fix

migrate:
	@if [ ! -f $(file) ]; then echo "File not found: $(file)"; exit 1; fi
	@python tools/migrate.py
	@bash tools/date.sh
	@echo "Migration complete!"

docs-serve:
	@echo "=> Serving documentation"
	$(PDM_RUN_BIN) sphinx-autobuild docs docs/_build/ -j auto --watch docs --port 8000
