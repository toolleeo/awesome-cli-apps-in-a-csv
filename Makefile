README.md: data/header.md data/footer.md data/cli-apps.md
	cat data/header.md data/cli-apps.md data/footer.md > README.md

data/cli-apps.md: cli2md.py data/apps.csv data/categories.csv data/resources.csv data/articles.csv
	python3 cli2md.py > data/cli-apps.md
