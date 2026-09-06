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

unit-test:
	uv run pytest tests/ -v
