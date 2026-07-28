# How to contribute

If you have any suggestion or want your project to be included in the list, you can contribute in the following ways.

## Open an issue

To suggest a new program, check the existence of the program in the list.
If it is not present, you can open an issue including the following items:

- `name`: Name of the program
- `homepage`: URL of the homepage (if it exists)
- `git`: URL of a clonable git repository (if it exists)
- `description`: Text with the description of the program

At least one of the two items `homepage` and `git` must be present.

## Pull request on `data/apps.csv`

The peculiarity of this repository is that the source of information is structured into CSV files with a simple structure.
See the `data/` directory.

If you want to contribute using a pull request, add the new entry to `data/apps.csv`.
In the CSV file, the `git` field refers to a **clonable git URL**.

Please make changes **to the CSV file only**, **not to the README file**.
I will review the request and, upon acceptance, I will take care of generating the README and updating the list.

# Generation of the README file

If necessary, the `README` file can be (re-)generated from the CSV files.
To build `README.md` run:

```
make
```

`python3` is required for building. And `make`, of course. :-)

