# The largest Awesome List of CLI/TUI programs

This repository contains a list of CLI/TUI apps with links and a short description.

To the best of my knowledge, this is the largest collection of CLI/TUI tools available in the form of awesome list.

If you are looking for additional information, you may like [CLIpedia](https://robot.unipv.it/clipedia/), a growing blog about CLI/TUI programs.

# Data organization and building of the list

The peculiarity of this repository is that the source of information is structured into CSV files with a simple structure.
See the `data/` directory.

This `README` file is generated from the CSV files.
To build `README.md` run:

```
make
```

`python3` is required for building. And `make`, of course. :-)

# How to contribute

If you have any suggestion or want your project included in the list, you can either open a pull request or send me an email with the necessary information.

If you want to contribute through a pull request, make sure to add new entries to the correct CSV file under the `data/` directory.
Please commit the CSV file only, not the README.
I will review the request and, upon acceptance, I will take care of generating the README and updating the list.

If you prefer an email, contact me at `toolleeo@gmail.com`.

# Summary

To date, **924** apps/tools covered, organized in **45** categories.

# Index

[Backup](#backup) (9) | [Calculators](#calc) (9) | [Chat and instant messaging](#chat) (13) | [Commands cheatsheet and snippets](#cheatsheet) (16) | [Conversion](#conversion) (8) | [Data management](#data-management) (38) | [Data transfer](#transfer) (32) | [Directory changers](#cd) (13) | [Disk usage analyzers](#disk-analyzer) (12) | [Editors](#editors) (23) | [Email](#email) (12) | [File and file system handling](#file-handling) (46) | [File manager](#file-manager) (17) | [File renamers](#file-renamer) (11) | [File systems](#file-system) (4) | [Font management](#font) (2) | [Funny tools](#funny) (26) | [Games](#games) (39) | [Git and accessories](#git) (34) | [Graphics](#graphics) (26) | [Multimedia](#multimedia) (8) | [Networking](#networking) (23) | [Note taking](#note-taking) (18) | [Office tools](#office) (17) | [Organizers and calendars](#organizers) (17) | [Online search and resources](#online) (10) | [Password managers](#password-manager) (14) | [Productivity](#productivity) (39) | [Programming](#programming) (35) | [Science](#science) (11) | [Security and encryption](#security) (20) | [Shells](#shells) (9) | [Sound and music](#music) (26) | [System monitoring](#monitor) (33) | [System tools](#system) (33) | [Terminals](#terminal) (9) | [Text processing](#text-processing) (48) | [Text search](#text-search) (10) | [Todo managers](#todo-manager) (21) | [Torrent](#torrent) (7) | [Utilities](#utility) (46) | [Versioning](#versioning) (6) | [Viewers](#viewers) (36) | [Web browser](#browser) (16) | [Web development](#webdev) (22)

Some links to [related resources](#resources).

## <a name="backup"></a>Backup

* [borg](https://www.borgbackup.org/) - Encrypted backups with a clean and simple interface
* [bupstash](https://github.com/andrewchambers/bupstash) - Easy and efficient encrypted backups.
* [duplicity](http://duplicity.nongnu.org/) - Creates GPG encrypted, compressed backups; client-side encryption allows to upload the backup onto untrusted servers.
* [Duply](http://duply.net/) - Simplifies the use of [duplicity](http://duplicity.nongnu.org/) by keeping clean configuration files to automate the backup.  
* [paperbackup](https://github.com/intra2net/paperbackup) - Create a pdf with barcodes to backup text files on paper.
* [shallow-backup](https://github.com/alichtman/shallow-backup) - Git integrated backup tool.
* [thread-safe](https://github.com/dkaslovsky/thread-safe) - Keep your favorite Twitter threads safe with a local copy.
* [Zaloha.sh](https://github.com/Fitus/Zaloha.sh) - Shellscript for synchronization of files and directories.
* [zbackup](http://zbackup.org/) - A globally-deduplicating backup tool, based on the ideas found in rsync.

## <a name="calc"></a>Calculators

Calculators for numbers, dates, etc..

* [bcal](https://github.com/jarun/bcal) - Byte CALculator - A REPL CLI utility for storage expression evaluation, SI/IEC conversion, byte address calculation, base conversion and LBA/CHS calculation.
* [Bitwise](https://github.com/mellowcandle/bitwise) - Base conversion and bit manipulator in ncurses.
* [cash-cli](https://github.com/xxczaki/cash-cli) - Convert Currency Rates.
* [kalk](https://github.com/PaddiM8/kalker) - Command line calculator that supports math-like syntax with user-defined variables, functions, derivation, integration, and complex numbers.
* [mdlt](https://github.com/metadelta/mdlt) - A lightweight command line tool that lets you perform arithmetic and symbolic math operations right from the terminal.
* [Nota](https://kary.us/nota/) - Terminal calculator with rich notation.
* [pdd](https://github.com/jarun/pdd) - Tiny date, time diff calculator.
* [Programmer calculator](https://github.com/alt-romes/programmer-calculator) - Terminal calculator made for programmers working with multiple number representations, sizes, and overall close to the bits.
* [Qalculate](https://qalculate.github.io/) - Multi-purpose calculator with customizable functions, units, arbitrary precision, plotting (it includes a GUI).

## <a name="chat"></a>Chat and instant messaging

* [Discordo](https://github.com/ayn2op/discordo) - A lightweight, secure, and feature-rich Discord terminal client.
* [finch](http://www.pidgin.im/) - IM program supporting many protocols, including Yahoo!, AIM, IRC, or WLM; comes with the `Pidgin` project.
* [irssi](http://www.irssi.org) - The most popular IRC client for the command-line; a flexible program, with many options and supporting many protocols.
* [kirc](http://kirc.io/) - A tiny IRC client written in POSIX C99.
* [matterhorn](https://github.com/matterhorn-chat/matterhorn) - A terminal client for the Mattermost chat system.
* [PingMe](https://github.com/kha7iq/pingme) - Sends messages or alerts to multiple messaging platforms & email, including Slack, Telegram, Mattermost, WeChat and others.
* [RainbowStream](http://www.rainbowstream.org/) - Twitter client for the terminal
* [ssh-chat](https://github.com/shazow/ssh-chat) - Custom SSH server written in Go. Instead of a shell, you get a chat prompt.
* [tiny](https://github.com/osa1/tiny) - tiny is an IRC client written in Rust.
* [ttchat](https://github.com/atye/ttchat) - Twitch chats in the terminal.
* [tuir](https://gitlab.com/ajak/tuir) - Reddit TUI.
* [tweets](https://github.com/diracdeltas/tweets) - Decentralized alternative to twitter that uses git as support tool to manage the tweets.
* [WeeChat](http://weechat.org/) - A "fast, light and extensible chat client".

## <a name="cheatsheet"></a>Commands cheatsheet and snippets

Tools to manage often used commands, code snippets, cheatsheets and alternative manpages.

* [AI](https://github.com/nitefood/ai-bash-gpt) - A commandline ChatGPT client in BASH with conversation/completion support.
* [aido-cli](https://github.com/kris7ian/aido-cli) - Looks another interface to online GPT models to execute command through natural language. Very poor documentation and readme, though.
* [Commandpilot](https://github.com/barthr/commandpilot) - An assistant which uses ChatGPT to aid in constructing commands for bash.
* [docfd](https://github.com/darrenldl/docfd) - TUI fuzzy document finder that looks for documentation files in markdown and txt format in the directory tree.
* [eg](https://github.com/srsudar/eg) - Useful examples at the command line.
* [ehh](https://github.com/lennardv2/ehh) - Command-line tool for remembering linux/terminal commands.
* [gpt-do](https://github.com/yasyf/gpt-do) - This is a handy-dandy CLI for when you don't know wtf to do; instead of furiously grepping through man pages, simply use do (or ddo if on bash/zsh), and have GPT-3 do all the magic for you.
* [kmdr-cli](https://github.com/ediardo/kmdr-cli) - The CLI tool for explaining commands from your terminal.
* [MUC](https://github.com/nate-sys/muc) - Visualize your most used commands.
* [Nap](https://github.com/maaslalani/nap) - Code snippet manager that allows to create and access new snippets quickly with the command-line interface or browse, manage, and organize them with the text-user interface.
* [navi](https://github.com/denisidoro/navi) - An interactive cheatsheet tool for the command-line.
* [tealdeer](https://github.com/dbrgn/tealdeer) - Very fast implementation of tldr in Rust.
* [The Fuck](https://github.com/nvbn/thefuck) - Magnificent app which corrects your previous console command (although I would be extra-cautious at making a program to automatically infer what I was intending).
* [tldr](https://tldr.sh/) - Client for tldr pages, a community effort to simplify the beloved man pages with practical examples.
* [topalias](https://github.com/meteoritt/topalias) - Linux alias generator from bash/zsh command history with statistics, written on Python.
* [Wat](https://github.com/dthree/wat) - Instant, central, community-built docs.

## <a name="conversion"></a>Conversion

File format converters.

* [BaFi](https://mmalcek.github.io/bafi/) - Universal JSON, BSON, YAML, CSV, XML translator to ANY format using templates.
* [catdoc](http://www.wagner.pp.ru/~vitus/software/catdoc/) - Command line converter from Microsoft Word to plain text
* [mdBook](https://github.com/rust-lang/mdBook) - Create book from markdown files.
* [NestedTextTo](https://github.com/AndydeCleyre/nestedtextto) - CLI to convert between NestedText and JSON, YAML, or TOML.
* [Pandoc](http://pandoc.org/) - Universal document file converter; handles input output from/to a number of formats: HTML, PDF, LaTeX, docx, odt, AsciiDoc, Markdown, Textile, just to mention a few; the quality of conversion strongly depends on the combination of input/output formats.
* [simtex](https://github.com/simtex-dev/engine) - simtex (simplified LaTeX) allows you to convert your markdown or text lectures into LaTeX file with one command, configured with simple .json file.
* [Vertopal-CLI](https://github.com/vertopal/vertopal-cli) - Vertopal-CLI is a small, yet powerful utility for converting digital files to a variety of file formats using Vertopal public API.
* [xls2csv](http://www.wagner.pp.ru/~vitus/software/catdoc/) - Command line converter from Excel to CSV file format.  

## <a name="data-management"></a>Data management

* [crudini](https://github.com/pixelb/crudini) - A utility for manipulating ini files.
* [csvkit](https://github.com/wireservice/csvkit) - A suite of command-line tools for converting to and working with CSV, the king of tabular file formats.
* [csvq](https://github.com/mithrandie/csvq) - SQL-like query language for csv.
* [csvtk](https://bioinf.shenwei.me/csvtk/) - A cross-platform, efficient and practical CSV/TSV toolkit written in Go.
* [dasel](https://github.com/TomWright/dasel) - Allows you to query and modify data structures using selector strings.
* [datadash](https://github.com/keithknott26/datadash) - Visualize and graph data in the terminal.
* [datasetGPT](https://github.com/radi-cho/datasetGPT) - A command-line interface and a Python library for inferencing Large Language Models to generate textual datasets.
* [Dolt](https://github.com/dolthub/dolt) - Dolt is Git for Data! Dolt is a SQL database that you can fork, clone, branch, merge, push and pull just like a git repository.
* [GNU Recutils](https://www.gnu.org/software/recutils/manual/) - Set of tools and libraries to access human-editable, text-based databases called recfiles.
* [gnuplot](https://www.explainshell.com/explain/1/gnuplot) - Generate two and three dimensional plots of data.
* [gojq](https://github.com/itchyny/gojq) - Pure Go implementation of jq.
* [Graphtage](https://github.com/trailofbits/graphtage) - Graphtage is a commandline utility and underlying library for semantically comparing and merging tree-like structures, such as JSON, XML, HTML, YAML, plist, and CSS files.
* [GROQ](https://github.com/sanity-io/groq-cli) - The CLI tool consumes both JSON and NDJSON documents. You can pass in data from a local file, or from piping to standard input.
* [IRedis](https://github.com/laixintao/iredis) - Interactive Redis: A Cli for Redis with AutoCompletion and Syntax Highlighting.
* [jp](https://github.com/therealklanni/jp) - A tiny commandline tool for parsing JSON from any source.
* [jq](https://stedolan.github.io/jq/) - (JSON Query?) is sed-like processor for JSON data; can be used to process JSON files and data streams and perform operations such as those allowed by `cat`, `sed`, `grep` and `awk` on regular text files.
* [jqp](https://github.com/noahgorstein/jqp) - A TUI playground for exploring jq.
* [jtc](https://github.com/ldn-softdev/jtc) - JSON manipulation and transformation.
* [lowcharts](https://github.com/juan-leon/lowcharts) - lowcharts is meant to be used in those scenarios where we have numerical data in text files that we want to display in the terminal to do a basic analysis.
* [Miller](https://github.com/johnkerl/miller) - Miller is like awk, sed, cut, join, and sort for data formats such as CSV, TSV, JSON, JSON Lines, and positionally-indexed.
* [mycli](https://github.com/dbcli/mycli) - A command line client for MySQL that can do auto-completion and syntax highlighting.
* [osmf](https://github.com/codesoap/osmar) - OpenStreetMap find - A simple command line tool to explore OSM data.
* [pgcli](https://github.com/dbcli/pgcli) - Postgres CLI with autocompletion and syntax highlighting.
* [q](http://harelba.github.io/q/) - Executes SQL-like queries on CSVs/TSVs tabular data files; each tabular file is treated as a database table; support to all SQL constructs (`WHERE`, `GROUP BY`, `JOIN`).
* [ramda-cli](https://github.com/raine/ramda-cli) - A tool for processing data with functional pipelines.
* [Redis Viewer](https://github.com/SaltFishPr/redis-viewer) - A tool to view redis data in terminal.
* [ROAPI](https://github.com/roapi/roapi) - ROAPI automatically spins up read-only APIs for static datasets without requiring you to write a single line of code.
* [Soul](https://github.com/thevahidal/soul) - A SQLite REST and realtime server.
* [sq](https://github.com/neilotoole/sq) - Command line tool that provides jq-style access to structured data sources such as SQL databases, or document formats like CSV or Excel.
* [termdbms](https://github.com/mathaou/termdbms) - A TUI for viewing and editing databases, written in pure Go.
* [TSV Utilities](https://github.com/eBay/tsv-utils) - Command line tools for large, tabular data files.
* [underscore-cli](https://github.com/ddopson/underscore-cli) - Command-line utility-belt for hacking JSON and Javascript.
* [usql](https://github.com/xo/usql) - Universal command-line interface for PostgreSQL, MySQL, Oracle Database, SQLite3, Microsoft SQL Server, and others, including NoSQL and non-relational databases.
* [VisiData](https://www.visidata.org/) - Interactive multitool for tabular data. It combines the clarity of a spreadsheet, the efficiency of the terminal, and the power of Python, into a lightweight utility which can handle millions of rows with ease.
* [WOPR](https://github.com/yaronn/wopr) - A simple markup language for creating rich terminal reports, presentations and infographic.
* [xsv](https://www.johndcook.com/blog/2019/12/31/sql-join-csv-files/) - Doing a SQL join with CSV files.
* [yq](https://github.com/mikefarah/yq) - Portable command-line YAML processor.
* [zq](https://zed.brimdata.io/docs/commands/zq/) - Processor for JSON data with stateful operators and a syntax that is more consistent w.r.t. jq (as claimed by the authors).

## <a name="transfer"></a>Data transfer

* [aria2](https://github.com/aria2/aria2) - Lightweight and easy-to-use download utility; it supports HTTP/HTTPS, FTP, SFTP, BitTorrent, Metalink and multiple sources; cross-platform.
* [Clipsync](https://github.com/marcopaganini/clipsync) - Share your clipboard across multiple machines using an MQTT service.
* [croc](https://github.com/schollz/croc) - Easily and securely send things from one computer to another.
* [curl](https://curl.haxx.se/) - A tool and library for transferring data with URL syntax
* [feuille](https://basedwa.re/tmtt/feuille.git) - A fast, dead-simple socket-based pastebin.
* [ffsend](https://github.com/timvisee/ffsend) - Easily and securely share files from the command line. A fully featured Firefox Send client.
* [Jitter](https://github.com/kevspau/jitter) - A repository-oriented binary manager for Linux, Jitter searches through online repository (currently only on GitHub) for releases with .tar.gz, .tgz, .zip or .AppImage assets.
* [lftp](https://lftp.yar.ru/) - "Sophisticated ftp/http client, and a file transfer program supporting a number of network protocols"; support for bookmarks and mirroring features.
* [Magic Wormhole](https://github.com/magic-wormhole/magic-wormhole) - The program allows transfer arbitrary-sized files and directories (or short pieces of text) from one computer to another The two endpoints are identified by using identical human-readable codes.  
* [Nextcloud share URL downloader](https://github.com/aertslab/nextcloud_share_url_downloader) - Download files from and list content of NextCloud (password protected) share directly from the command line without needing a webbrowser.
* [OnionShare](https://onionshare.org/) - "An open source tool that lets you securely and anonymously share a file of any size." 
* [pbgopy](https://github.com/nakabonne/pbgopy) - Copy and paste between devices.
* [pbproxy](https://github.com/nikvdp/pbproxy) - Send your clipboard anywhere you can ssh to.
* [portal](https://github.com/SpatiumPortae/portal) - A quick and easy command-line file transfer utility from any computer to another.
* [qr-filetransfer](https://github.com/sdushantha/qr-filetransfer) - Transfer files over WiFi between your computer and your smartphone from the terminal.
* [qrcp](https://www.linuxuprising.com/2020/07/qrcp-transfer-files-between-desktop-and.html) - Transfer Files Between Desktop And Mobile Devices Over Wi-Fi By Scanning A QR Code.
* [rclone](https://rclone.org/) - Rclone manages file synchronization on cloud storage.
* [rclone-tui](https://github.com/darkhz/rclone-tui) - Cross-platform manager for rclone, which aims to be on-par with the web GUI.
* [rsync](https://download.samba.org/pub/rsync/rsync.html) - Mirror directories across networked machines
* [sharing](https://github.com/parvardegr/sharing) - Sharing is a command-line tool to share directories and files from the CLI to iOS and Android devices without the need of an extra client app.
* [shcopy](https://github.com/aymanbagabas/shcopy) - Copy text to your system clipboard locally and remotely using ANSI OSC52 sequence.
* [sitecopy](http://www.manyfish.co.uk/sitecopy/) - Synchronizes a local copy of a website with a remote copy on a server
* [stftp](http://stftp.sourceforge.net/) - (simple terminal FTP) aims to be a "easy-to-use and unbloated client for the UNIX (and UNIX-like) console".
* [tran](https://github.com/abdfnx/tran) - Securely transfer and send anything between computers with TUI.
* [Unison](https://www.cis.upenn.edu/~bcpierce/unison/) - File synchronizer. It allows two replicas of a collection of files and directories to be stored on different hosts (or different disks on the same host), modified separately, and then brought up to date by propagating the changes in each replica to the other.
* [Woof](http://www.home.unix-ag.org/simon/woof.html) - (Web Offer One File) sets up an HTTP webserver to serve files from a given local directory
* [xh](https://github.com/ducaale/xh) - xh is a friendly and fast tool for sending HTTP requests. It reimplements as much as possible of HTTPie's excellent design.
* [Yark](https://github.com/Owez/yark) - YouTube archiving made simple.
* [youtube-dl](https://github.com/ytdl-org/youtube-dl/) - Downloads videos from [YouTube](https://www.youtube.com/) and some other sites
* [yt-splitter](https://github.com/redsolver/yt-splitter) - Downloads and splits audio tracks from a YouTube video according to the chapters/tracks. Useful for compilations or full album uploads.
* [ytfzf](https://github.com/pystardust/ytfzf) - A POSIX script that helps you find Youtube videos (without API) and opens/downloads them using mpv/youtube-dl.
* [ytmdl](https://github.com/deepjyoti30/ytmdl) - Get songs from Youtube in mp3 format.

## <a name="cd"></a>Directory changers

Tools for improving the efficiency of directory traversal.

* [autojump](https://github.com/wting/autojump) - A cd command that learns - easily navigate directories from the command line.
* [broot](https://dystroy.org/broot/) - A new way to navigate directory trees on linux, made in rust.
* [fasd](https://github.com/clvv/fasd) - A Commandline Tool That Offers Quick Access to Files and Directories. It offers quick access to files and directories for POSIX shells.  It is inspired by tools like autojump, z and v. Fasd keeps track of files and directories you have accessed, so that you can quickly reference them in the command line.
* [fastdiract](https://github.com/dp12/fastdiract) - Lightning-fast cd and command execution.
* [fz](https://github.com/changyuheng/fz.sh) - Fuzzy tab completion for z.
* [Jmp](https://github.com/gholmes829/Jmp) - Change directory with smart searching of the path specified through regex.
* [llama](https://github.com/antonmedv/llama) - Minimalistic file opener and directory changer focused on fuzzy searching the path.
* [pazi](https://github.com/euank/pazi) - Fast autojump helper.
* [pm](https://github.com/Angelmmiguel/pm) - The easy way to switch between your projects on ZSH. In short, another directory changer.
* [SmartCd](https://github.com/CodesOfRishi/smartcd) - A cd command with improved usability features, which can remember your recently visited directory paths and, search and directly traverse to sub-directories and as well as parent directories, all with Fuzzy searching.
* [z](https://github.com/rupa/z) - Directory changer based on aging and frecency.
* [z.lua](https://github.com/skywind3000/z.lua) - Directory changer that learns your habits.
* [zoxide](https://github.com/ajeetdsouza/zoxide) - A faster way to navigate your filesystem.

## <a name="disk-analyzer"></a>Disk usage analyzers

* [cdu](http://arsunik.free.fr/prog/cdu.html) - cdu (colored `du`) is a perl script that calls `du` and displays a pretty histogram with optional colors allowing to immediately see the directories which take most disk space.
* [dfc](https://github.com/rolinh/dfc) - Report file system space usage information with style.
* [diskonaut](https://github.com/imsnif/diskonaut) - Terminal disk space navigator that traverse the file-system with a TUI interface.
* [diskus](https://github.com/sharkdp/diskus) - Minimal, fast alternative to du -sh.
* [dua](https://github.com/Byron/dua-cli) - Disk Usage Analyzer. Learn about the usage of disk space of a given directory with parallel access to max out SSD exploration.
* [duf](https://github.com/muesli/duf) - Disk Usage/Free Utility.
* [Dust](https://github.com/bootandy/dust) - du + rust = dust. Like du but more intuitive.
* [dutree](https://github.com/nachoparker/dutree) - A tool to analyze file system usage written in Rust.
* [erdtree](https://github.com/solidiquis/erdtree) - A multi-threaded file-tree visualizer and disk usage analyzer.
* [gdu](https://github.com/dundee/gdu) - Pretty fast disk usage analyzer written in Go. Gdu is intended primarily for SSD disks where it can fully utilize parallel processing. However HDDs work as well, but the performance gain is not so huge.
* [ncdu](https://dev.yorhel.nl/ncdu) - "A disk usage analyzer with an ncurses interface.  It is designed to find space hogs on a remote server where you don't have an entire graphical setup available."
* [vizex](https://github.com/bexxmodd/vizex) - Visualize the disk space usage for every partition and media on the user's machine.

## <a name="editors"></a>Editors

Terminal text editors.

* [ash](https://github.com/akashnag/ash) - A simple and clean terminal-based text editor, that aims to be easy to use with modern key-bindings.
* [Diakonos](https://github.com/Pistos/diakonos) - A powerful editor with “standard" keybindings and several advanced features; written in Ruby.
* [Emacs](https://www.gnu.org/software/emacs/) - One of the godfathers of text editors
* [eon](https://github.com/tomas/eon) - A light, modern editor for your terminal that doesn't want to be vim.
* [Feather](https://www.feathereditor.com/) - The only terminal based text editor designed to work with BIG files.
* [Helix](https://github.com/helix-editor/helix) - A kakoune / neovim inspired editor, written in Rust. The editing model is very heavily based on kakoune.
* [jed](http://www.jedsoft.org/jed/index.html) - A text editor with a drop-down menu facility that make it especially user-friendly.  
* [joe](http://joe-editor.sourceforge.net/) - (Joe's Own Editor) is a compact text editor written in C
* [Kakoune](http://kakoune.org/) - Modal editor, faster as in less keystrokes, multiple selections, orthogonal design.
* [micro](https://github.com/zyedidia/micro) - A terminal-based text editor written in Go that aims to be easy to use and intuitive, while also taking advantage of the full capabilities of modern terminals.
* [nano](https://www.nano-editor.org/) - Easy to use, lightweigth text editor; no complex keybindings to remember.
* [neovim](https://neovim.io/) - A work in progress attempt to improve [vim](http://www.vim.org/), dropping older/unused OS compatibility, improving the codebase readability, modularity and maintainability; it has chances to become the next choice of vim users.
* [o](https://github.com/xyproto/orbiton) - Configuration-free text editor and IDE limited to VT100. Suitable for writing git commit messages, editing Markdown, config files, source code, viewing man pages and for quick edit-compile cycles when programming.
* [pickaxe](https://github.com/mdom/pickaxe) - The redmine wiki editor.
* [slap](https://github.com/slap-editor/slap) - Text editor inspired by [Sublime Text](https://www.sublimetext.com/) written in NodeJS
* [Tilde](https://os.ghalkes.nl/tilde/) - Tilde is a text editor that provides an intuitive interface for people accustomed to GUI environments, usual shortcuts for common operation, a traditional menu bar, etc.
* [vai](https://github.com/stefanoborini/vai) - A text editor similar to `vim` written in Python; many feature are nicely replicated, some are still missing; however, the advantage of this implementation is its simplicity, maintainability and extensibility, thanks to the Python implementation.
* [VE](http://www.inverary.net/ve/ve.html) - Lean, fast and feature rich text editor.
* [vim](http://www.vim.org/) - Historically one of the preferred text editors
* [vis](https://github.com/martanne/vis) - "a modern, legacy free, simple yet efficient vim-like editor", and more: "The intention is not to be bug for bug compatible with vim, instead a similar editing experience should be provided. The goal could thus be summarized as 80% of vim's features implemented in roughly 1% of the code"; the editor is scriptable in LUA and supports editing large files.
* [vy](https://github.com/vyapp/vy) - A vim-like in python made from scratch.
* [WordGrinder](https://cowlark.com/wordgrinder/) - From the website: "WordGrinder is a word processor for processing words. It is not WYSIWYG. It is not point and click. It is not a desktop publisher. It is not a text editor. It does not do fonts and it barely does styles. What it does do is words. It's designed for writing text. It gets out of your way and lets you type." 
* [zee](https://github.com/zee-editor/zee) - Zee is a modern editor for the terminal, in the spirit of Emacs. It is written in Rust and it is somewhat experimental.

## <a name="email"></a>Email

Email clients ([Mail User Agents](https://en.wikipedia.org/wiki/Email_client) - MUA), mail synchronization.

* [aerc](https://aerc-mail.org/) - A pretty good email client
* [alot](https://github.com/pazz/alot) - MUA written in Python using the [NotMuch](https://notmuchmail.org/) backend
* [alpine](http://www.washington.edu/alpine/) - Mail client which aims at being "fast, easy to use email client that is suitable for both the inexperienced email user as well as for the most demanding of power users".
* [Himalaya](https://github.com/soywod/himalaya) - Command-line interface for email management.
* [mbsync](http://isync.sourceforge.net/mbsync.html) - Mailboxes synchronization tool
* [meli](https://git.meli.delivery/meli/meli.git) - BSD/Linux terminal email client with support for multiple accounts and Maildir / mbox / notmuch / IMAP / JMAP.
* [Mutt](http://www.mutt.org/) - Mail client with tons of features, customization chances, support for IMAP, POP3, multiple storage formats.
* [NeoMutt](https://neomutt.org/) - Patched and up-to-dated mutt fork.
* [nmail](https://github.com/d99kris/nmail) - nmail is a console-based email client for Linux and macOS with a user interface similar to alpine / pine.
* [pymailgen](https://github.com/toolleeo/pymailgen) - Starting from the content of a CSV file and a template text file, pymailgen generates a list of emails to be sent out using a command-line SMTP client.
* [sup](http://sup-heliotrope.github.io/) - MUA written in Ruby; specifically developed for accounts with "a lot of emails"; nice thread-based presentation.
* [tmpmail](https://github.com/sdushantha/tmpmail) - A command line utility written in POSIX sh that allows you to create a temporary email address and receive emails to the temporary email address.

## <a name="file-handling"></a>File and file system handling

File managers, tagging, bookmarking.

* [alder](https://github.com/aweary/alder) - Directory tree visualizer.
* [backdown](https://github.com/Canop/backdown) - Safely and ergonomically remove duplicate files
* [Brash](https://github.com/zakariagatter/brash) - CLI Trash Manager in Pure Bash.
* [classifier](https://github.com/bhrigu123/classifier) - Organize files in your current directory, by classifying them into folders of music, pdfs, images, etc.
* [cv](https://github.com/Xfennec/progress) - (Coreutils Progress Viewer) "looks for coreutils basic commands (`cp`, `mv`, `dd`, `tar`, `gzip/gunzip`, `cat`, etc.) currently running on your system and displays the percentage of copied data. It can also show estimated time and throughput".
* [czkawka](https://qarmin.github.io/czkawka/) - Remove unnecessary files from your computer
* [detox](http://detox.sourceforge.net/) - A utility designed to easily clean up filenames
* [Dext](https://github.com/AfzGit/dext) - (Directories by Extensions) is a script that moves (or copies) files of the same extension into a folder.
* [Dirdiff](https://github.com/OCamlPro/dirdiff) - Efficiently compute the differences between two directories.
* [doppelganger](https://github.com/witchard/doppelganger) - Save and load your shell environment to create doppelganger shells!
* [dtrx](https://brettcsmith.org/2007/dtrx/) - (Do The Right eXtraction) aims at taking "all the hassle out of extracting archives"; allows to use one command to extract archives in different formats, recursive extraction (files into file) and extracts files into dedicated directories.
* [entr](https://github.com/eradman/entr) - Event Notify Test Runner - Run an arbitrary command when files change.
* [exa](https://the.exa.website/) - Replacement for 'ls' written in Rust, with colors and several additional "views".
* [FClones](https://github.com/pkolaczk/fclones) - Efficient Duplicate File Finder.
* [fd](https://github.com/sharkdp/fd) - A simple, fast and user-friendly alternative to find. Written in Rust.
* [ff](https://github.com/akymos/ff) - ff is a command-line tool to manage favorite folders, creating an alias, to be used via shell directly with the cd command.
* [file-type-cli](https://github.com/sindresorhus/file-type-cli) - Detect the file type of a file or stdin.
* [friendly-find](https://github.com/sjl/friendly-find) - Usable replacement for find.
* gcp - `gcp` (Goffi's cp) is an advanced file copier tool, heavily inspired from the traditional `cp` command utility, but with some additional features: Displays the copy progress indicator, with estimated time, current file speed; logs of all actions; resume of interrupted copy processes.
* [GoCatGo](https://github.com/vaaleyard/gocatgo) - GoCatGo is another pastebin tool with a super focus on transparency.
* [happyfinder](https://github.com/hugows/hf) - (another) Fuzzy file finder for the command line.
* [ictree](https://github.com/NikitaIvanovV/ictree) - Like tree but interactive.
* [inventory](https://github.com/mothdotmonster/inventory) - Move files like an old text adventure.
* [ll](https://github.com/antonmedv/ll) - ls with git status.
* [lsd](https://github.com/lsd-rs/lsd) - This project is a rewrite of GNU ls with lot of added features like colors, icons, tree-view, more formatting options etc. The project is heavily inspired by the super colorls project.
* [mat2](https://0xacab.org/jvoisin/mat2.git) - Metadata removal tool, supporting a wide range of commonly used file formats.
* [nat](https://github.com/willdoescode/nat) - Complete replacement for the `ls` command.
* [organize-cli](https://github.com/ManrajGrover/organize-cli) - Organize your files automatically.
* [PathPicker](https://facebook.github.io/PathPicker/) - A tool from Facebook that parses the output from a command and presents a UI to select files and directories
* [pcopy](https://github.com/binwiederhier/pcopy) - A temporary file host, nopaste and clipboard across machines. It can be used from the Web UI, via a CLI or without a client by using curl.
* [progress](https://github.com/Xfennec/progress) - A tool to monitor the progress of common Coreutils command-line tools (`cp`, `mv`, `dd`, `tar`, `rsync`, etc.); it uses an ncurses interface to display the percentage of data copied; it works by reading from system files and retrieving the necessary information for the estimation.
* [pycp](https://github.com/dmerejkowsky/pycp) - cp and mv with a progressbar.
* [RecoverPy](https://github.com/PabloLec/RecoverPy) - RecoverPy is a powerful tool that leverages your system capabilities to recover lost files. Unlike others, you can not only recover deleted files but also overwritten data.
* [rip](https://github.com/nivekuil/rip) - Safe and ergonomic alternative to rm.
* [rmlint](https://github.com/sahib/rmlint/) - A tool to recursively scan a directory tree looking for duplicate and broken files
* [rmw](https://remove-to-waste.info/) - (ReMove to Waste) is a trashcan/recycle bin utility for the command line. It can move and restore files to and from directories specified in a configuration file.
* [trash-cli](https://github.com/sindresorhus/trash-cli) - Move files and folders to the trash.
* [tre](https://github.com/dduan/tre) - `tree` command improved with git awareness, editor aliasing, and colors.
* [tree](http://mama.indstate.edu/users/ice/tree/) - "Recursive directory listing command that produces a depth indented listing of files".
* [TUI Archiver](https://www.nexus0.net/pub/sw/tuiarchiver/) - A TUI/CLI application to list / manage archives. Can be used stand-alone and has some features for integrating with TUI file managers
* [twf](https://github.com/wvanlint/twf) - Standalone tree view file explorer.
* [vidir](https://github.com/trapd00r/vidir) - vidir allows editing of the contents of a directory in a text editor.
* [watchexec](https://github.com/watchexec/watchexec) - Executes commands in response to file modifications.
* [wfh](https://github.com/kzys/wfh) - Continuously watches your local directories and rsync them against a remote host.
* [xcp](https://github.com/tarka/xcp) - Extended cp.
* [xplr](https://github.com/sayanarijit/xplr) - A hackable, minimal, fast TUI file explorer, stealing ideas from nnn and fzf.

## <a name="file-manager"></a>File manager

* [cfiles](https://github.com/mananapr/cfiles) - ncurses file manager written in C with vim like keybindings
* [clifm](https://github.com/leo-arch/clifm) - A CLI-based, shell-like, and non-curses terminal file manager written in C: simple, fast, extensible, and lightweight as hell.
* [felix](https://github.com/kyoheiu/felix) - TUI file manager with vim-like key mapping
* [fff](https://github.com/dylanaraps/fff) - Fast, simple file manager written in bash.
* [fman](https://github.com/nore-dev/fman) - TUI File Manager
* [goful](https://github.com/anmitsu/goful) - Goful is a CUI file manager written in Go.
* [hunter](https://github.com/rabite0/hunter) - Ranger-like file browser written in rust.
* [joshuto](https://github.com/kamiyaa/joshuto) - ranger-like terminal file manager
* [lf](https://github.com/gokcehan/lf) - lf (as in "list files") is a terminal file manager written in Go with a heavy inspiration from ranger file manager.
* [lfm](https://inigo.katxi.org/devel/lfm/) - (Last File Manager) is a file manager written in Python; it comes with lots of features, including 1-pane or 2-pane view, files filters and bookmarks, tree view, virtual file-systems to open compressed archives, search in files, customizable keybindings and themes.
* [Midnight Commander](http://www.midnight-commander.org/) - A visual file manager, full-screen text mode application that allows you to copy, move and delete files and whole directory trees and search for files; includes an internal viewer and editor.
* [ncursesFM](https://github.com/FedeDP/ncursesFM) - File manager written in C
* [nnn](https://github.com/jarun/nnn) - “The unorthodox terminal file manager" is a tiny, nearly 0-config and fast file manager supporting all the operations on files and directories.
* [ranger](https://ranger.github.io/) - Console file manager with vi key bindings
* [rnr](https://github.com/bugnano/rnr) - The RNR File Manager (RNR's Not Ranger) is a text based file manager that combines the best features of Midnight Commander and Ranger.
* [TUIFI Manager](https://github.com/GiorgosXou/TUIFIManager) - A cross-platform terminal-based termux-oriented file manager (and component), meant to be used with a Uni-Curses project or as is.
* [vifm](https://vifm.info/) - "ncurses based file manager with vi like keybindings/modes/options/commands/configuration, which also borrows some useful ideas from mutt" (cit.).

## <a name="file-renamer"></a>File renamers

* [F2](https://github.com/ayoisaiah/f2) - Cross-platform command-line tool for batch renaming files and directories quickly and safely.
* [massren](https://github.com/laurent22/massren) - Easily rename multiple files using your text editor.
* [mmv](https://github.com/itchyny/mmv) - Rename multiple files using your $EDITOR. The command name is named after multi-mv.
* [mmv-c](https://github.com/mcauley-penney/mmv-c) - Interactively rename files with your favorite editor.
* [moove](https://github.com/urin/moove) - Manipulate file names and locations using a text editor.
* [Musort](https://github.com/tdeerenberg/Musort) - Rename multiple audio/music files based on the ID3 tag at once.
* [nomino](https://github.com/yaa110/nomino) - Batch rename utility for developers.
* [rename](https://www.kernel.org/pub/linux/utils/util-linux/) - Included in `util-linux`, allows bulk rename of files with regex support.
* [rename-cli](https://github.com/jhotmann/node-rename-cli) - File renamer with TUI interface and preview.
* [renameutils](http://www.nongnu.org/renameutils/) - A set of programs to change file and directory names by editing them inplace
* [Tempren](https://github.com/idle-code/tempren) - A powerful file renaming utility that uses flexible template expressions to create new file paths and names.

## <a name="file-system"></a>File systems

* [ipfs-deploy](https://github.com/ipfs-shipyard/ipfs-deploy) - Zero-Config CLI to Deploy Static Websites to IPFS [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System).
* [sshfs](https://github.com/libfuse/sshfs) - Locally mount a remote file-system through SSH and access files and directory as they would be on the local machine.  
* [TMSU](http://tmsu.org/) - A tool for tagging files
* [wutag](https://github.com/vv9k/wutag) - CLI Tool for tagging and organizing files by tags.

## <a name="font"></a>Font management

* [FIGlet](http://www.figlet.org/) - Not exactly a font manager, but a nice program for making large letters out of ordinary text; an astonishing number of different fonts is available.
* [toilet](http://caca.zoy.org/wiki/toilet) - A program that tries to improve `FIGlet`; can load FIGlet fonts; supports Unicode input and output, colour fonts and output, and various output formats, including HTML, IRC and ANSI; uses `libcaca` to produce nice textual effects.

## <a name="funny"></a>Funny tools

Miscellaneous of tools that provide some funny/aesthetical functionality.

* [asciicquarium](http://www.robobunny.com/projects/asciiquarium/html/) - Enjoy the mysteries of the sea from the safety of your own terminal!
* [Binary Clock](https://github.com/tom-on-the-internet/binary-clock) - Displays a clock where numbers are represented with blue and gray dots with binary encoding.
* [cbonsai](https://gitlab.com/jallbrit/cbonsai) - A bonsai tree generator, written in C using ncurses. It intelligently creates, colors, and positions a bonsai tree.
* [cli-fireplace](https://github.com/dolsup/cli-fireplace) - Shows digital fireplace.
* [cmatrix](http://www.asty.org/cmatrix/) - ncurses program that display the scrolling lines found in the movie `The matrix`.
* [cowsay](https://en.wikipedia.org/wiki/Cowsay) - A program that generates a ASCII art of a cow with a bubble containing the specified message (I provide the Wikipedia link since at the moment the link to the author's homepage results to be unreachable).  
* [cowthink](https://en.wikipedia.org/wiki/Cowsay) - Same as `cowsay`, but uses a "think" bubble instead of a speech bubble.
* [ctree](https://github.com/gleich/ctree) - A Christmas tree right from your terminal.
* [Draw](https://github.com/maaslalani/draw) - draw is an simple drawing tool in the terminal. Hold your mouse down and move it across the screen to draw anything you want!
* [fortune](http://software.clapper.org/fortune/) - Generates random messages feched from a quotation database.  
* [gof-rs](https://github.com/omagdy7/gof-rs) - Game of life rendered in your terminal with over 500+ unique patterns to choose from.
* [kyun](https://github.com/file-acomplaint/kyun) - Kyun is a low productivity, low fidelity, low customizablity text editor that has its focus firm on user discomfort.
* [Limoji](https://github.com/GEROGIANNIS/Limoji) - Limoji is an open source tool that makes it easy to choose between hundreds of cool ASCII emoticons and share them with your friends.
* [LundukeHoliday](https://github.com/BryanLunduke/LundukeHoliday) - A simple Bash script that shows some animated, ASCII holiday decorations in your shell.
* [matrix-webcam](https://github.com/joschuck/matrix-webcam) - Take your video conference from within the matrix.
* [Maze Solver](https://github.com/Vlamonster/maze_solver_rust) - Generate, display and solve mazes in an animated way in the terminal.
* [No More Secrets](https://github.com/bartobri/no-more-secrets) - A command line tool that recreates the famous data decryption effect seen in the 1992 movie Sneakers.
* [pipes.sh](https://github.com/pipeseroni/pipes.sh) - Animated pipes terminal screensaver.
* [pokeget](https://github.com/talwat/pokeget) - A bash script you can use to display cool sprites of pokemon in your terminal.
* [ponysay](https://github.com/erkin/ponysay) - Pony rewrite of cowsay.
* [pyjokes](https://github.com/pyjokes/pyjokes) - One line jokes for programmers (jokes as a service).
* [Russhian Roulette](https://github.com/cyradotpink/russhian-roulette) - 1/6 chance of posting your SSH private key on pastebin (do you really want to try?).
* [sha256-animation](https://github.com/in3rsha/sha256-animation) - Animation of the SHA-256 hash function in your terminal.
* [Steam Locomotive](http://www.cyberciti.biz/tips/displays-animations-when-accidentally-you-type-sl-instead-of-ls.html) - A steam locomotive traverses the screen from right to left if `sl` is typed instead of `ls`.  
* [ternimal](https://github.com/p-e-w/ternimal) - Simulate a lifeform in the terminal.
* [yosay](https://github.com/yeoman/yosay) - Like cowsay, but for yeoman.

## <a name="games"></a>Games

* [Angband](https://rephial.org/) - Angband is a free, single-player dungeon exploration game.
* [anonymine](https://oskog97.com/projects/anonymine/) - Curses mode minesweeper without guessing and other original features.
* [bastet](http://fph.altervista.org/prog/bastet.html) - (Bastard Tetris) implements the classical Tetris but with a logic to generate the next block which maximizes the difficulty for the player.  
* [Cataclysm: Dark Days Ahead](https://cataclysmdda.org/) - Open source turn-based survival RPG development project.
* [chs](https://github.com/nickzuber/chs) - Play chess against the Stockfish engine in your terminal.
* [cli-chess](https://github.com/trevorbayless/cli-chess) - A highly customizable way to play chess in your terminal. Play online (via Lichess.org) and offline against the Fairy-Stockfish engine. All Lichess variants are supported.
* [clidle](https://github.com/ajeetdsouza/clidle) - Wordle, now over SSH.
* [crappybird-py](https://github.com/JonPizza/crappybird-py) - Flappy bird.
* [Dwarf fortress](http://www.bay12games.com/dwarves/) - A fantasy game using ASCII art graphical representation of the game environment
* [Flapioca](https://github.com/kbrgl/flapioca) - A Flappy Bird-inspired terminal game written in Go.
* [freesweep](http://www.upl.cs.wisc.edu/~hartmann/sweep/) - A Minesweeper clone for the terminal which allows you to configure settings such as table rows and columns up to 1024x1024!), percentage of bombs, colors and also has a highscores table.
* [gambit](https://github.com/maaslalani/gambit) - Chess board in your terminal.
* [GameShell](https://github.com/phyver/GameShell) - GameShell was devised as a tool to help university students to engage with a real shell, in a way that encourages learning while also having fun.
* [greed](http://www.catb.org/~esr/greed/) - A game of consumption. Eat as much as you can before munching yourself into a corner.
* [hangman](https://github.com/braheezy/hangman) - A Go TUI Hangman game built with the lovely BubbleTea framework.
* [kboard](https://github.com/CamiloGarciaLaRotta/kboard) - Terminal game to practice keyboard typing.
* [Language-games](https://github.com/Hellisotherpeople/Language-games) - Dead simple games made with word vectors.
* [mazter](https://github.com/Canop/mazter) - A maze in your terminal.
* [minesweeper](https://github.com/gazpachoking/minesweeper) - Cross-platform terminal based minesweeper.
* [Minesweeper Game](https://github.com/omerkarabacak/minesweeper) - A small command line Minesweeper Game.
* [nc2048](https://github.com/t0xk/nc2048) - A ncurses 2048 game that can be played in the terminal.
* [Nethack](http://nethack.org/) - Single player rogue-like dungeon exploration game.
* [Oldrunner](http://culot.org/public/Code/oldrunner.html) - Character-based remake of Lode Runner
* [othello-cli](https://github.com/LelsersLasers/othello-cli) - othello-cli is a cli version of Othello (Reversi) written in Rust. You can play against another player, the AI, or watch two AIs play each other.
* [Pokete](https://github.com/lxgr-linux/pokete) - A terminal based Pokemon like game.
* [rpg-cli](https://github.com/facundoolano/rpg-cli) - Your filesystem as a dungeon!
* [sku](https://github.com/fedeztk/sku) - Simple TUI written in go to play sudoku in the terminal.
* [Slash'EM](http://slashem.sourceforge.net/) - Rogue-like game derived from `nethack` offering extra features, monsters, and items; includes a GUI version.
* [Solitaire TUI](https://github.com/brianstrauch/solitaire-tui) - Klondike solitaire for the terminal.
* [sssnake](https://github.com/AngelJumbo/sssnake) - (Smart and sexy snake) The classic snake game for the terminal that can plays itself and be use like a screensaver.
* StarWars vision - See Star Wars in ASCII with ``telnet towel.blinkenlights.nl``.  
* [terdle](https://github.com/neelkarma/terdle) - Wordle implemented in Rust.
* [Terminal Phase](https://dustycloud.org/blog/terminal-phase-1.0/) - A space shooter game you can play in your terminal.
* [terminal_board_games](https://github.com/salt-die/terminally_bored_terminal_board_games) - Board games for the terminal.
* [terminordle](https://github.com/HP4k1h5/terminordle) - Inspired by the popular online game wordle made, you can play a pretty close replica of the original locally or multiplayer over the network.
* [Typespeed](http://typespeed.sourceforge.net/) - Type words that are flying by from left to right as fast as you can; features different word sets, e.g., UNIX commands, English words, Non-English words.
* [usolitaire](https://github.com/eliasdorneles/usolitaire) - Solitaire in your terminal.
* [wordle-curses](https://github.com/knosmos/wordle-curses) - A simple TUI wordle game with curses.
* [Words](https://github.com/ludovicianul/words) - A set of word-based puzzle games for the CLI while you wait for the build to run.

## <a name="git"></a>Git and accessories

* [BFG Repo-Cleaner](https://github.com/rtyley/bfg-repo-cleaner) - Removes large or troublesome blobs like git-filter-branch does, but faster.
* [czg](https://github.com/Zhengqbbb/cz-git) - Interactively generate standardized commit messages.
* [forgit](https://github.com/wfxr/forgit) - A utility tool powered by fzf for using git interactively.
* [fzf-git.sh](https://github.com/junegunn/fzf-git.sh) - bash and zsh key bindings for Git objects, powered by fzf.
* [gh-f](https://github.com/gennaro-tedesco/gh-f) - The ultimate, compact and snappy fzf extension for gh cli.
* [gh-s](https://github.com/gennaro-tedesco/gh-s) - Search github repositories interactively.
* [gh-stars](https://github.com/aymanbagabas/gh-stars) - A GitHub CLI extension to show repository stargazers.
* [git](https://git-scm.com/) - The winner across all the existing file versioning tools
* [Git Auto Sync](https://github.com/GitJournal/git-auto-sync) - Automatically commits changes to a git repository, and always keep that repo up to date.
* [git commander](https://github.com/golbin/git-commander) - A git tool with an easy interactive terminal interface.
* [git-all-branches](https://github.com/zacanger/git-all-branches) - Improved visualization of git branches (`git branch -a`).
* [git-annex](https://git-annex.branchable.com/) - Manages files with `git`, without checking the file contents into git; very useful to manage large/binary files.
* [git-cliff](https://github.com/orhun/git-cliff) - A highly customizable Changelog Generator that follows Conventional Commit specifications.
* [git-cz](https://github.com/streamich/git-cz) - Semantic Git commits.
* [git-extras](https://github.com/tj/git-extras) - Little git extras like git-ignore, git-setup, git-changelog, git-release, git-effort and more.
* [git-peek](https://github.com/Jarred-Sumner/git-peek) - git peek is the fastest way to open a remote git repository in your local text editor.
* [git-remote-aws](https://github.com/nathants/git-remote-aws) - Management of encrypted git hosting.
* [git-secret](https://github.com/sobolevn/git-secret) - A bash tool which stores private data inside a git repo; it uses users' public keys, allowing trusted users to access encrypted data using pgp and their secret keys.
* [git-stats](https://github.com/IonicaBizau/git-stats) - Local git statistics including GitHub-like contributions calendars.
* [gita](https://github.com/nosarthur/gita) - A command-line tool to manage multiple git repos.
* [Gitea](https://gitea.com/) - Single binary self-hosted Git service.
* [gitlab-cli](https://github.com/vishwanatharondekar/gitlab-cli) - Create GitLab merge requests.
* [gitsummary](https://github.com/glenreesor/gitsummary) - A better git status taht lists stashes, file statuses, branch list, all nicely formatted with color.
* [gitui](https://github.com/extrawurst/gitui) - GitUI provides you with the comfort of a git GUI but right in your terminal
* [GitUI](https://github.com/extrawurst/gitui) - The comfort of a git GUI but right in your terminal, with keyboard only control, scalable UI, and features all the necessary operations of git.
* [grv](https://github.com/rgburke/grv) - Git Repository Viewer - A terminal based interface for viewing Git repositories. It allows refs, commits and diffs to be viewed, searched and filtered.
* [onefetch](https://github.com/o2sh/onefetch) - Git repository summary on your terminal.
* [rcz](https://github.com/Cassin01/rcz) - A tool to write a commit message based on “Conventional Commits”.
* [sad](https://github.com/ms-jpq/sad) - CLI search and replace. Show you a nice diff of proposed changes before you commit them.
* [semantic-git-commit-cli](https://github.com/JPeer264/node-semantic-git-commit-cli) - Ensure semantic commits messages. With emoji support.
* [Soft Serve](https://github.com/charmbracelet/soft-serve) - Self-hostable Git server for the command line. One distinguished feature is the possibility to create new repositories with a push.
* [stargazer](https://github.com/gennaro-tedesco/stargazer) - Github stats from the command line.
* [tig](https://github.com/jonas/tig) - An ncurses-based text-mode interface for `git` that can act as a repository browser, but can also assist in staging changes for commit at chunk level.
* [travelgrunt](https://github.com/ivanilves/travelgrunt) - cd inside [mono]repos without fatigue.

## <a name="graphics"></a>Graphics

* [Aewan](http://aewan.sourceforge.net/) - Aewan is a multi-layered ASCII graphics/animation editor. It produces stand-alone cat-able ASCII art files and an easy-to-parse format for integration into terminal applications.
* [Artem](https://github.com/FineFindus/artem) - Convert images from multiple formats (jpg, png, webp, etc…) to ASCII art, written in Rust.
* [chafa](https://github.com/hpjansson/chafa) - Terminal graphics for the 21st century.
* [cli-mandelbrot](https://github.com/danyshaanan/cli-mandelbrot) - A cli for traversing the Mandelbrot fractal.
* [D2](https://github.com/terrastruct/d2) - D2 is a modern diagram scripting language that turns text to diagrams.
* [deviceframe](https://github.com/c0bra/deviceframe) - Put device frames around mobile/web/progressive app screenshots.
* [gifgen](https://github.com/lukechilds/gifgen) - Simple high quality GIF encoding.
* [gifsicle](https://github.com/kohler/gifsicle) - Create, manipulate, and optimize GIF images and animations.
* [givegif](https://github.com/passy/givegif) - GIFs on the command line.
* [GraphicsMagick](http://www.graphicsmagick.org/) - Swiss army knife of image processing.
* [ImageMagick](http://www.imagemagick.org/script/index.php) - Software suite to create, edit, compose, or convert bitmap images; it handles many file formats (including PDF and SVG) and provides processing tools to "resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves".
* [imgcat](https://github.com/trashhalo/imgcat) - Tool to output images in the terminal. Built with bubbletea.
* [imgp](https://github.com/jarun/imgp) - A command line image resizer and rotator for JPEG and PNG images. It can resize (or thumbnail) and rotate thousands of images in a go, at lightning speed, while saving significantly on storage.
* [inklayers](https://github.com/toolleeo/inklayers) - A command line program that exports layers from an SVG file. It can be used to create slide shows by editing a single SVG file.
* [jp2a](https://csl.name/jp2a/) - Command-line tool that converts images to ASCII art in the Linux terminal.
* [kakikun](https://github.com/file-acomplaint/kakikun) - Kakikun is a tool to paint, draw and create ASCII art in your terminal using unicode characters.
* [Korkut](https://github.com/oguzhaninan/korkut) - Quick and simple image processing with the following functions: optimize, convert, crop, resize, rotate, watermark, flip.
* [LinuxLogo](https://sourceforge.net/projects/linuxlogo/) - Display the Linux distribution logo in ASCII format.
* [mandelbrot-cli](https://github.com/MicheleFiladelfia/mandelbrot-cli) - Multiplatform terminal mandelbrot set explorer.
* [MapSCII](https://github.com/rastapasta/mapscii) - A Braille & ASCII world map renderer for your console
* [Mercator](https://github.com/mrusme/mercator) - OpenStreetMap but as terminal user interface (TUI) program.
* [pastel](https://github.com/sharkdp/pastel) - A command-line tool to generate, analyze, convert and manipulate colors.
* [scrot](https://github.com/dreamer/scrot) - A simple CLI tool to capture screenshots.  
* [svgcleaner](https://github.com/RazrFalcon/svgcleaner) - Clean up your SVG files from the unnecessary data.
* [SVGO](https://github.com/svg/svgo) - SVG Optimizer is a Node.js-based tool for optimizing SVG vector graphics files.
* [vhs](https://github.com/charmbracelet/vhs) - Write terminal GIFs as code for integration testing and demoing your CLI tools.

## <a name="multimedia"></a>Multimedia

Programs to specifically deal audio/video files.

* [BadaBoomBooks](https://github.com/WirlyWirly/BadaBoomBooks) - Quickly organize audiobooks using a terminal and web-browser.
* [cTune](https://github.com/An7ar35/ctune) - A ncurses based internet radio player written in C for Linux.
* [Editly](https://github.com/mifi/editly) - A tool and framework for declarative NLE (non-linear video editing) using Node.js and ffmpeg.
* [ffmpeg](https://ffmpeg.org/) - The Swiss knife of video editing from the command line.
* [ffscreencast](https://github.com/cytopia/ffscreencast) - A ffmpeg screencast with video overlay and multi monitor support.
* [invidtui](https://github.com/darkhz/invidtui) - Invidious TUI client, which fetches data from invidious instances and displays a user interface in the terminal, and allows for selecting and playing Youtube audio and video.
* [lotc](https://github.com/ranelpadon/lord-of-the-clips) - (Lord Of The Clips) Video downloader, trimmer, and merger using the terminal. Supports YouTube, Facebook, Reddit, Twitter, etc. Downloads/trims at multiple points. Merges multiple clips.
* [YouTube TUI](https://siriusmart.github.io/youtube-tui/) - A lightweight and user friendly TUI for browsing YouTube content from the terminal.

## <a name="networking"></a>Networking

Programs to deal with networks and communication.

* [bandwhich](https://github.com/imsnif/bandwhich) - Terminal bandwidth utilization tool.
* [bluetuith](https://github.com/darkhz/bluetuith) - A TUI-based Bluetooth connection manager, which can interact with Bluetooth adapters and devices. It aims to be a replacement to most Bluetooth managers, like blueman.
* [bore](https://github.com/ekzhang/bore) - A simple CLI tool for making tunnels to localhost.
* [geoiplookup](https://github.com/maxmind/geoip-api-c) - A little application to find geographical and network information of an IP address based no the geoip C API.
* [hflow](https://github.com/comradequinn/hflow) - A command-line, debugging http/s proxy server.
* [ipcalc](http://jodies.de/ipcalc) - Takes an IP address and netmask and calculates the resulting broadcast, network, Cisco wildcard mask, and host range.
* [mitmproxy](https://mitmproxy.org/) - An interactive HTTPS proxy.
* [mosh](https://mosh.org/) - Remote SSH client that achieve good responsiveness in presence of intermittent connectivity and roaming.
* [Optic](https://www.useoptic.com/) - Optic's Open Source tools make OpenAPI and API-first practices easy for any team to adopt.
* [PSSH](https://code.google.com/archive/p/parallel-ssh/) - PSSH provides parallel versions of OpenSSH and related tools. Included are pssh, pscp, prsync, pnuke, and pslurp. The project includes psshlib which can be used within custom applications.
* [quickserve](https://github.com/haileys/quickserve) - Quickserve is a very simple HTTP server written in Python that is intended for quickly sharing files on an ad-hoc basis. Aside from opening a port in your firewall if you have one, quickserve requires no set-up and should work with no hassle.
* [redive](https://github.com/neelkarma/redive) - Trace URL redirections in the terminal.
* [rtop](http://www.rtop-monitor.org/) - rtop is a simple, agent-less, remote server monitoring tool that works over plain SSH. Written in golang, it does not need any software to be installed on the server that you want to monitor. It works by establishing an SSH session, and running commands on the remote server to collect system metrics.
* [Rustcat](https://github.com/robiot/rustcat) - Netcat Alternative in Rust.
* [serve](https://github.com/vercel/serve) - Serves a static site, single page application, or just a static file, and provides a neat interface for listing the directory's contents.
* [speedtest-net](https://github.com/ddsol/speedtest.net) - Test internet connection speed and ping using speedtest.net.
* [termishare](https://github.com/qnkhuat/termishare) - Peer to peer terminal sharing.
* [TStream](https://github.com/qnkhuat/tstream) - Live streaming from the terminal. Requires the connection to a central server, from which the streaming is dispatched.
* [ttyd](https://github.com/tsl0922/ttyd) - Share your terminal over the web.
* [Tunnelmole](https://github.com/robbie-cahill/tunnelmole-client) - Connect to local servers from anywhere.
* [Wishlist](https://github.com/charmbracelet/wishlist) - With Wishlist you can have a single entrypoint for multiple SSH endpoints.
* [xiringuito](https://github.com/ivanilves/xiringuito) - VPN made easy! No configuration. No VPN servers. No hassle. Using SSH capabilities.
* [xxh](https://github.com/xxh/xxh) - Bring your favorite shell wherever you go through the ssh.

## <a name="note-taking"></a>Note taking

* [cadmus](https://github.com/RyanGreenup/cadmus) - Shell Scripts to Facilitate Effective Note Taking.
* [dn](https://github.com/tomlockwood/dn) - Daily notes command line tool.
* [dnote](https://github.com/dnote/dnote) - A simple command line notebook for the terminal. It also offers a seamless multi-device sync and a web interface.
* [eureka](https://github.com/simeg/eureka) - Store your ideas without leaving the terminal.
* [Geeknote](https://github.com/jeffkowalski/geeknote) - A command line client for Evernote that can be use on Linux, FreeBSD and OS X.
* [idea](https://github.com/IonicaBizau/idea) - A lightweight tool for keeping ideas in a safe place quick and easy.
* [jnrl](https://github.com/maebert/jrnl) - Collect your thoughts and notes without leaving the command line.
* [jot](https://github.com/araekiel/jot) - Jot is a feature-stripped version of Obsidian focused on rapid note management through the terminal. It uses the same format of storage as Obsidian.
* [journalC](https://github.com/Dr-42/journalC) - A simple encrypted terminal jounaling book.
* [kb](https://github.com/gnebbia/kb) - A minimalist knowledge base manager.
* [meudeus](https://github.com/dj8yfo/meudeus) - A skim-based `*.md` explore and surf tool.
* [nb](https://github.com/xwmx/nb) - A command line and local web note-taking, bookmarking, archiving, and knowledge base application.
* [Noted](https://github.com/torbratsberg/noted) - Notes library, with viewer and shortcuts to add, delete and edit notes.
* [NoteSH](https://github.com/Cvaniak/NoteSH) - Sticky notes App in the Terminal, built with Textual, an amazing TUI framework!
* [posce](https://github.com/vdt/posce) - A note-taking toolkit for your command line.
* [sncli](https://github.com/insanum/sncli) - A Python application that gives you access to your Simplenote account via the command line.
* [Standard Unix Notes](https://github.com/Standard-Unix-Notes/unix-notes) - GPG Encrypted Notes/Notebook manager for BSD/Linux.
* [Terminal velocity](https://vhp.github.io/terminal_velocity/) - A fast, cross-platform note-taking application for the UNIX terminal.

## <a name="office"></a>Office tools

Spreadsheet and presentations.

* [conan](https://github.com/mirage/conan) - Find clue about the type of the file.
* [conrad](https://github.com/vinayak-mehta/conrad) - Track conferences and meetups.
* [DeckTape](https://github.com/astefanutti/decktape) - DeckTape is a high-quality PDF exporter for HTML presentation frameworks.
* [Lotus 1-2-3 for Linux](https://github.com/taviso/123elf) - A native port of Lotus 1-2-3 Release 3 to Linux.
* [mdp](https://github.com/visit1985/mdp) - A command-line based markdown presentation tool.
* [Quoter](https://github.com/frossm/quoter) - The console based stock quote tool.
* [sc-im](https://github.com/andmarti1424/sc-im) - Spreadsheet Calculator Improvised -- An ncurses spreadsheet program for terminal. It is rich in functionalities, but the syntax of functions and other details are different from the common spreadsheets such as Excel and Calc, making difficult to "re-cycle" existing knowledge on these programs to work proficiently with sc-im. Neverthless, a nice piece of software."
* [scholarref](https://adamsgaard.dk/scholarref.html) - Tools to never deal with journal webpages again.
* [sent](https://tools.suckless.org/sent/) - Simple plaintext presentation tool.
* [Slides](https://github.com/maaslalani/slides) - Terminal based presentation tool.
* [Teapot](https://www.syntax-k.de/projekte/teapot/) - Compact ncurses-based spreadsheet with original syntax, 3D-style and built-in functions.
* [Ticker](https://github.com/achannarasappa/ticker) - Terminal stock watcher and stock position tracker.
* [tpp](http://www.ngolde.de/tpp.html) - (text presentation program) a ncurses Ruby program that allows to produce nice text-based presentation with simple markup language.
* [translate-shell](https://github.com/soimort/translate-shell) - Command-line translator using Google Translate or other online services.
* [trino](https://github.com/eneserdogan/trino) - Quick and easy translation of words and phrases entered in the command line.  
* [VocabCLI](https://github.com/HighnessAtharva/VocabCLI) - Lightweight CLI that allows users to look up word definitions, examples, synonyms and antonyms directly via the command line; it also offers advanced Text Classification and Processing via the use of Natural Language Processing and Machine Learning algorithms.
* [wikit](https://github.com/KorySchneider/wikit) - A command line program for getting Wikipedia summaries easily.

## <a name="organizers"></a>Organizers and calendars

Calendar managers.

* [addrb](https://github.com/mrusme/addrb) - A lightweight CLI / TUI address book that supports CardDAV.
* [buku](https://github.com/jarun/buku) - A powerful bookmark manager written in Python3 and SQLite3.
* [Calcure](https://github.com/anufrievroman/calcure) - Modern TUI calendar and task manager with customizable interface.
* [calcurse](https://calcurse.org/) - A calendar and scheduling application for the command line. It helps keep track of events, appointments and everyday tasks.
* [caldr](https://github.com/mrusme/caldr) - A lightweight CLI / TUI calendar that supports CalDAV.
* [gcalcli](https://github.com/insanum/gcalcli) - CLI to access Google Calendars; allows to do the main tasks: create, delete, and list events.
* [goobook](https://gitlab.com/goobook/goobook) - The purpose of GooBook is to make it possible to use your Google Contacts from the command-line and from MUAs such as Mutt.  It can be used from Mutt the same way as abook.
* [khal](https://github.com/pimutils/khal) - CLI and terminal calendar program, able to synchronize with CalDAV servers through [vdirsyncer](https://github.com/pimutils/vdirsyncer).
* [khard](https://github.com/lucc/khard) - Console carddav client written in Pyhton.  
* [Org mode](http://orgmode.org/) - Super-powerful [Emacs](https://www.gnu.org/software/emacs/) plugin to manage outlines with associated timestamps, priorities, labels, etc.; available views grouped by time (agenda), tags, etc.; plain text storage format.
* [pal](http://palcal.sourceforge.net/) - Calendar program for Unix/Linux systems that can keep track of events; custom, plain text storage format; interesting and fully functional.
* [peroutine](https://github.com/UlyssesZh/peroutine) - Remind you of periodical events. The period can be any positive integer of days, so work around the fact that the number of days in a week is prime.
* [ppl addressbook](http://ppladdressbook.org/) - `ppl` is free software made out of other free software.  It's built on top of Ruby and Git, and the completely free vcard address book format.
* [Remind](https://dianne.skoll.ca/projects/remind/) - Calendar program with possibility to set complex rules to define events; custom, powerful text-based storage format.
* [remint](https://sr.ht/~mlaparie/remint/) - A simple terminal UI wrapper for D. Skoll's Remind calendar program
* [vdirsyncer](https://github.com/pimutils/vdirsyncer) - CalDAV synchronization program.
* [Wyrd](http://freecode.com/projects/wyrd/) - Curses front-end for [Remind](https://www.roaringpenguin.com/products/remind) written in OCaml with vertically scrollable time table.  

## <a name="online"></a>Online search and resources

* [arch-wiki](https://github.com/deadhead420/arch-wiki) - Search the Arch Wiki anywhere from the command line.  
* [Awesome CLI](https://github.com/umutphp/awesome-cli) - Awesome CLI is a simple command line tool to give you a fancy command line interface to dive into Awesome lists.
* [Awesome Finder](https://github.com/mingrammer/awesome-finder) - Search the awesome lists from the command line.
* [ddgr](https://github.com/jarun/ddgr) - A command line utility to search DuckDuckGo (html version) from the terminal.
* [googler](https://github.com/jarun/googler) - Google Search, Google Site Search, Google News from the terminal.
* [pockyt](https://github.com/achembarpu/pockyt) - Read, manage, and automate the collection of articles in [Pocket](https://getpocket.com), an application for managing a reading list of articles from the Internet.
* [Seashells](https://seashells.io/) - Pipe output to the web.
* [so](https://github.com/samtay/so) - Terminal interface for Stack Overflow.
* [socialscan](https://github.com/iojw/socialscan) - Python library and CLI for accurately querying username and email usage on online platforms.
* [socli](https://github.com/gautamkrishnar/socli) - Stack overflow command line client written in Python.  Search and browse stack overflow without leaving the terminal 

## <a name="password-manager"></a>Password managers

* [Bitwarden CLI](https://bitwarden.com/help/cli/) - Command-line interface for Bitwarden, a multi-platform password manager targeted to companies and enterprises.
* [cpass](https://github.com/xlucn/cpass) - Another console UI for pass.
* dpg - The Deterministic Password Generator - Generates passwords based on a master password and the indication of the website/service/username, without the need of storing anything.
* [gopass](https://www.gopass.pw/) - gopass is a rewrite of the pass password manager in Go with the aim of making it cross-platform and adding additional features. The target audience are professional developers and sysadmins (and especially teams of those) who are well versed with a command line interface.
* [hide](https://github.com/whatl3y/hide) - AES-256 bit encrypted password manager with all encrypted passwords stored locally on your machine
* [keydex](https://github.com/shikaan/keydex) - Manage KeePass databases from your terminal.
* [kpcli](http://kpcli.sourceforge.net/) - A command line interface for KeePass.
* [pa](https://github.com/biox/pa) - A simple password manager; encryption via age, written in portable posix shell.
* [pass](https://www.passwordstore.org/) - With pass, each password lives inside of a gpg encrypted file whose filename is the title of the website or resource that requires the password. These encrypted files may be organized into meaningful folder hierarchies, copied from computer to computer, and, in general, manipulated using standard command line file management utilities.
* [passfzf](https://git.sr.ht/~mlaparie/passfzf) - A simple fzf wrapper for pass (the UNIX password-store). It allows fuzzy finding your pass passwords to copy, show, edit, delete, rename and duplicate them.
* [Pswd](https://github.com/Mandrew0822/pswd) - A secure password generator written in C.
* [safe.sh](https://github.com/windowsrefund/safe) - Pure Bash script to manage secure archives; simple and clean; uses [gnugpg](https://gnupg.org/) for encryption/decryption, thus can leverage tools like [GPG Agent](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html).
* [SpicyPass](https://github.com/JFreegman/SpicyPass) - A light-weight password manager with a focus on simplicity and security.
* [titan](https://www.byteptr.com/titan/) - Password management belongs to the command line, deep into the Unix heartland, the shell. Titan is written in C and is available under the MIT license.

## <a name="productivity"></a>Productivity

* [ancv](https://github.com/alexpovel/ancv) - Renders your (JSON) resume/CV for online & pretty terminal display.
* [arbtt](http://arbtt.nomeata.de/) - (automatic, rule-based time tracker) runs in background, collecting information regarding open windows, focussed ones, etc.; it can be configured to display statistics on the collected data, e.g., figuring out the time spent on one specific window.
* [avail](https://github.com/mufeez-amjad/avail) - Find available times between all your calendars.
* [Bartib](https://github.com/nikolassv/bartib) - Easy to use time tracking tool for the command line. It saves a log of all tracked activities as a plaintext file and allows you to create flexible reports.
* [cambd-cli](https://github.com/rocktimsaikia/cambd) - A CLI tool to automate the process to access the Cambridge dictionary.
* [CLI-Dictionary](https://github.com/Lodobo/dict.py) - Scripts for downloading and viewing wiktionary entries from Kaikki.org.
* [Clipboard](https://getclipboard.app/) - An easy-to-use information management tool that acts like an external brain.
* [cowyo](https://github.com/schollz/cowyo) - Feature rich wiki webserver for minimalists.
* [dijo](https://github.com/NerdyPepper/dijo) - Scriptable, curses-based, digital habit tracker.
* [doing](https://github.com/ttscoff/doing) - A command line tool for remembering what you were doing and tracking what you've done.
* [fasttyper](https://github.com/ickyicky/fasttyper) - Fasttyper is minimalistic typing test based on user provided exercising text.
* [flash-tui](https://github.com/TBS1996/speki) - Flashcard app for the terminal.
* [gdir](https://github.com/pafoster/gdir) - A command line tool which queries Google Directions. The tool displays results as human-readable text.
* [GTT - Google Translate TUI](https://github.com/eeeXun/GTT) - A TUI interface to bring Google Translation in the terminal.
* [h-m-m](https://github.com/nadrad/h-m-m) - h-m-m (pronounced like the interjection "hmm") is a simple, fast, keyboard-centric terminal-based tool for working with mind maps.
* [habitctl](https://github.com/blinry/habitctl) - Minimalist command line tool you can use to track and examine your habits.
* [habitmap](https://github.com/shuu-wasseo/habitmap) - A command-line app to track your habits and visualise how committed you are to making or maintaining them with colorful heatmaps.
* [hardv](https://github.com/dongyx/hardv) - A CLI flashcard app for UNIX-compatible systems, conforming to the UNIX philosophy.
* [hledger](https://hledger.org/) - A is fast, reliable, free, multicurrency double-entry accounting software to track money, investments, cryptocurrencies, time, or any other quantifiable commodity; uses a future-proof plain text file format.
* [kabmat](https://github.com/PlankCipher/kabmat) - TUI program for managing kanban boards with vim-like keybindings.
* [ledger](http://ledger-cli.org/) - A powerful, double-entry accounting system from the command-line; it uses a simple yet powerful text syntax to specify the items to account.
* [moeda](https://github.com/thompsonemerson/moeda) - A foreign exchange rates and currency conversion using the command line.
* [Moro](https://github.com/getmoro/moro) - A command line tool for tracking work hours, as simple as it can get.
* [paycon](https://github.com/arcorion/paycon) - Converts pay amounts between different time units.
* [Productivity Timer](https://github.com/h-sifat/productivity-timer) - A CLI/TUI Pomodoro timer and todo (coming soon) application for keyboard addicts and terminal fans that makes you more productive.
* [py_flashcards](https://github.com/M4THYOU/py_flashcards) - Text-only CLI flashcards parsed from Markdown file.
* [speedread](https://github.com/pasky/speedread) - A simple terminal-based open source Spritz-alike filter that shows input text as a per-word RSVP (rapid serial visual presentation) aligned on optimal reading points.
* [speki](https://github.com/tbs1996/speki) - Manage flashcards in the terminal
* [Taskell](https://github.com/smallhadroncollider/taskell) - A CLI kanban board/task manager for Mac and Linux.
* [Termtyper](https://github.com/kraanzu/termtyper) - An awesome TUI monkeytype like typing application to level up your fingers!
* [thokr](https://github.com/jrnxf/thokr) - Sleek typing tui with visualized results and historical logging.
* [Timetrap](https://github.com/samg/timetrap) - A simple command line time tracker written in Ruby. It provides an easy to use command line interface for tracking what you spend your time on.
* [Timewarrior](https://github.com/GothenburgBitFactory/timewarrior) - A time tracking utility that offers simple stopwatch features as well as sophisticated calendar-based backfill, along with flexible reporting.
* [toipe](https://github.com/Samyak2/toipe) - Yet another typing test, but crab flavoured.
* [Translate Shell](https://www.soimort.org/translate-shell/) - Command-line translator using Google Translate, Bing Translator, Yandex.Translate, etc.
* [tuxi](https://github.com/Bugswriter/tuxi) - A CLI tool that scrapes Google search results and SERPs that provides instant and concise answers.
* [tz](https://github.com/oz/tz) - tz helps you schedule things across time zones. It's an interactive TUI program that displays time across the time zones of your choosing.
* [utt](https://github.com/larose/utt) - Ultimate Time Tracker - A simple command-line time tracker written in Python.
* [Watson](https://github.com/TailorDev/Watson) - Time tracking CLI to know how much time you are spending on your projects. It can generate nice reports for clients.
* [zeitkatze](https://github.com/leonmavr/zeitkatze) - Simplest stopwatch in a linux console.

## <a name="programming"></a>Programming

* [add-gitignore](https://github.com/TejasQ/add-gitignore) - Interactively generate a .gitignore for software projects.
* [boilr](https://github.com/tmrts/boilr) - Boilerplate template manager that generates files or directories from template repositories.
* [cgasm](https://github.com/bnagy/cgasm) - Pronounced “SeekAzzem”, it is a standalone, offline terminal-based tool with no dependencies that gives me x86 assembly documentation.
* [chars](https://github.com/antifuchs/chars) - Display names and codes for various ASCII (and unicode) characters / code points.
* [cloc](https://github.com/AlDanial/cloc) - Tool for counting blank lines, comment lines, and physical lines of source code in many programming languages.
* [clog](https://github.com/clog-tool/clog-cli) - Creates a changelog automatically from local git metadata.
* [CodeMark CLI](https://github.com/rootCircle/codemark-cli) - Helps you manage coding assignments and tests; easily initialize the configuration, list assignments, fetch and check your code, submit your code for grading, and get AI-powered error recommendations.
* [Cookiecutter](https://github.com/cookiecutter/cookiecutter) - A cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects.
* [Cppcheck](http://cppcheck.net/) - Static analysis tool for C/C++ code providing unique code analysis to detect bugs and focuses on detecting undefined behaviour and dangerous coding constructs.
* [dtool](https://github.com/guoxbin/dtool) - Collection of development tools.
* [fastmod](https://github.com/facebookincubator/fastmod) - A tool to assist you with large-scale codebase refactors, and it supports most of codemod's options. It is focused on improving the use case "I want to use interactive mode to make sure my regex is correct, and then I want to apply the regex everywhere".
* [fmake](https://github.com/bharatvaj/fmake) - Brings `make`s interface to almost any build system.
* [Frama-C](https://frama-c.com/) - Open-source extensible and collaborative platform dedicated to source-code analysis of C software. Frama-C can assist from the navigation through unfamiliar projects up to the certification of critical software.
* [gdb-dashboard](https://github.com/cyrus-and/gdb-dashboard) - Modular visual interface for GDB in Python.
* [grex](https://github.com/pemistahl/grex) - A command-line tool for generating regular expressions from user-provided test cases.
* [hors](https://github.com/WindSoilder/hors) - Instant coding answers via the command line.
* [howdoi](https://github.com/gleitz/howdoi) - Instant coding answers via the command line.
* [kickstart](https://github.com/Keats/kickstart) - Scaffolding tool to get new projects up and running quickly.
* [Kool](https://github.com/kool-dev/kool) - CLI tool that brings the complexities of modern software development making these environments lightweight, fast and reproducible.
* [legit](https://github.com/captainsafia/legit) - Automagically generates a LICENSE file for the current working directory that you are in or a license header for a file where applicable.
* [license-up](https://github.com/nikitavoloboev/license-up) - Create a license quickly for a given name.
* [mklicense](https://github.com/cezaraugusto/mklicense) - CLI tool for easily generating the text of the most common licenses.
* [nbterm](https://github.com/davidbrochart/nbterm) - Jupyter Notebooks in the terminal.
* [pire](https://github.com/johannestaas/pire) - Python Interactive Regular Expressions.
* [Proji](https://github.com/nikoksr/proji) - Powerful cross-platform CLI project templating tool.
* [pvcheck](https://github.com/claudio-unipv/pvcheck) - A tool to apply automated testing to programs that produce textual output. The format of the output is very specific, making pvcheck suitable to test programming quizzes.
* [readme-md-generator](https://github.com/kefranabg/readme-md-generator) - CLI that generates beautiful README.md files.
* [rebound](https://github.com/shobrook/rebound) - Fetch Stack Overflow results in your terminal when you get an error. Supported languages: Python, Node.js, Ruby, Golang, and Java.
* [release-it](https://github.com/release-it/release-it) - Automate releases for Git repositories and/or Node.js packages.
* [rr](https://rr-project.org/) - Debug the recording, deterministically, as many times as you want.
* [scc](https://github.com/boyter/scc) - Sloc Cloc and Code (scc) is a codebase statistics counter. Goal is to be the fastest code counter possible, but also perform COCOMO calculation like sloccount and to estimate code complexity similar to cyclomatic complexity calculators. In short one tool to rule them all.
* [scons](https://github.com/SCons/scons) - Software construction tool.
* [temci](https://github.com/parttimenerd/temci) - Advanced benchmarking tool written in Python 3 that supports setting up an environment for benchmarking and the generation of visually appealing reports.
* [Tokei](https://github.com/XAMPPRocky/tokei) - Tokei is a program that displays statistics about your code. Tokei will show the number of files, total lines within those files and code, comments, and blanks grouped by language.
* [umake](https://github.com/mcandre/unmake) - Makefile linter emphasizing portability, targeting the POSIX make standard.

## <a name="science"></a>Science

Tools for scientific research and science applications.

* [bib.awk](https://github.com/huijunchen9260/bib.awk) - Bibliography manager written in awk.
* [cobib](https://gitlab.com/mrossinek/cobib) - Simple, command-line based bibliography management tool.
* [element](https://github.com/gennaro-tedesco/element) - Periodic table on the command line.
* [FAWOC](https://github.com/robolab-pavia/fawoc) - FAWOC is a TUI program for manually labelling a list of words. It has been developed to support the efficient clustering of documents based on topic modeling algorithms such as Dirichlet Latent Allocation.
* [Go-L](https://github.com/Jeadie/Go-L) - Game of Life with different update rules and on a bunch of different topologies (sphere, torus, klein bottle, etc.).
* [papis](https://github.com/alejandrogallo/papis) - Extensible document and bibliography manager.
* [pt.sh](https://github.com/alexeytal/pt.sh) - CLI periodic table with search and many properties.
* [ptable](https://github.com/velorek1/ptable) - A beautiful TUI periodic table for GNU/linux terminals.
* [Pubs](https://github.com/pubs/pubs) - Pubs organizes your scientific papers together with their bibliographic data and provides command line access to basic and advanced manipulation of your library.
* [slr-kit](https://github.com/robolab-pavia/slr-kit) - Set of CLI tools to assist the writing of Systematic Literature Reviews powered by Natural Language Processing.
* [starfetch](https://github.com/Haruno19/starfetch) - Command line tool that displays constellations.

## <a name="security"></a>Security and encryption

Cryptography, ciphered archive managers, encrypted file-systems.

* [acmetool](https://github.com/hlandau/acmetool) - Easy-to-use command line tool for automatically acquiring certificates from ACME servers (such as Let's Encrypt).
* [cipher](https://github.com/ash-shell/cipher) - An Ash module that makes it easy to perform aes-256-cbc encryption for files and directories.  
* [cotp](https://github.com/replydev/cotp) - Trustworthy, encrypted, command-line TOTP/HOTP authenticator app with import functionality.
* [cream](https://z3bra.org/cream/) - Encrypt and decrypt streams of data with only a master password. The key is derivated from the password + salt combo, and used to encrypt data byte per byte.
* [enc](https://github.com/life4/enc) - A modern and friendly CLI alternative to GnuPG: generate and download keys, encrypt, decrypt, and sign text and files, and more.
* [encfs](http://www.arg0.net/#!encfs/c1awt) - Encrypted filesystem in user-space based on [FUSE](https://it.wikipedia.org/wiki/FUSE)
* [feroxbuster](https://github.com/epi052/feroxbuster) - A fast, simple, recursive content discovery tool written in Rust.
* [Firejail](https://firejail.wordpress.com/) - A SUID program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces and seccomp-bpf.
* [GnuPG](https://gnupg.org/) - GnuPG is a complete and free implementation of the OpenPGP standard as defined by RFC4880 (also known as PGP).
* [hashcat](https://hashcat.net/hashcat/) - A robust and efficient password cracking tool that can help you recover lost passwords, audit password security, benchmark, or just figure out what data is stored in a hash.
* [Image Steganography Tool](https://github.com/7thSamurai/steganography) - Simple C++ Encryption and Steganography tool that uses Password-Protected-Encryption to secure a file's contents.
* [LUKS](https://guardianproject.info/code/luks/) - Hard disk encryption tool; it stores all setup information in the partition header, enabling easy data transport or migration.
* [Minisign](https://github.com/jedisct1/minisign) - A dead simple tool to sign files and verify digital signatures.
* [OAuth2c](https://github.com/cloudentity/oauth2c) - A command-line tool for interacting with OAuth 2.0 authorization servers.
* [ots](https://github.com/sniptt-official/ots) - Share end-to-end encrypted secrets with others via a one-time URL.
* [PaperAge](https://github.com/matiaskorhonen/paper-age) - Easy and secure paper backups of secrets, which takes a text and generates an encrypted QRcode to print on paper.
* [pgen](https://github.com/ctsrc/Pgen) - Generate passphrases using the wordlists for random passphrases made by the EFF.
* [StegCloak](https://github.com/kurolabs/stegcloak) - Hide secrets with invisible characters in plain text securely using passwords
* [uacme](https://github.com/ndilieto/uacme) - ACMEv2 client written in plain C with minimal dependencies.
* [wifi-password](https://github.com/rauchg/wifi-password) - Get wifi pass.

## <a name="shells"></a>Shells

* [Bash](https://www.gnu.org/software/bash/) - (Bourne Again SHell) The most widespread system shell to date.  
* [Cat9](https://github.com/letoram/cat9) - Cat9 is a user shell script for LASH - a command-line shell that discriminates against terminal emulators, written in Lua.
* [cosh](https://github.com/tomhrr/cosh) - Concatenative command-line shell.
* [Fish](https://fishshell.com/) - "A command line shell for the 90s"; focused on user-friendliness, with powerful autosuggestions, colors, "sane scripting" (w.r.t. to Bash).
* [N-Commodore](https://github.com/psprint/n-commodore) - A novel file manager/shell/command-line, where everything is panelized, greppable and remembered.
* [Reptyl](https://github.com/0ut0flin3/Reptyl) - A cross-platform command line shell that supports execution of commands in natural language.
* [Spaceship](https://spaceship-prompt.sh/) - Minimalistic, powerful and extremely customizable Zsh prompt.
* [xonsh](https://xon.sh/) - The xonsh shell lets you easily mix Python and shell commands in a powerful and simplified approach to the command line.
* [Zsh](http://www.zsh.org/) - Alternative shell designed for interactive use.  

## <a name="music"></a>Sound and music

Music players.

* [Alsamixer](http://www.alsa-project.org/main/index.php/Main_Page) - ALSA mixer with curses interfaces.  
* [beets](https://github.com/beetbox/beets) - Beets is the media library management system for obsessive music geeks: catalogs your collection, automatically improving its metadata as it goes.
* [castero](https://github.com/xgi/castero) - A TUI podcast client for the terminal.
* [cmus](https://cmus.github.io/) - A fast and lightweight audio player with configurable keybindings and playlist support.  
* [dzr](https://github.com/yne/dzr) - Command Line deezer.com Player for Linux, BSD, Android, Windows.
* [espeak](http://espeak.sourceforge.net/) - A compact open source software speech synthesizer for English and other languages.
* [Instant Music Downloader](https://github.com/yask123/Instant-Music-Downloader) - Instantly download any song!
* [kord](https://github.com/synestematic/kord) - A python framework that provides programmers with a simple api for the creation of music-based applications.
* [MOC](https://moc.daper.net/) - (music on console) is a powerful and easy to use console audio player
* [Mp3blaster](http://www.mp3blaster.org/?m=1) - Audio player for the text console.
* [mpg123](http://mpg123.org/) - Quick `mp3` sound file player; no visual interface, just a command-line audio file player for `mp3` files.
* [mps-youtube](https://github.com/mps-youtube/yewtube) - A curses player for music tracks from Youtube; it allows to search for songs and playlists; it downloads the video, extracts the audio track and plays it; handles local playlists and many configuration parameters.
* [mpvc](https://github.com/gmt4/mpvc/) - A minimal mpc-like CLI and TUI for controlling mpv from the shell.
* [muCLIar](https://github.com/aayush1205/muCLIar) - YouTube automator bringing you your music right on your CLI.
* [MusicPlayerPlus](https://github.com/doctorfree/MusicPlayerPlus) - Featureful ncurses based MPD client inspired by ncmpc with integration for Beets, spectrum visualization,Bandcamp/Soundcloud, asciimatics, cantata, and more.
* [musikcube](https://github.com/clangen/musikcube) - A cross-platform, terminal-based audio engine, library, player and server written in C++.
* [ncmpcpp](https://rybczak.net/ncmpcpp/) - NCurses Music Player Client (Plus Plus) - featureful ncurses based MPD client inspired by ncmpc. Relevant features: tag editor, playlist editor, easy to use search engine, media library, music visualizer, ability to fetch artist info from [last.fm](https://www.last.fm/), new display mode, alternative user interface, ability to browse and add files from outside of MPD music directory.
* [ogg123](https://www.xiph.org/downloads/) - Quick `ogg` sound file player; no visual interface, just a command-line audio file player for the free and open `ogg` file format.
* [PyRadio](https://github.com/coderholic/pyradio) - Curses based internet radio player.
* [Siren](https://www.kariliq.nl/siren/) - Siren is a text-based audio player for UNIX-like operating systems.
* [Spotify TUI](https://github.com/Rigellute/spotify-tui) - A Spotify client for the terminal written in Rust.
* [spotify-player](https://github.com/aome510/spotify-player) - spotify-player is a fast, easy to use, and configurable terminal music player having feature parity with the official Spotify application.
* [Tera](https://github.com/shinokada/tera) - Terminal Radio: an easy-to-use CLI music player to play favorite music, radio stations and explore various radio stations from the terminal only.
* [termusic](https://github.com/tramhao/termusic) - Terminal Music Player written in Rust.
* [Tizonia](https://github.com/tizonia/tizonia-openmax-il) - Command-line cloud music player for Linux with support for Spotify, Google Play Music, YouTube, SoundCloud, TuneIn, iHeartRadio, Plex servers and Chromecast devices.
* [yt-audio](https://github.com/RijulGulati/yt-audio) - A simple, configurable youtube-dl wrapper to download and manage youtube audio.

## <a name="monitor"></a>System monitoring

* [below](https://github.com/facebookincubator/below) - A time traveling resource monitor for modern Linux systems
* [bpytop](https://github.com/aristocratos/bpytop) - Linux/OSX/FreeBSD resource monitor with a nice interface.
* [Chokidar CLI](https://github.com/open-cli-tools/chokidar-cli) - Fast cross-platform command line utility to watch file system changes.
* [dmidecode](https://www.nongnu.org/dmidecode/) - System information utility.
* [Fastfetch](https://github.com/LinusDierheimer/fastfetch) - Like neofetch, but much faster because written in C.
* [glances](https://nicolargo.github.io/glances/) - A comprehensive and detailed system monitoring tool; monitored parameters include: CPU, memory, load, process list, network interfaces, disk I/O, sensors, filesystems, docker, system info, uptime.
* [htop](http://hisham.hm/htop/) - An interactive process viewer for Unix; improves the UI of `top`, by adding real-time meters and colors.
* [hyperfine](https://github.com/sharkdp/hyperfine) - A command-line benchmarking tool.
* [inxi](http://smxi.org/docs/inxi.htm) - A comprehensive system information script; provides information about CPU, graphics, audio and network devices, drives and partitions, sensors; implemented as a Bash script.
* [iotop](http://guichaz.free.fr/iotop/) - "A Python program with a top like UI used to show of behalf of which process is the I/O going on".
* [lfs](https://github.com/Canop/lfs) - A thing to get information on your mounted disks
* [multitail](https://www.vanheusden.com/multitail/) - A command to open multiple log files in a single terminal window and monitor them in real-time.  
* [neofetch](https://github.com/dylanaraps/neofetch) - Neofetch is a CLI system information tool written in BASH. Neofetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice.
* [ngrep](http://ngrep.sourceforge.net/) - (Network grep) applies the `grep` logic to the network layer, allowing to match regular expressions against data payloads of packets; it recognizes IPv4/6, TCP, UDP, ICMPv4/6, IGMP and Raw across Ethernet, PPP, SLIP, FDDI, Token Ring and null interfaces.
* [noti](https://github.com/variadico/noti) - Monitor a process and trigger a notification.
* [nvitop](https://github.com/XuehaiPan/nvitop) - An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management.
* [PCtrl](https://github.com/MohamedSherifNoureldin/PCtrl) - Robust, featureful, easy-to-use and powerful process manager.
* [powertop](https://01.org/powertop) - A `top`-like utility to monitor the sources of power consumption
* ramfetch - A fetch which displays memory info using /proc/meminfo. * IL LINK SEGNATO DAVA ERRORE 404*
* [screenFetch](https://github.com/KittyKatt/screenFetch) - It can be used to generate one of those nifty terminal theme information + ASCII distribution logos. It auto-detects the distribution and display an ASCII version of that distribution's logo and some valuable information to the right.
* [smem](https://www.selenic.com/smem/) - Python program that reports memory usage; it can report the "proportional set size" (PSS), a meaningful representation of the amount of memory used by libraries and applications in a virtual memory system; it has built-in chart generation.
* [sysdig](https://www.sysdig.org/) - Sysdig captures system calls and events from the Linux kernel.  You can save, filter, and analyze the data with our CLI or our desktop app.  Think of sysdig as strace + tcpdump + htop + iftop + lsof + wireshark for your entire system.
* [The Logfile Navigator](https://lnav.org/) - An advanced and colorful log file viewer with TUI interface.
* [tiptop](https://github.com/nschloe/tiptop) - A command-line system monitoring tool in the spirit of top, written in Python. It displays various interesting system stats and graphs them. Works on all operating systems.
* [top](http://www.unixtop.org/ *ERRORE 404 SUL BROWSER*) - The classical Unix utility that provides a rolling display of top cpu using processes.  
* [ttop](https://github.com/inv2004/ttop) - top-like system monitoring tool with TUI, historical data service and triggers.
* [ttyload](http://www.daveltd.com/src/util/ttyload/) - ttyload is a lightweight utility which is intended to offer a color-coded graph of load averages over time on Linux and other Unix-like systems. It enables a graphical tracking of system load average in a terminal ("tty”).
* [watch](http://www.linfo.org/watch.html) - Periodically runs a command in the console while temporarily clearing the screen content; it makes it easy to check differences between the output of two subsequent commands; it provides "diff" functionality to highlight the changing characters between outputs.
* [watcher](https://github.com/sethigeet/watcher) - Watches all the files present in a directory and whenever a file is changed or a file is created/deleted from the directory, it runs a specified command.
* [whowatch](https://www.tecmint.com/whowatch-monitor-linux-users-and-processes-in-real-time/) - Monitor Linux Users and Processes in Real Time.
* [wtf](https://github.com/wtfutil/wtf) - The personal information dashboard for your terminal.
* [ytop](https://github.com/cjbassi/ytop) - TUI system monitor written in Rust.
* [zfxtop](https://github.com/ssleert/zfxtop) - Self described as “fetch top written by bubbletea enjoyer”.

## <a name="system"></a>System tools

* [active-win-cli](https://github.com/sindresorhus/active-win-cli) - Get the title/id/etc of the active window.
* [asdf](https://asdf-vm.com/) - Manage multiple runtime versions with a single CLI tool.
* [atuin](https://github.com/ellie/atuin) - Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.
* [Bevel](https://github.com/NorfairKing/bevel) - Command line history in an SQLite database for effective re-use.
* [bin](https://github.com/marcosnils/bin) - Manages binary files downloaded from different sources.
* [brightnessctl](https://github.com/Hummer12007/brightnessctl) - Read and control device brightness. Devices, by default, include backlight and LEDs - searched for in corresponding classes.
* [checksum.sh](https://checksum.sh/) - Checksum.sh is a simple way to download, review, and verify install scripts. If the checksum is OK the script will be printed to stdout, which can be piped to sh or elsewhere.
* [cli-tools-info](https://github.com/Lilja/cli-info) - An overview of you CLI tools, if they are installed and what version they are on.
* [conspy](http://conspy.sourceforge.net/) - "Conspy allows a (possibly remote) user to see what is displayed on a Linux virtual console, and send keystrokes to it." 
* [ContainerSSH](https://github.com/ContainerSSH/ContainerSSH) - An SSH Server that Launches Containers in Kubernetes and Docker on demand.
* [Devbox](https://github.com/jetpack-io/devbox) - Devbox is a command-line tool that lets you easily create isolated shells and containers by defining the list of packages required by the environment.
* [docker](https://docs.docker.com/) - Self-sufficient runtime for containers.
* [fkill-cli](https://github.com/sindresorhus/fkill-cli) - Simple cross-platform process killer.
* [has](https://github.com/kdabir/has) - Checks presence of various command line tools on the PATH and reports their installed version.
* [hiSHtory](https://github.com/ddworken/hishtory) - A better shell history that stores context (directory, succeeded or failed, how long it took, etc). The history is stored locally and end-to-end encrypted for syncing to other computers.
* [hstr](https://github.com/dvorka/hstr) - A tool for managing the history
* [hypershell](https://github.com/holepunchto/hypershell) - Spawn shells anywhere. Fully peer-to-peer, authenticated, and end to end encrypted.
* [just](https://github.com/casey/just) - just is a handy way to save and run project-specific commands.
* [lshw](http://www.ezix.org/project/wiki/HardwareLiSter) - A small tool to provide detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc.
* [mackup](https://github.com/lra/mackup) - Keep your application settings in sync (OS X/Linux).
* [mprocs](https://github.com/pvolok/mprocs) - mprocs runs multiple commands in parallel and shows output of each command separately.
* [Mxflow-cli](https://github.com/metaory/mxflow-cli) - A modern, general purpose CLI task runner with human readable yaml config file.
* [nala](https://gitlab.com/volian/nala) - apt package manager front-end with cleaner interface.
* [Ntfy](https://github.com/dschep/ntfy) - Cross-platform Python utility that enables you to automatically get desktop notifications on demand or when long running commands complete. It can as well send push notifications to your phone once a particular command completes.
* [parallel](https://www.gnu.org/software/parallel/) - A shell tool from GNU for executing jobs in parallel using one or more computers
* [procmux](https://github.com/napisani/procmux) - A TUI utility for running multiple commands in parallel in easily switchable terminals.
* [pulsemixer](https://github.com/GeorgeFilipkin/pulsemixer) - CLI and curses mixer for PulseAudio.
* [pypi-command-line](https://github.com/wasi-master/pypi-command-line) - A powerful, colorful, beautiful command-line-interface for pypi.org.
* [sake](https://github.com/alajmo/sake) - A command runner for local and remote hosts. You define servers and tasks in sake.yaml file and then run the tasks on the servers.
* [stew](https://github.com/marwanhawari/stew) - An independent package manager for compiled binaries.
* [sysm](https://github.com/jafarlihi/sysm) - Makes your system play custom sounds when any configured system or external event happens.
* [systeroid](https://github.com/orhun/systeroid) - A more powerful alternative to sysctl(8) with a terminal user interface.
* [task-spooler](http://vicerveza.homeunix.net/~viric/soft/ts/) - A Unix batch system that can be used to add the Linux commands to the queue and execute them one after the other in numerical order (ascending order, to be precise). This can be very useful when you have to run a lots of commands, but you don't want to waste time waiting for one command to finish and run the next command. You can queue it all up and Task Spooler will execute them one by one. In the mean time, you can do other activities.

## <a name="terminal"></a>Terminals

* [byobu](http://byobu.co/) - A text-based window manager and terminal multiplexer; it features enhanced profiles, convenient keybindings, configuration utilities, and toggle-able system status notifications; compatible with `screen` and `tmux`.
* [dtach](https://github.com/crigler/dtach) - A program written in C that emulates the detach feature of screen.
* [mtm](https://github.com/deadpixi/mtm) - Micro Terminal Multiplexer - Simple but usable, stable and minimalistic terminal multiplexer.
* [mx](https://gitlab.com/lpireyn/mx) - A tmux session manager written as a single Bash script.
* [screen](https://www.gnu.org/software/screen/) - Terminal multiplexer that split a physical terminal between several processes, typically interactive shells.
* [Tmate](https://tmate.io/) - A fork of tmux that allows to share the terminal with other users. AFAIK, it connects to a centralized server to establish the connection. Someone may see this inconvenient for privacy issues.
* [tmux](https://tmux.github.io/) - Terminal multiplexer; born to improve `screen`; client-server architecture, `vi` and `emacs` key-bindings, search in window feature and many more.
* [warp](https://github.com/spolu/warp) - Secure and simple terminal sharing.  
* [Zellij](https://github.com/zellij-org/zellij) - A workspace aimed at developers, ops-oriented people and anyone who loves the terminal. At its core, it is a terminal multiplexer.

## <a name="text-processing"></a>Text processing

* [alex](https://github.com/get-alex/alex) - Catch insensitive, inconsiderate writing, by finding gender favoring, polarizing, race related, or other unequal phrasing in text.
* [amber](https://github.com/dalance/amber) - Code search / replace tool.
* [anew](https://github.com/tomnomnom/anew) - Tool for adding new lines to files, skipping duplicates.
* [as-tree](https://github.com/jez/as-tree) - Print a list of paths as a tree of paths.
* [brok](https://github.com/smallhadroncollider/brok) - Find broken links in text documents.
* [ccat](https://github.com/owenthereal/ccat) - A `cat` command with colorized output.  
* [choose](https://github.com/jagprog5/choose) - NCurses based token selector with a nice terminal user interface for selecting tokens. Selecting a line from the bash history is only one of its use cases.
* [csv-diff](https://github.com/simonw/csv-diff) - Python CLI tool and library for diffing CSV and JSON files
* [deadlink](https://github.com/nschloe/deadlink) - Parses text files for HTTP URLs and checks if they are still valid. Good to use on markdown documentation files.
* [delta](https://github.com/dandavison/delta) - A syntax-highlighter for git and diff output.
* [detect-indent-cli](https://github.com/sindresorhus/detect-indent-cli) - Detect the indentation of code.
* [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy) - Make your diffs human readable instead of machine readable.
* [diff2html-cli](https://github.com/rtfpessoa/diff2html-cli) - Parse git diffs as JSON and generate pretty HTML.
* [Difftastic](https://github.com/Wilfred/difftastic) - Syntax-aware structured diff tool.
* [DocToc](https://github.com/thlorenz/doctoc) - Generates table of contents for markdown files inside local git repository. Links are compatible with anchors generated by github or other sites.
* [espanso](https://github.com/espanso/espanso) - Cross-platform Text Expander written in Rust. Not limited to the command line.
* [fullname-cli](https://github.com/sindresorhus/fullname-cli) - Get the fullname of the current user.
* [fzf](https://github.com/junegunn/fzf) - (FuZzy Finder) is a general-purpose command-line finder with fuzzy search/filter capabilities
* [fzy](https://github.com/jhawthorn/fzy) - Better fuzzy finder.
* [grc](https://github.com/pengwynn/grc) - (Generic Colouriser) can be configured to parse a given text stream and to colorize it according to regexp written in configuration files
* [gzip-size-cli](https://github.com/sindresorhus/gzip-size-cli) - Get the gzipped size of a file.
* [HASHA CLI](https://github.com/sindresorhus/hasha-cli) - Hashing made simple. Get the hash of text or stdin.
* [hck](https://github.com/sstadick/hck) - A sharp cut clone.
* [hget](https://github.com/bevacqua/hget) - A CLI to convert HTML into plain text. Can be used to fetch a site's HTML version and convert it into plain text, or to deliver plain text versions of your site dynamically.
* [huniq](https://github.com/koraa/huniq) - Command line utility to remove duplicates from the given input. Note that huniq does not sort the input, it just removes duplicates.
* [kill-tabs](https://github.com/sindresorhus/kill-tabs) - Kill all Chrome tabs to improve performance, decrease battery usage, and save memory.
* [leven-cli](https://github.com/sindresorhus/leven-cli) - Measure the difference between two strings using the Levenshtein distance algorithm.
* [lolcat](https://github.com/busyloop/lolcat) - Ruby Gem to colorize the output of the cat command.
* [lowdown](https://kristaps.bsd.lv/lowdown/) - Markdown translator (HTML5, roff, LaTeX, gemini, OpenDocument, and terminal output)
* [luneta](https://github.com/fbeline/luneta) - Interactive filter that can be easily composed within any script.
* [pdf-diff](https://github.com/serhack/pdf-diff) - A tool for visualizing differences between two pdf files. Mainly dedicated to editors that usually spends a lot of hours on several pdf.
* [percol](https://github.com/mooz/percol) - A Python script that "1) receives input lines from `stdin` or a file, 2) lists the input lines and waits for input that filter/select the line(s), 3) outputs the selected line(s) to `stdout`"; can be used to add interactivity to many regular shell commands.
* [pick](https://github.com/mptre/pick) - Utility that allows users to choose one option from a set of choices using an interface with fuzzy search functionality.  
* [pup](https://github.com/ericchiang/pup) - Parsing HTML at the command line.
* [pv](http://www.ivarch.com/programs/pv.shtml) - The pv command is used to monitor the progress of data through pipe.
* [rare](https://github.com/zix99/rare) - Realtime regex-extraction and aggregation into common formats such as histograms, bar graphs, numerical summaries, tables, and more!
* [sd](https://github.com/chmln/sd) - s[earch] & d[isplace] - An intuitive find & replace CLI
* [skim](https://github.com/lotabout/skim) - Fuzzy Finder in rust.
* [smenu](https://github.com/p-gen/smenu) - Started as a lightweight and flexible terminal menu generator, it evolved into a powerful and versatile CLI selection tool for interactive or scripting use.
* [squeeze](https://github.com/aymericbeaumet/squeeze) - Enables to extract rich information from any text (raw, JSON, HTML, YAML, etc).
* [swordfish-rs](https://github.com/vim-zz/swordfish-rs) - Mimics real person behavior with realtime typing into terminal
* [teip](https://github.com/greymd/teip) - Select partial standard input and replace with the result of another command.
* [to-double-quotes](https://github.com/sindresorhus/to-double-quotes-cli) - Convert matching single-quotes to double-quotes.
* [to-single-quotes](https://github.com/sindresorhus/to-single-quotes-cli) - Convert matching double-quotes to single-quotes.
* [trurl](https://github.com/curl/trurl) - Command line tool for URL parsing and manipulation.
* [tuc](https://github.com/riquito/tuc) - You want to cut on more than just a character, perhaps using negative indexes or format the selected fields as you want... Maybe you want to cut on lines (ever needed to drop first and last line?)... That's where tuc can help.
* [Ultimate Plumber](https://github.com/akavel/up) - Helps to interactively and incrementally explore textual data in Linux, by making it easier to quickly build complex pipelines, thanks to a fast feedback loop.
* [ydiff](https://github.com/ymattw/ydiff) - View colored, incremental diff.

## <a name="text-search"></a>Text search

* [ack](http://beyondgrep.com/) - A tool like `grep` optimized for programmers; written in Perl, it speeds up searches thanks to skipping non interesting directories, such as `.git`.
* [ag](https://github.com/ggreer/the_silver_searcher) - (The silver searcher) is a text search utility targeted to source code; it skips versioning systems data directories; it is inspired by `ack`, but faster.
* [jiq](https://github.com/fiatjaf/jiq) - jid on jq - interactive JSON query tool using jq expressions.
* [paragrep](http://software.clapper.org/paragrep/) - Greps regular expressions in a text file(s) and prints out the paragraphs containing those expressions
* [ripgrep](https://github.com/BurntSushi/ripgrep) - Recursively searches directories for a regex pattern.
* [ripgrep-all](https://github.com/phiresky/ripgrep-all) - grep in text files but also search in PDFs, E-Books, office documents, zip, tar.gz, etc.
* [sift](https://sift-tool.org/) - Fast and powerful open source alternative to grep; it targets flexibility and performance: can be as fast as "regular" grep and allows to specify complex expressions to find text.
* [todocheck](https://github.com/preslavmihaylov/todocheck) - Static code analyzer for annotated TODO comments.
* [ugrep](https://github.com/Genivia/ugrep) - Ultra fast grep with interactive TUI, fuzzy search, boolean queries, hexdumps and more.
* [vgrep](https://github.com/vrothberg/vgrep) - User-friendly pager for grep.

## <a name="todo-manager"></a>Todo managers

* [CLI-Manager](https://github.com/MikyStar/CLI-Manager) - Command Line Interface for managing tasks locally on the fly.
* [devtodo](https://swapoff.org/devtodo.html) - A hierarchical command-line task manager, with data storage in JSON format.
* [Dooit](https://github.com/kraanzu/dooit) - Todo manager with interactive and beautiful UI, and vim keybindings.
* [dstask](https://github.com/naggie/dstask) - Single binary terminal-based TODO manager with git-based sync + markdown notes per task.
* [grit](https://github.com/climech/grit) - A multitree-based personal task manager.
* [iKog](https://sites.google.com/site/henspace/ikog/) - A fully-featured task manager incapsulated within a Python script (just carry around the script to retain all the TODOs). When the script is run, a Python shell is opened, where task-related commands can be entered (ADD, LIST, etc.); a pity that commands are uppercase, which requires the annoying use of the Shift key.
* [mdt](https://github.com/basilioss/mdt) - A simple command-line markdown todo list manager inspired by t.
* [t](https://github.com/sjl/t) - A command-line todo list manager for people that want to finish tasks, not organize them.
* [taskbook](https://github.com/klaudiosinani/taskbook) - Tasks, boards & notes for the command-line habitat.
* [taskell](https://github.com/smallhadroncollider/taskell) - Interactive kanban board/task manager.
* [TaskWarrior](https://taskwarrior.org/) - Todo manager with advanced features
* [td-cli](https://github.com/darrikonn/td-cli) - A command line todo manager, where you can organize and manage your todos across multiple projects.
* [todo.txt](http://todotxt.org/) - Minimalistic todo manager that uses a simple plain text file to keep track of items
* [todolist](http://todolist.site/) - A minimal clone of [Wunderlist](https://www.wunderlist.com/), with 30% of its features. GTD oriented. It stores the task list in a hidden JSON file in the home directory, making it easy to backup or share them.
* [todotxt-machine](https://pypi.org/project/todotxt-machine/) - Interfacce for todo.txt.
* [topydo](https://github.com/topydo/topydo) - A powerful todo list application for the console, using the todo.txt format.
* [tsk](https://github.com/kakengloh/tsk) - Terminal task management app with an emphasis on simplicity, efficiency and ease of use.
* [TuDu](https://code.meskio.net/tudu/) - A comand line interface to manage hierarchical todos.  Each task has a title, a long text description, a deadline (tudu warns you when the date is close), and a scheduled date. There are categories and priorities.
* [Ultralist](https://ultralist.io/) - A simple, powerful, open source task management system for the command line.
* [xit](https://github.com/jotaen/xit) - A plain-text file format for todos and check lists. So, not really a program, but I believe it is worth to list :-)
* [Yokadi](https://yokadi.github.io/) - Project-based todo manager: every task must be specified with a mandatory project indication. Tasks are stored within a SQLlite DB. Written in Python.  

## <a name="torrent"></a>Torrent

BitTorrent clients.

* [Deluge](http://deluge-torrent.org/) - A lightweight, Free Software, cross-platform BitTorrent client; a terminal curses interface, web interface and command line client can connect to a running daemon to manage torrent downloads.
* [Mabel](https://github.com/smmr-software/mabel) - Deriving its name from the Hebrew word ""מבול,"" meaning flood, deluge, or (loosely) torrent, Mabel is a fancy BitTorrent client for the terminal.
* [rtorrent](https://github.com/rakshasa/rtorrent) - Bittorrent client uses ncurses and is ideal for use with tmux, screen or dtach.
* [Stig](https://github.com/rndusr/stig) - Stig is a client application to connect and control the BitTorrent Transmission client app.
* [torrentCLI](https://github.com/amogusussy/torrentCLI) - Get torrents from the Terminal.
* [Transgression TUI](https://github.com/PanAeon/transg-tui) - A remote TUI client for the Transmission bittorrent program.
* [Transmission](https://transmissionbt.com/) - Fast, easy and free bittorrent client.

## <a name="utility"></a>Utilities

* [asciinema](https://github.com/asciinema/asciinema) - Terminal session recorder.
* [ata](https://github.com/rikhuijzer/ata) - Ask the Terminal Anything: OpenAI GPT in the terminal.
* [Autocomplete](https://github.com/withfig/autocomplete) - IDE-style autocomplete for your existing terminal & shell.
* [bash-cache](https://github.com/dimo414/bash-cache) - A function memoisation / caching library for bash scripts and shells
* [bbl](https://github.com/nehemiaharchives/bbl) - Read, search Holy Bible in command line.
* [bible](https://github.com/BibleJS/BibleApp) - Read the Holy Bible via the command line.
* [bkt](https://bkt.rs) - bkt is a subprocess caching utility that makes it easy to reuse past invocations of slow commands
* [chatgpt](https://github.com/mglantz/chatgpt) - Simple command line integration to Chat GPT.
* [cligpt](https://github.com/paij0se/cligpt) - ChatGPT but in the terminal.
* [Cloudcash](https://github.com/mrusme/cloudcash) - Check your cloud spending from the CLI, from Waybar, and from the macOS menu bar!
* [cointop](https://github.com/cointop-sh/cointop) - A fast and lightweight interactive terminal based UI application for tracking cryptocurrencies.
* [dasht](http://sunaku.github.io/dasht/man/man0/README.html) - Search API docs offline, in your terminal or browser.
* [dateutils](http://www.fresse.org/dateutils/) - Dateutils are a bunch of tools that revolve around fiddling with dates and times in the command line with a strong focus on use cases that arise when dealing with large amounts of financial data.
* [flog](https://github.com/mingrammer/flog) - A fake log generator for log formats such as apache-common, apache error and RFC3164 syslog.
* [Gaze](https://github.com/wtetsu/gaze) - Runs a command, right after you save a file.
* [GoTTY](https://github.com/yudai/gotty) - A program to turn CLI tools into web applications; basically, it runs a command and starts a server so that the output can be displayed in a web page.
* [guesswidth](https://github.com/noborus/guesswidth) - Guess the width output without delimiters in commands that output to the terminal.
* [just](https://github.com/casey/just) - Handy way to save and run project-specific commands.
* [Keep](https://github.com/keephq/keep) - Simple alerting tool, with declarative syntax and builtin providers.
* [Lakshmi](https://github.com/sarvjeets/lakshmi) - Investing library and command-line interface inspired by the Bogleheads philosophy.
* [mkdesk](https://gitlab.com/mr-draxs/mkdesk) - A program/command to create .desktop files (program launchers) using the terminal.
* [movie](https://github.com/mayankchd/movie) - A CLI for getting information about a movies and comparing two movies.
* [moviemon](https://github.com/iCHAIT/moviemon) - A Python program that displays all the information about all your movies in the command line.
* [MyTimer](https://github.com/sepandhaghighi/mytimer) - Simple timer for the terminal with timer-mode and alarm.
* [oji](https://github.com/xxczaki/oji) - Interactive text emoji creator.
* [ora](https://github.com/sindresorhus/ora) - Elegant terminal spinner.
* [peaches](https://github.com/KCaverly/peaches) - A smart switcher for the terminal. Based on tmux.
* [pmenu](https://github.com/sgtpep/pmenu) - A dynamic terminal-based menu inspired by dmenu.
* [powerline](https://github.com/powerline/powerline) - Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile.
* [Python re(gex)? exercises](https://github.com/learnbyexample/TUI-apps/tree/main/PyRegexExercises) - TUI application intended to help you practice Python regular expressions
* [rofi](https://github.com/davatorium/rofi) - A window switcher, application launcher and dmenu replacement.
* [rss-cli](https://github.com/Clortox/rss-cli) - A unix-inspired cli application for interacting with RSS feeds.
* [sauce](https://github.com/cadecuddy/sauce) - A novelty CLI tool that identifies an anime from an image and yields key data about it.
* [shmenu](https://github.com/duclos-cavalcanti/shmenu) - Menu TUI tool written solely in bash.
* [Skylab](https://github.com/SerhiiStets/skylab) - A text user interface (TUI) tool that displays upcoming space launches in a user-friendly way.
* [sshto](https://github.com/vaniacer/sshto) - Small bash script to manage your ssh connections. It builds menu (via dialog) from your ~/.ssh/config. It can not only connect but also to run commands, copy files, tunnel ports.
* [Starship](https://starship.rs/) - The cross-shell prompt for astronauts.
* [teetail](https://github.com/sl236/teetail) - Like tee, but only the tail goes in the file.
* [termsaver](http://termsaver.brunobraga.net/) - termsaver to enjoy fancy ASCII screensavers like matrix, clock, starwars, and a couple of not-safe-for-work screens.
* [ttyscheme](https://github.com/kolunmi/ttyscheme) - Collection of Color Schemes for the TTY.
* [unix-permissions](https://github.com/ehmicky/unix-permissions) - Swiss Army knife for Unix permissions.
* [upnup](https://github.com/tomit4/upnup) - A command line utility that generates a LICENSE file in the current working directory.
* [Viddy](https://github.com/sachaos/viddy) - Modern watch command. Time machine and pager etc.
* [weather-cli](https://github.com/riyadhalnur/weather-cli) - Check the weather for your city from the terminal.
* [welcome.sh](https://github.com/G2-Games/welcome.sh) - A nice little script that greets you on every launch, with some helpful (and customizable!) information.
* [yank](https://github.com/mptre/yank) - Reads input from stdin and display a selection interface that allows a field to be selected and copied to the clipboard.

## <a name="versioning"></a>Versioning

* [Bazaar](http://bazaar.canonical.com/en/) - Multiplatform version control system supporting diffferent workflows; it is part of the GNU Project, and it is free software sponsored by Canonical.
* [fossil](https://fossil-scm.org/) - A simple, high-reliability, distributed software configuration management system with these advanced features: project management, built-in web interface, friendly self-hosting, simple networking, all-in-one standalone executable, and much more.
* [gee](https://github.com/human37/gee) - CLI repository manager and automation tool written in rust.
* [Gistup](https://github.com/mbostock/gistup) - Create a gist from terminal, then use git to update it.
* [Mercurial](https://www.mercurial-scm.org/) - Free, distributed source control management tool.
* [SnowFS](https://github.com/snowtrack/snowfs) - A high-performance application and node library for binary file versioning, initially made for the graphics industry.

## <a name="viewers"></a>Viewers

* [baca](https://github.com/wustho/baca) - Lets you indulge in your favorite e-books in the comfort of your terminal.
* [bat](https://github.com/sharkdp/bat) - A cat clone with syntax highlighting and Git integration.
* [cacaview](http://caca.zoy.org/wiki/libcaca) - A library and a program to display JPG, PNG, GIF or BMP images in the terminal using ASCII characters.
* [Canto Curses](https://github.com/themoken/canto-curses) - Curses frontend for [Canto daemon](https://github.com/themoken/canto-next) for RSS feeds.
* [feh](https://feh.finalrewind.org/) - "X11 image viewer aimed mostly at console users" (cit.); with no fancy GUI, it is controlled via commandline arguments and configurable key/mouse actions.
* [fx](https://github.com/antonmedv/fx) - Command-line JSON viewer.
* [glow](https://github.com/charmbracelet/glow) - Render markdown on the CLI, with pizzazz!
* [Grip](https://github.com/joeyespo/grip) - GitHub Readme Instant Preview - Preview markdown files as GitHub would render them.
* [haxor-news](https://github.com/donnemartin/haxor-news) - Browse Hacker News like a haxor: A Hacker News command line interface (CLI).
* [hexyl](https://github.com/sharkdp/hexyl) - Command-line hex viewer.
* [jc](https://github.com/kellyjonbrazil/jc) - Serializes the output of command line tools to JSON.
* [jless](https://pauljuliusmartinez.github.io/) - Command-line JSON viewer designed for reading, exploring, and searching through JSON data.
* [jqview](https://github.com/fiatjaf/jqview) - Simplest possible native GUI for inspecting JSON.
* [mdcat](https://github.com/swsnr/mdcat) - cat for Markdown
* [mdt](https://github.com/robolab-pavia/mdt) - MarkDown in the Terminal. A markdown viewer with themes defined by JSON files and interactive mode to open links and word-wrapping adaptable to the terminal width.
* [medium-cli](https://github.com/djadmin/medium-cli) - Medium for Hackers - Read [medium.com](https://medium.com/) stories in the terminal.
* [mplayer](http://www.mplayerhq.hu/design7/news.html) - One of the most popular video/audio players around
* [mpv](https://mpv.io/) - A cross-platform media player with many features such as frame timing, MKV chapters and subtitles. It is a responsive video player with minimal layout customizable with themes. A good alternative media player to VLC since it can handle almost all the media formats as VLC, but using much less resources.
* [Newsbeuter](http://newsbeuter.org/) - "The Mutt of RSS Feed Readers": Newsbeuter is an open-source RSS/Atom feed reader for text terminals. Has great configurability and vast number of features, making it a slick and fast feed reader that can be completely controlled via keyboard.
* [Newsboat](https://newsboat.org/) - An RSS/Atom feed reader for the text console. It's an actively maintained fork of Newsbeuter.
* [nom](https://github.com/guyfedwards/nom) - RSS reader for the terminal.
* [ov](https://github.com/noborus/ov) - Feature-rich terminal-based text viewer.
* [reader](https://github.com/mrusme/reader) - Reader parses a web page for its actual content and displays it in nicely highlighted text on the command line
* [rReader](https://github.com/rainygirl/rreader) - RSS reader client with TUI interface.
* [tabview](https://github.com/TabViewer/tabview) - Python curses command line CSV and tabular data viewer.
* [Terminal Markdown Viewer](https://github.com/axiros/terminal_markdown_viewer) - Python based Markdown viewer for the terminal.
* [TerminalImageViewer](https://github.com/stefanhaustein/TerminalImageViewer) - Small C++ program to display images in a (modern) terminal using RGB ANSI codes and unicode block graphics characters.
* [termv](https://github.com/Roshan-R/termv) - A terminal iptv player written in bash.
* [texel](https://github.com/Lauriat/texel) - Command line interface for reading spreadsheets inside terminal.
* [Textual Markdown Browser](https://github.com/willmcgugan/textual-markdown) - Experimental "Markdown browser" for the terminal, built with Textual.
* [TubiTui](https://codeberg.org/777/TubiTui.git) - A lightweight, libre, TUI-based YouTube client
* [TV](https://github.com/alexhallam/tv) - Cross-platform CSV pretty printer made to maximize viewer enjoyment.
* [viu](https://github.com/learn-anything/command-line-tools) - Command-line application to view images from the terminal written in Rust.
* [vj](https://github.com/busyloop/vj) - JSON Humanizer makes JSON human readable by applying visual formatting.
* [youtube-tui](https://github.com/Siriusmart/youtube-tui) - An aesthetically pleasing YouTube TUI
* [youtube-viewer](https://github.com/trizen/youtube-viewer) - Lightweight application that searches and streams videos from YouTube.

## <a name="browser"></a>Web browser

* [Amfora](https://github.com/makew0rld/amfora) - Amfora aims to be the best looking Gemini client with the most features. It does not support Gopher or other non-Web protocols.
* [asuka](https://git.sr.ht/~julienxx/asuka) - A Gemini Project client written in Rust with NCurses.
* [Bombadillo](https://bombadillo.colorfield.space/) - A non-web browser, designed for a growing list of protocols operating outside of the web. Currently supports Gemini, Finger and Gopher.
* [browsh](https://www.brow.sh/) - It renders anything that a modern browser can; HTML5, CSS3, JS, video and even WebGL. Its main purpose is to be run on a remote server and accessed via SSH/Mosh or the in-browser HTML service in order to significantly reduce bandwidth and thus both increase browsing speeds and decrease bandwidth costs.
* [cli-arxiv](https://github.com/knguyenanhoa/cli-arxiv) - CLI tool for exploring arXiv.
* [Elinks](http://elinks.cz/) - "Advanced and well-established feature-rich text mode web browser"; started as a fork of `Links`; it supports background download with queueing, some support from CSS, text box editing in external text editor.
* [gplaces](https://github.com/dimkr/gplaces) - Simple but powerful terminal Gemini client.
* [Graphene](https://github.com/atsepkov/Graphene) - A text-based web browser that's a joy to use.
* [Gremlin](https://github.com/actuday6418/gremlin) - Gemini browser for the terminal.
* [Links](http://www.jikos.cz/~mikulas/links//) - A textual Web browser with tables and frames.  
* [Lynx](http://lynx.invisible-island.net/) - A highly configurable text-based web browser
* [min](https://github.com/a-h/min) - A Gemini browser with Vim style keyboard navigation, client certificate support and history and bookmarks saved in TSV files.
* [Romulus](https://github.com/LukeEmmet/Romulus) - A cross platform Gemini console client in C# with a simple user interface, interactive menus and mouse support.
* [s](https://github.com/zquestz/s) - Web search from the terminal. Just opens in your browser.
* [Telescope](https://telescope.omarpolo.com/) - Gemini client with UI that is strongly inspired from Emacs and W3M.
* [w3m](http://w3m.sourceforge.net/) - A text-based web browser as well as a pager like `less`

## <a name="webdev"></a>Web development

Static site generators, load test tools..

* [ain](https://github.com/jonaslu/ain) - An HTTP API client for the terminal.
* [crawley](https://github.com/s0rg/crawley) - Unix-way web crawler: crawls web pages and prints any link it can find.
* [Discharge](https://github.com/brandonweiss/discharge) - Deploy static websites to Amazon S3.
* [http-tanker](https://github.com/PierreKieffer/http-tanker) - Terminal application used for API testing; easily create, manage and execute http requests from the terminal.
* [HTTPie](https://github.com/httpie/httpie) - HTTPie for Terminal: human-friendly CLI HTTP client for the API era.
* [Hugo](https://gohugo.io/) - The world's fastest framework for building websites.
* [iola](https://github.com/pvarentsov/iola) - A command-line socket client with REST API. It helps to work with socket servers using your favorite REST client.
* [is-up-cli](https://github.com/sindresorhus/is-up-cli) - Check whether a website is up or down using the [isitup.org](https://isitup.org/) API.
* [linkchecker](https://github.com/linkchecker/linkchecker) - Check links in web documents or full websites.
* [lychee](https://github.com/lycheeverse/lychee) - Fast, async, resource-friendly link checker written in Rust.
* [Metalsmith](http://www.metalsmith.io/) - An extremely simple static site generator
* [Mycorrhiza Wiki](https://mycorrhiza.wiki/) - A lightweight file-system wiki engine that uses Git for keeping history.
* [nanoc](http://nanoc.ws/) - Static site generator written in Ruby
* [pageres-cli](https://github.com/sindresorhus/pageres-cli) - Capture screenshots of websites in various resolutions. A good way to make sure your websites are responsive.
* [Reachable](https://github.com/italolelis/reachable) - Check if a domain is up.
* [s3cmd](https://github.com/s3tools/s3cmd) - Command line tool for managing Amazon S3 and CloudFront services.
* [siege](https://www.joedog.org/siege-home/) - An http load testing and benchmarking utility designed to let web developers stress their code.  
* [snallygaster](https://github.com/hannob/snallygaster) - Tool to scan for secret files on HTTP servers.
* [surge](https://surge.sh) - Static web publishing on surge.sh CDN.
* [Tsung](http://tsung.erlang-projects.org/) - A multi-protocol distributed load testing tool that can be used to stress HTTP, WebDAV, SOAP, PostgreSQL, MySQL, LDAP and Jabber/XMPP servers.
* [urlhunter](https://github.com/utkusen/urlhunter) - Recon tool that allows searching on URLs that are exposed via shortener services.
* [xpe](https://github.com/charmparticle/xpe) - A commandline xpath tool that is easy to use.


# <a name="resources"></a>Related resources

A list of some online resoures that contribute interesting links to apps and info.

[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) - A wonderful summary from Joshua Levy regarding command line (Bash in particular) tools, programs, tips and tricks; contains many pointers to resources and repositories, in the form of "to do this you must know that", which gives great pointers but requires further investigation from different sources; translated in many languages.

[Inconsolation blog](https://inconsolation.wordpress.com/) - "Adventures with lightweight and minimalist software for Linux": reviews of many command-line programs; many programs reviewed (400+, at least), with screenshots and animated GIFs; the style of presentation is ironic and funny, but requires some effort to figure out the real contribution of a program.

[A little collection of cool unix terminal/console/curses tools](https://kkovacs.eu/cool-but-obscure-unix-tools) - "Some are little-known, some are just too useful to miss, some are pure obscure..." from Kristof Kovacs; nice list with screenshot; mostly oriented to system administration; unfortunately there are no clickable links.

[Caleb Xu shell awesome](https://github.com/alebcay/awesome-shell) - Focused on UNIX shell tools.

[Adam Harris awesome CLI apps](https://github.com/aharris88/awesome-cli-apps) - Nice list of tools; somehow too much Javascript/Node.js-centered for my tastes.

[Marcel Bischoff awesome commandd line apps](https://github.com/herrbischoff/awesome-command-line-apps) - Nice up-to-date list of useful tools.

[Awesome CLI by sintaxi](https://github.com/sintaxi/awesome-cli) - Relatively short list with short descriptions; with some original entries.

[awesome-ttygames](https://ligurio.github.io/awesome-ttygames/) - Large awesome list of terminal games. The collection is maintained in a YAML format. Each item contains a description and an optional screencast.

[Site Generators](https://jamstack.org/generators/) - A comprehensive list of Static Site Generators.

[Awesome git addons](https://github.com/stevemao/awesome-git-addons) - A curated list of add-ons that extend/enhance the git CLI.

[Terminals Are Sexy](https://github.com/k4m4/terminals-are-sexy) - A curated list of Terminal frameworks, plugins & resources for CLI lovers.



