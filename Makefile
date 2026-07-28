README.md: data/header.md data/cli-apps.md
	cat data/header.md data/cli-apps.md > README.md

data/cli-apps.md: cli2md.py data/apps.csv data/categories.csv data/resources.csv data/articles.csv data/groups.json
	python3 cli2md.py > data/cli-apps.md
