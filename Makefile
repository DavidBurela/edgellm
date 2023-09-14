.PHONY: help
help: ## Show this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


dev:
	cd edge-ui && npm run dev &
	cd edge-api && flask --app server run

build:
	docker-compose build
	./kompose convert -f docker-compose.yml -o k8s.yml

push:
	docker-compose push

deploy: 
	kubectl create secret docker-registry north-registry --docker-server=north.azurecr.io  --docker-username=north --docker-password=
	kubectl apply -f k8s.yml







	