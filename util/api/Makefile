IMAGE := api
PORT := 8000

build:
	docker build -t $(IMAGE) .

run: build
	docker run -d -p $(PORT):$(PORT) --name $(IMAGE) $(IMAGE)

clean:
	docker rm $(IMAGE)

stop:
	docker stop $(IMAGE) && docker rm $(IMAGE)

seed:
	cd db-init && uv run python seed.py

test:
	curl http://localhost:$(PORT)/customers
	curl http://localhost:$(PORT)/products/1

unit-test:
	uv run pytest tests/ -v

deploy: build
	kubectl apply -f k8s/

redeploy: build
	kubectl rollout restart deployment/jetson-api

undeploy:
	kubectl delete -f k8s/

k8s-status:
	kubectl get pods -l app=jetson-api
	kubectl get svc jetson-api

k8s-logs:
	kubectl logs -f deployment/jetson-api

k8s-test:
	curl http://localhost:30080/customers
	curl http://localhost:30080/products/1
