.PHONY: help
help: ## Show this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

get-model:
	@model="llama-2-7b.Q4_K_M.gguf"; \
	if [ ! -f "./models/$$model" ]; then \
		echo "Downloading model.."; \
 		curl -L -w '%{url_effective}' -o "./models/$$model" -L "https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/$$model"; \
	else \
		echo "Model already exists"; \
	fi

dev:
	cd edge-ui && npm run dev &
	cd edge-api && flask --app server run

build:
	docker build -t north.azurecr.io/discopilot .

push:
	docker push north.azurecr.io/discopilot







