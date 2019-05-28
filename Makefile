build:
	docker build -t ansyrm/overviewer:latest -f Dockerfile .
	docker tag "ansyrm/overviewer:latest" "ansyrm/overviewer:${TRAVIS_COMMIT}"
	docker tag "ansyrm/overviewer:latest" "ansyrm/overviewer:$(shell date +%Y-%m)"

test-dive:
	docker build -t ansyrm/overviewer:latest -f Dockerfile .
	docker run --rm -it \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-e CI=true \
		wagoodman/dive:latest "ansyrm/overviewer:latest"
push:
	@make build
	echo "${DOCKER_HUB_PASSWORD}" | docker login -u "${DOCKER_HUB_USERNAME}" --password-stdin
	docker push "ansyrm/overviewer:latest"
	docker push "ansyrm/overviewer:${TRAVIS_COMMIT}"
	docker push "ansyrm/overviewer:$(shell date +%Y-%m)"
