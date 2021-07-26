# Example of usage
# $ make RECEPTOR_NODE_COUNT=2

create-receptor-mesh: update-config
	docker-compose down
	docker-compose build
	docker-compose up

update-config:
	mkdir -p ./configs
	rm -f ./configs/*
	python config.py

# TODO Change this to some Red Hat artifacts repo
# (ask Elijah about it)
./bin/receptor:
	mkdir -p ./bin
	curl -Ls --output ./bin/receptor https://www.dropbox.com/s/wv2bx00lxmzqjlr/receptor?dl=1
	chmod +x ./bin/receptor

clean:
	rm -rf ./bin/
	rm -rf ./configs/
	rm -f docker-compose.yaml
