# Makefile

.PHONY: cli api clean mock

# Run CLI with proper PYTHONPATH
cli:
	@echo "Running CLI..."
	PYTHONPATH=. python cli/main.py

# Start Flask API with proper PYTHONPATH
api:
	@echo "Starting API on http://localhost:5000..."
	PYTHONPATH=. python api/app.py

# Run CLI with a mock prompt from file
mock:
	@echo "Running mock prompt from examples/prompt1.txt..."
	PYTHONPATH=. python cli/main.py < examples/prompt1.txt

# Clean generated files
clean:
	@rm -f network.yaml
	@echo "✅ Cleaned network.yaml"
