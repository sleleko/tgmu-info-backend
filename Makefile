build:
	docker build -t tgmu:infoscreen-backend-v0.2 .
start:
	docker run -d --name tgmu-infoscreen-backend -v /srv/db/tgmu-infoscreen-static:/app/static -p 8181:80 tgmu:infoscreen-backend-v0.2
test:
	docker run -it --rm tgmu:infoscreen-backend-v0.1 -C /bin/sh
