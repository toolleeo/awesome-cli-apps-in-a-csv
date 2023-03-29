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

To date, **883** apps/tools covered, organized in **45** categories.

# Index

[Backup](#backup) (9) | [Calculators](#calc) (9) | [Chat and instant messaging](#chat) (12) | [Commands cheatsheet and snippets](#cheatsheet) (15) | [Conversion](#conversion) (7) | [Data management](#data-management) (38) | [Data transfer](#transfer) (32) | [Directory changers](#cd) (13) | [Disk usage analyzers](#disk-analyzer) (12) | [Editors](#editors) (23) | [Email](#email) (11) | [File and file system handling](#file-handling) (42) | [File manager](#file-manager) (12) | [File renamers](#file-renamer) (11) | [File systems](#file-system) (4) | [Font management](#font) (2) | [Funny tools](#funny) (25) | [Games](#games) (37) | [Git and accessories](#git) (31) | [Graphics](#graphics) (26) | [Multimedia](#multimedia) (7) | [Networking](#networking) (23) | [Note taking](#note-taking) (16) | [Office tools](#office) (17) | [Organizers and calendars](#organizers) (17) | [Online search and resources](#online) (10) | [Password managers](#password-manager) (14) | [Productivity](#productivity) (37) | [Programming](#programming) (33) | [Science](#science) (10) | [Security and encryption](#security) (20) | [Shells](#shells) (8) | [Sound and music](#music) (26) | [System monitoring](#monitor) (32) | [System tools](#system) (32) | [Terminals](#terminal) (9) | [Text processing](#text-processing) (44) | [Text search](#text-search) (10) | [Todo managers](#todo-manager) (21) | [Torrent](#torrent) (7) | [Utilities](#utility) (44) | [Versioning](#versioning) (6) | [Viewers](#viewers) (31) | [Web browser](#browser) (16) | [Web development](#webdev) (22)

Some links to [related resources](#resources).

## <a name="backup"></a>Backup

* [borg]() - Encrypted backups with a clean and simple interface; easy to use and set up; possibility to mount the backup archive with FUSE and inspect it as a regular file system.  
* [bupstash]() - Easy and efficient encrypted backups.
* [duplicity](https://gitlab.com/duplicity/duplicity) - Creates GPG encrypted, compressed backups; client-side encryption allows to upload the backup onto untrusted servers.
* [Duply](https://sourceforge.net/projects/ftplicity/) - Simplifies the use of [duplicity](http://duplicity.nongnu.org/) by keeping clean configuration files to automate the backup.  
* [paperbackup]() - Create a pdf with barcodes to backup text files on paper.
* [shallow-backup]() - Git integrated backup tool.
* [thread-safe]() - Keep your favorite Twitter threads safe with a local copy.
* [Zaloha.sh]() - Shellscript for synchronization of files and directories.
* [zbackup](https://github.com/zbackup/zbackup) - A globally-deduplicating backup tool, based on the ideas found in rsync.

## <a name="calc"></a>Calculators

Calculators for numbers, dates, etc..

* [bcal]() - Byte CALculator - A REPL CLI utility for storage expression evaluation, SI/IEC conversion, byte address calculation, base conversion and LBA/CHS calculation.
* [Bitwise]() - Base conversion and bit manipulator in ncurses.
* [cash-cli]() - Convert Currency Rates.
* [kalk]() - Command line calculator that supports math-like syntax with user-defined variables, functions, derivation, integration, and complex numbers.
* [mdlt]() - A lightweight command line tool that lets you perform arithmetic and symbolic math operations right from the terminal.
* [Nota](https://github.com/pouyakary/Nota) - Terminal calculator with rich notation.
* [pdd]() - Tiny date, time diff calculator.
* [Programmer calculator]() - Terminal calculator made for programmers working with multiple number representations, sizes, and overall close to the bits.
* [Qalculate](https://github.com/Qalculate/libqalculate) - Multi-purpose calculator with customizable functions, units, arbitrary precision, plotting (it includes a GUI).

## <a name="chat"></a>Chat and instant messaging

* [finch]() - IM program supporting many protocols, including Yahoo!, AIM, IRC, or WLM; comes with the `Pidgin` project.
* [irssi](https://github.com/irssi/irssi) - The most popular IRC client for the command-line; a flexible program, with many options and supporting many protocols.
* [kirc](https://github.com/mcpcpc/kirc) - A tiny IRC client written in POSIX C99.
* [matterhorn]() - A terminal client for the Mattermost chat system.
* [PingMe]() - Sends messages or alerts to multiple messaging platforms & email, including Slack, Telegram, Mattermost, WeChat and others.
* [RainbowStream]() - Twitter client for the terminal; allows almost all the operations that can be done from GUI and Web clients.
* [ssh-chat]() - Custom SSH server written in Go. Instead of a shell, you get a chat prompt.
* [tiny]() - tiny is an IRC client written in Rust.
* [ttchat]() - Twitch chats in the terminal.
* [tuir]() - Reddit TUI.
* [tweets]() - Decentralized alternative to twitter that uses git as support tool to manage the tweets.
* [WeeChat](https://github.com/weechat/weechat) - A "fast, light and extensible chat client".

## <a name="cheatsheet"></a>Commands cheatsheet and snippets

Tools to manage often used commands, code snippets, cheatsheets and alternative manpages.

* [AI]() - A commandline ChatGPT client in BASH with conversation/completion support.
* [aido-cli]() - Looks another interface to online GPT models to execute command through natural language. Very poor documentation and readme, though.
* [Commandpilot]() - An assistant which uses ChatGPT to aid in constructing commands for bash.
* [eg]() - Useful examples at the command line.
* [ehh]() - Command-line tool for remembering linux/terminal commands.
* [gpt-do]() - This is a handy-dandy CLI for when you don't know wtf to do; instead of furiously grepping through man pages, simply use do (or ddo if on bash/zsh), and have GPT-3 do all the magic for you.
* [kmdr-cli]() - The CLI tool for explaining commands from your terminal.
* [MUC]() - Visualize your most used commands.
* [Nap]() - Code snippet manager that allows to create and access new snippets quickly with the command-line interface or browse, manage, and organize them with the text-user interface.
* [navi]() - An interactive cheatsheet tool for the command-line.
* [tealdeer]() - Very fast implementation of tldr in Rust.
* [The Fuck]() - Magnificent app which corrects your previous console command (although I would be extra-cautious at making a program to automatically infer what I was intending).
* [tldr](https://github.com/tldr-pages/tldr) - Client for tldr pages, a community effort to simplify the beloved man pages with practical examples.
* [topalias]() - Linux alias generator from bash/zsh command history with statistics, written on Python.
* [Wat]() - Instant, central, community-built docs.

## <a name="conversion"></a>Conversion

File format converters.

* [BaFi](https://github.com/mmalcek/bafi) - Universal JSON, BSON, YAML, CSV, XML translator to ANY format using templates.
* [catdoc](http://www.wagner.pp.ru/gitweb/?p=oss/catdoc.git) - Command line converter from Microsoft Word to plain text; output is sent to the standard output.  
* [mdBook]() - Create book from markdown files.
* [NestedTextTo]() - CLI to convert between NestedText and JSON, YAML, or TOML.
* [Pandoc](https://github.com/jgm/pandoc) - Universal document file converter; handles input output from/to a number of formats: HTML, PDF, LaTeX, docx, odt, AsciiDoc, Markdown, Textile, just to mention a few; the quality of conversion strongly depends on the combination of input/output formats.
* [simtex]() - simtex (simplified LaTeX) allows you to convert your markdown or text lectures into LaTeX file with one command, configured with simple .json file.
* [xls2csv](http://www.wagner.pp.ru/gitweb/?p=oss/catdoc.git) - Command line converter from Excel to CSV file format.  

## <a name="data-management"></a>Data management

* [crudini]() - A utility for manipulating ini files.
* [csvkit]() - A suite of command-line tools for converting to and working with CSV, the king of tabular file formats.
* [csvq]() - SQL-like query language for csv.
* [csvtk](https://github.com/shenwei356/csvtk/) - A cross-platform, efficient and practical CSV/TSV toolkit written in Go.
* [dasel]() - Allows you to query and modify data structures using selector strings.
* [datadash]() - Visualize and graph data in the terminal.
* [datasetGPT]() - A command-line interface and a Python library for inferencing Large Language Models to generate textual datasets.
* [Dolt]() - Dolt is Git for Data! Dolt is a SQL database that you can fork, clone, branch, merge, push and pull just like a git repository.
* [GNU Recutils]() - Set of tools and libraries to access human-editable, text-based databases called recfiles.
* [gnuplot](https://github.com/idank/explainshell) - Generate two and three dimensional plots of data.
* [gojq]() - Pure Go implementation of jq.
* [Graphtage]() - Graphtage is a commandline utility and underlying library for semantically comparing and merging tree-like structures, such as JSON, XML, HTML, YAML, plist, and CSS files.
* [GROQ]() - The CLI tool consumes both JSON and NDJSON documents. You can pass in data from a local file, or from piping to standard input.
* [IRedis]() - Interactive Redis: A Cli for Redis with AutoCompletion and Syntax Highlighting.
* [jp]() - A tiny commandline tool for parsing JSON from any source.
* [jq](https://github.com/stedolan/jq) - (JSON Query?) is sed-like processor for JSON data; can be used to process JSON files and data streams and perform operations such as those allowed by `cat`, `sed`, `grep` and `awk` on regular text files.
* [jqp]() - A TUI playground for exploring jq.
* [jtc]() - JSON manipulation and transformation.
* [lowcharts]() - lowcharts is meant to be used in those scenarios where we have numerical data in text files that we want to display in the terminal to do a basic analysis.
* [Miller]() - Miller is like awk, sed, cut, join, and sort for data formats such as CSV, TSV, JSON, JSON Lines, and positionally-indexed.
* [mycli]() - A command line client for MySQL that can do auto-completion and syntax highlighting.
* [osmf]() - OpenStreetMap find - A simple command line tool to explore OSM data.
* [pgcli]() - Postgres CLI with autocompletion and syntax highlighting.
* [q](https://github.com/harelba/q) - Executes SQL-like queries on CSVs/TSVs tabular data files; each tabular file is treated as a database table; support to all SQL constructs (`WHERE`, `GROUP BY`, `JOIN`).
* [ramda-cli]() - A tool for processing data with functional pipelines.
* [Redis Viewer]() - A tool to view redis data in terminal.
* [ROAPI]() - ROAPI automatically spins up read-only APIs for static datasets without requiring you to write a single line of code.
* [Soul]() - A SQLite REST and realtime server.
* [sq]() - Command line tool that provides jq-style access to structured data sources such as SQL databases, or document formats like CSV or Excel.
* [termdbms]() - A TUI for viewing and editing databases, written in pure Go.
* [TSV Utilities]() - Command line tools for large, tabular data files.
* [underscore-cli]() - Command-line utility-belt for hacking JSON and Javascript.
* [usql]() - Universal command-line interface for PostgreSQL, MySQL, Oracle Database, SQLite3, Microsoft SQL Server, and others, including NoSQL and non-relational databases.
* [VisiData](https://github.com/saulpw/visidata) - Interactive multitool for tabular data. It combines the clarity of a spreadsheet, the efficiency of the terminal, and the power of Python, into a lightweight utility which can handle millions of rows with ease.
* [WOPR]() - A simple markup language for creating rich terminal reports, presentations and infographic.
* [xsv]() - Doing a SQL join with CSV files.
* [yq]() - Portable command-line YAML processor.
* [zq](https://github.com/brimdata/zed) - Processor for JSON data with stateful operators and a syntax that is more consistent w.r.t. jq (as claimed by the authors).

## <a name="transfer"></a>Data transfer

* [aria2]() - Lightweight and easy-to-use download utility; it supports HTTP/HTTPS, FTP, SFTP, BitTorrent, Metalink and multiple sources; cross-platform.
* [Clipsync]() - Share your clipboard across multiple machines using an MQTT service.
* [croc]() - Easily and securely send things from one computer to another.
* [curl](https://github.com/curl/curl) - A tool and library for transferring data with URL syntax; supports a lot of protocols.  
* [feuille]() - A fast, dead-simple socket-based pastebin.
* [ffsend]() - Easily and securely share files from the command line. A fully featured Firefox Send client.
* [Jitter]() - A repository-oriented binary manager for Linux, Jitter searches through online repository (currently only on GitHub) for releases with .tar.gz, .tgz, .zip or .AppImage assets.
* [lftp](https://github.com/lavv17/lftp) - "Sophisticated ftp/http client, and a file transfer program supporting a number of network protocols"; support for bookmarks and mirroring features.
* [Magic Wormhole]() - The program allows transfer arbitrary-sized files and directories (or short pieces of text) from one computer to another The two endpoints are identified by using identical human-readable codes.  
* [Nextcloud share URL downloader]() - Download files from and list content of NextCloud (password protected) share directly from the command line without needing a webbrowser.
* [OnionShare](https://github.com/onionshare/onionshare) - "An open source tool that lets you securely and anonymously share a file of any size." 
* [pbgopy]() - Copy and paste between devices.
* [pbproxy]() - Send your clipboard anywhere you can ssh to.
* [portal]() - A quick and easy command-line file transfer utility from any computer to another.
* [qr-filetransfer]() - Transfer files over WiFi between your computer and your smartphone from the terminal.
* [qrcp](https://github.com/claudiodangelis/qrcp) - Transfer Files Between Desktop And Mobile Devices Over Wi-Fi By Scanning A QR Code.
* [rclone](https://github.com/rclone/rclone) - Rclone manages file synchronization on cloud storage.
* [rclone-tui]() - Cross-platform manager for rclone, which aims to be on-par with the web GUI.
* [rsync](https://github.com/WayneD/rsync) - Mirror directories across networked machines; handles diffs/changed files; works across SSH; plenty of parameters.  
* [sharing]() - Sharing is a command-line tool to share directories and files from the CLI to iOS and Android devices without the need of an extra client app.
* [shcopy]() - Copy text to your system clipboard locally and remotely using ANSI OSC52 sequence.
* [sitecopy]() - Synchronizes a local copy of a website with a remote copy on a server; does not use SSH/`scp` but FTP for file copy; useful when the remote server does not support secure copy.  
* [stftp](https://sourceforge.net/projects/stftp/) - (simple terminal FTP) aims to be a "easy-to-use and unbloated client for the UNIX (and UNIX-like) console".
* [tran]() - Securely transfer and send anything between computers with TUI.
* [Unison](https://github.com/bcpierce00/unison) - File synchronizer. It allows two replicas of a collection of files and directories to be stored on different hosts (or different disks on the same host), modified separately, and then brought up to date by propagating the changes in each replica to the other.
* [Woof](https://github.com/simon-budig/woof/) - (Web Offer One File) sets up an HTTP webserver to serve files from a given local directory; all the users connected to the network can see and download the files.  
* [xh]() - xh is a friendly and fast tool for sending HTTP requests. It reimplements as much as possible of HTTPie's excellent design.
* [Yark]() - YouTube archiving made simple.
* [youtube-dl]() - Downloads videos from [YouTube](https://www.youtube.com/) and some other sites; useful for automated bulk downloads.  
* [yt-splitter]() - Downloads and splits audio tracks from a YouTube video according to the chapters/tracks. Useful for compilations or full album uploads.
* [ytfzf]() - A POSIX script that helps you find Youtube videos (without API) and opens/downloads them using mpv/youtube-dl.
* [ytmdl]() - Get songs from Youtube in mp3 format.

## <a name="cd"></a>Directory changers

Tools for improving the efficiency of directory traversal.

* [autojump]() - A cd command that learns - easily navigate directories from the command line.
* [broot](https://github.com/Canop/broot) - A new way to navigate directory trees on linux, made in rust.
* [fasd]() - A Commandline Tool That Offers Quick Access to Files and Directories. It offers quick access to files and directories for POSIX shells.  It is inspired by tools like autojump, z and v. Fasd keeps track of files and directories you have accessed, so that you can quickly reference them in the command line.
* [fastdiract]() - Lightning-fast cd and command execution.
* [fz]() - Fuzzy tab completion for z.
* [Jmp]() - Change directory with smart searching of the path specified through regex.
* [llama]() - Minimalistic file opener and directory changer focused on fuzzy searching the path.
* [pazi]() - Fast autojump helper.
* [pm]() - The easy way to switch between your projects on ZSH. In short, another directory changer.
* [SmartCd]() - A cd command with improved usability features, which can remember your recently visited directory paths and, search and directly traverse to sub-directories and as well as parent directories, all with Fuzzy searching.
* [z]() - Directory changer based on aging and frecency.
* [z.lua]() - Directory changer that learns your habits.
* [zoxide]() - A faster way to navigate your filesystem.

## <a name="disk-analyzer"></a>Disk usage analyzers

* [cdu]() - cdu (colored `du`) is a perl script that calls `du` and displays a pretty histogram with optional colors allowing to immediately see the directories which take most disk space.
* [dfc]() - Report file system space usage information with style.
* [diskonaut]() - Terminal disk space navigator that traverse the file-system with a TUI interface.
* [diskus]() - Minimal, fast alternative to du -sh.
* [dua]() - Disk Usage Analyzer. Learn about the usage of disk space of a given directory with parallel access to max out SSD exploration.
* [duf]() - Disk Usage/Free Utility.
* [Dust]() - du + rust = dust. Like du but more intuitive.
* [dutree]() - A tool to analyze file system usage written in Rust.
* [erdtree]() - A multi-threaded file-tree visualizer and disk usage analyzer.
* [gdu]() - Pretty fast disk usage analyzer written in Go. Gdu is intended primarily for SSD disks where it can fully utilize parallel processing. However HDDs work as well, but the performance gain is not so huge.
* [ncdu](https://code.blicky.net/yorhel/ncdu/) - "A disk usage analyzer with an ncurses interface.  It is designed to find space hogs on a remote server where you don't have an entire graphical setup available."
* [vizex]() - Visualize the disk space usage for every partition and media on the user's machine.

## <a name="editors"></a>Editors

Terminal text editors.

* [ash]() - A simple and clean terminal-based text editor, that aims to be easy to use with modern key-bindings.
* [Diakonos]() - A powerful editor with “standard” keybindings and several advanced features; written in Ruby.
* [Emacs](http://git.savannah.gnu.org/cgit/emacs.git) - One of the godfathers of text editors; free long-standing software project; tons of extensions and funcionalities; the biggest drawback (my taste): it needs [E-Lisp](https://www.gnu.org/software/emacs/manual/eintr.html) for being programmed.  
* [eon]() - A light, modern editor for your terminal that doesn't want to be vim.
* [Feather](https://github.com/0xBaca/FeatherEditor) - The only terminal based text editor designed to work with BIG files.
* [Helix]() - A kakoune / neovim inspired editor, written in Rust. The editing model is very heavily based on kakoune.
* [jed](https://github.com/jedsoft/jed) - A text editor with a drop-down menu facility that make it especially user-friendly.  
* [joe](https://sourceforge.net/projects/joe-editor/) - (Joe's Own Editor) is a compact text editor written in C; a detailed list of features and missing ones is explicitly reported in the website; this editor is mentioned in several web sources for its capability in handling large files.  
* [Kakoune](https://github.com/mawww/kakoune) - Modal editor, faster as in less keystrokes, multiple selections, orthogonal design.
* [micro]() - A terminal-based text editor written in Go that aims to be easy to use and intuitive, while also taking advantage of the full capabilities of modern terminals.
* [nano](https://git.savannah.gnu.org/cgit/nano.git/log/) - Easy to use, lightweigth text editor; no complex keybindings to remember.
* [neovim](https://github.com/neovim/neovim) - A work in progress attempt to improve [vim](http://www.vim.org/), dropping older/unused OS compatibility, improving the codebase readability, modularity and maintainability; it has chances to become the next choice of vim users.
* [o]() - Configuration-free text editor and IDE limited to VT100. Suitable for writing git commit messages, editing Markdown, config files, source code, viewing man pages and for quick edit-compile cycles when programming.
* [pickaxe]() - The redmine wiki editor.
* [slap]() - Text editor inspired by [Sublime Text](https://www.sublimetext.com/) written in NodeJS; extedable in Javascript.  
* [Tilde](https://github.com/gphalkes/tilde) - Tilde is a text editor that provides an intuitive interface for people accustomed to GUI environments, usual shortcuts for common operation, a traditional menu bar, etc.
* [vai]() - A text editor similar to `vim` written in Python; many feature are nicely replicated, some are still missing; however, the advantage of this implementation is its simplicity, maintainability and extensibility, thanks to the Python implementation.
* [VE]() - Lean, fast and feature rich text editor.
* [vim](https://github.com/vim/vim) - Historically one of the preferred text editors; behavior based on editing modes; plenty of plugins and tips to address every possible editing problem.  
* [vis]() - "a modern, legacy free, simple yet efficient vim-like editor", and more: "The intention is not to be bug for bug compatible with vim, instead a similar editing experience should be provided. The goal could thus be summarized as 80% of vim's features implemented in roughly 1% of the code"; the editor is scriptable in LUA and supports editing large files.
* [vy]() - A vim-like in python made from scratch.
* [WordGrinder](https://github.com/davidgiven/wordgrinder) - From the website: "WordGrinder is a word processor for processing words. It is not WYSIWYG. It is not point and click. It is not a desktop publisher. It is not a text editor. It does not do fonts and it barely does styles. What it does do is words. It's designed for writing text. It gets out of your way and lets you type." 
* [zee]() - Zee is a modern editor for the terminal, in the spirit of Emacs. It is written in Rust and it is somewhat experimental.

## <a name="email"></a>Email

Email clients ([Mail User Agents](https://en.wikipedia.org/wiki/Email_client) - MUA), mail synchronization.

* [alot]() - MUA written in Python using the [NotMuch](https://notmuchmail.org/) backend; MailDir format support.  
* [alpine]() - Mail client which aims at being "fast, easy to use email client that is suitable for both the inexperienced email user as well as for the most demanding of power users".
* [Himalaya]() - Command-line interface for email management.
* [mbsync]() - Mailboxes synchronization tool; allows to download email locally; MailDir format supported.  
* [meli]() - BSD/Linux terminal email client with support for multiple accounts and Maildir / mbox / notmuch / IMAP / JMAP.
* [Mutt](https://gitlab.com/muttmua/mutt) - Mail client with tons of features, customization chances, support for IMAP, POP3, multiple storage formats.
* [NeoMutt](https://github.com/neomutt/neomutt) - Patched and up-to-dated mutt fork.
* [nmail]() - nmail is a console-based email client for Linux and macOS with a user interface similar to alpine / pine.
* [pymailgen]() - Starting from the content of a CSV file and a template text file, pymailgen generates a list of emails to be sent out using a command-line SMTP client.
* [sup](https://github.com/sup-heliotrope/sup) - MUA written in Ruby; specifically developed for accounts with "a lot of emails"; nice thread-based presentation.
* [tmpmail]() - A command line utility written in POSIX sh that allows you to create a temporary email address and receive emails to the temporary email address.

## <a name="file-handling"></a>File and file system handling

File managers, tagging, bookmarking.

* [alder]() - Directory tree visualizer.
* [Brash]() - CLI Trash Manager in Pure Bash.
* [classifier]() - Organize files in your current directory, by classifying them into folders of music, pdfs, images, etc.
* [cv]() - (Coreutils Progress Viewer) "looks for coreutils basic commands (`cp`, `mv`, `dd`, `tar`, `gzip/gunzip`, `cat`, etc.) currently running on your system and displays the percentage of copied data. It can also show estimated time and throughput".
* [detox](https://sourceforge.net/projects/detox/) - A utility designed to easily clean up filenames; it replaces characters like spaces with standard equivalents; it also replace UTF-8 or Latin-1 (or CP 1252) characters with more handy ones.  
* [Dext]() - (Directories by Extensions) is a script that moves (or copies) files of the same extension into a folder.
* [doppelganger]() - Save and load your shell environment to create doppelganger shells!
* [dtrx](https://github.com/dtrx-py/dtrx) - (Do The Right eXtraction) aims at taking "all the hassle out of extracting archives"; allows to use one command to extract archives in different formats, recursive extraction (files into file) and extracts files into dedicated directories.
* [entr]() - Event Notify Test Runner - Run an arbitrary command when files change.
* [exa](https://github.com/ogham/exa) - Replacement for 'ls' written in Rust, with colors and several additional "views".
* [FClones]() - Efficient Duplicate File Finder.
* [fd]() - A simple, fast and user-friendly alternative to find. Written in Rust.
* [ff]() - ff is a command-line tool to manage favorite folders, creating an alias, to be used via shell directly with the cd command.
* [file-type-cli]() - Detect the file type of a file or stdin.
* [friendly-find]() - Usable replacement for find.
* [gcp]() - `gcp` (Goffi’s cp) is an advanced file copier tool, heavily inspired from the traditional `cp` command utility, but with some additional features: Displays the copy progress indicator, with estimated time, current file speed; logs of all actions; resume of interrupted copy processes.
* [GoCatGo]() - GoCatGo is another pastebin tool with a super focus on transparency.
* [happyfinder]() - (another) Fuzzy file finder for the command line.
* [ictree]() - Like tree but interactive.
* [inventory]() - Move files like an old text adventure.
* [ll]() - ls with git status.
* [lsd]() - This project is a rewrite of GNU ls with lot of added features like colors, icons, tree-view, more formatting options etc. The project is heavily inspired by the super colorls project.
* [mat2]() - Metadata removal tool, supporting a wide range of commonly used file formats.
* [nat]() - Complete replacement for the `ls` command.
* [organize-cli]() - Organize your files automatically.
* [PathPicker](https://github.com/facebook/pathpicker/) - A tool from Facebook that parses the output from a command and presents a UI to select files and directories; can be used to apply a command of a interactively selected files or to move across directories.  
* [pcopy]() - A temporary file host, nopaste and clipboard across machines. It can be used from the Web UI, via a CLI or without a client by using curl.
* [progress]() - A tool to monitor the progress of common Coreutils command-line tools (`cp`, `mv`, `dd`, `tar`, `rsync`, etc.); it uses an ncurses interface to display the percentage of data copied; it works by reading from system files and retrieving the necessary information for the estimation.
* [pycp]() - cp and mv with a progressbar.
* [RecoverPy]() - RecoverPy is a powerful tool that leverages your system capabilities to recover lost files. Unlike others, you can not only recover deleted files but also overwritten data.
* [rip]() - Safe and ergonomic alternative to rm.
* [rmlint]() - A tool to recursively scan a directory tree looking for duplicate and broken files; it outputs statistics and save the list of files in JSON format; it produce a shell script that can be inspected before running it to delete the desire files.  
* [rmw](https://github.com/theimpossibleastronaut/rmw/) - (ReMove to Waste) is a trashcan/recycle bin utility for the command line. It can move and restore files to and from directories specified in a configuration file.
* [trash-cli]() - Move files and folders to the trash.
* [tre]() - `tree` command improved with git awareness, editor aliasing, and colors.
* [tree](https://gitlab.com/OldManProgrammer/unix-tree) - "Recursive directory listing command that produces a depth indented listing of files".
* [twf]() - Standalone tree view file explorer.
* [vidir]() - vidir allows editing of the contents of a directory in a text editor.
* [watchexec]() - Executes commands in response to file modifications.
* [wfh]() - Continuously watches your local directories and rsync them against a remote host.
* [xcp]() - Extended cp.
* [xplr]() - A hackable, minimal, fast TUI file explorer, stealing ideas from nnn and fzf.

## <a name="file-manager"></a>File manager

* [clifm]() - A CLI-based, shell-like, and non-curses terminal file manager written in C: simple, fast, extensible, and lightweight as hell.
* [fff]() - Fast, simple file manager written in bash.
* [hunter]() - Ranger-like file browser written in rust.
* [lf]() - lf (as in "list files") is a terminal file manager written in Go with a heavy inspiration from ranger file manager.
* [lfm]() - (Last File Manager) is a file manager written in Python; it comes with lots of features, including 1-pane or 2-pane view, files filters and bookmarks, tree view, virtual file-systems to open compressed archives, search in files, customizable keybindings and themes.
* [Midnight Commander](https://github.com/MidnightCommander/mc) - A visual file manager, full-screen text mode application that allows you to copy, move and delete files and whole directory trees and search for files; includes an internal viewer and editor.
* [ncursesFM]() - File manager written in C; rather complete in terms of features; especially lightweight and responsive.  
* [nnn]() - “The unorthodox terminal file manager” is a tiny, nearly 0-config and fast file manager supporting all the operations on files and directories.
* [ranger](https://github.com/ranger/ranger) - Console file manager with vi key bindings; curses interface with a view on the directory hierarchy; comes with a file launcher that automatically determines which program to use for opening a given file type.  
* [rnr]() - The RNR File Manager (RNR's Not Ranger) is a text based file manager that combines the best features of Midnight Commander and Ranger.
* [TUIFI Manager]() - A cross-platform terminal-based termux-oriented file manager (and component), meant to be used with a Uni-Curses project or as is.
* [vifm](https://github.com/vifm/vifm) - "ncurses based file manager with vi like keybindings/modes/options/commands/configuration, which also borrows some useful ideas from mutt" (cit.).

## <a name="file-renamer"></a>File renamers

* [F2]() - Cross-platform command-line tool for batch renaming files and directories quickly and safely.
* [massren]() - Easily rename multiple files using your text editor.
* [mmv]() - Rename multiple files using your $EDITOR. The command name is named after multi-mv.
* [mmv-c]() - Interactively rename files with your favorite editor.
* [moove]() - Manipulate file names and locations using a text editor.
* [Musort]() - Rename multiple audio/music files based on the ID3 tag at once.
* [nomino]() - Batch rename utility for developers.
* [rename]() - Included in `util-linux`, allows bulk rename of files with regex support.
* [rename-cli]() - File renamer with TUI interface and preview.
* [renameutils]() - A set of programs to change file and directory names by editing them inplace; I find `imv` especially useful to edit a filename at the program prompt.  
* [Tempren]() - A powerful file renaming utility that uses flexible template expressions to create new file paths and names.

## <a name="file-system"></a>File systems

* [ipfs-deploy]() - Zero-Config CLI to Deploy Static Websites to IPFS [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System).
* [sshfs]() - Locally mount a remote file-system through SSH and access files and directory as they would be on the local machine.  
* [TMSU](https://github.com/oniony/TMSU) - A tool for tagging files; it provides a simple command line tool for applying tags and a virtual filesystem so that you can get a tag-based view of your files from within any other program.  
* [wutag]() - CLI Tool for tagging and organizing files by tags.

## <a name="font"></a>Font management

* [FIGlet](https://github.com/cmatsuoka/figlet) - Not exactly a font manager, but a nice program for making large letters out of ordinary text; an astonishing number of different fonts is available.
* [toilet](https://github.com/cacalabs/toilet) - A program that tries to improve `FIGlet`; can load FIGlet fonts; supports Unicode input and output, colour fonts and output, and various output formats, including HTML, IRC and ANSI; uses `libcaca` to produce nice textual effects.

## <a name="funny"></a>Funny tools

Miscellaneous of tools that provide some funny/aesthetical functionality.

* [asciicquarium](https://github.com/rgoring/asciiquarium) - Enjoy the mysteries of the sea from the safety of your own terminal!
* [Binary Clock]() - Displays a clock where numbers are represented with blue and gray dots with binary encoding.
* [cbonsai]() - A bonsai tree generator, written in C using ncurses. It intelligently creates, colors, and positions a bonsai tree.
* [cli-fireplace]() - Shows digital fireplace.
* [cmatrix](https://github.com/abishekvashok/cmatrix) - ncurses program that display the scrolling lines found in the movie `The matrix`.
* [cowsay](https://github.com/tnalpgge/rank-amateur-cowsay) - A program that generates a ASCII art of a cow with a bubble containing the specified message (I provide the Wikipedia link since at the moment the link to the author's homepage results to be unreachable).  
* [cowthink](https://github.com/tnalpgge/rank-amateur-cowsay) - Same as `cowsay`, but uses a "think" bubble instead of a speech bubble.
* [ctree]() - A Christmas tree right from your terminal.
* [Draw]() - draw is an simple drawing tool in the terminal. Hold your mouse down and move it across the screen to draw anything you want!
* [fortune](https://github.com/bmc/fortune) - Generates random messages feched from a quotation database.  
* [gof-rs]() - Game of life rendered in your terminal with over 500+ unique patterns to choose from.
* [Limoji]() - Limoji is an open source tool that makes it easy to choose between hundreds of cool ASCII emoticons and share them with your friends.
* [LundukeHoliday]() - A simple Bash script that shows some animated, ASCII holiday decorations in your shell.
* [matrix-webcam]() - Take your video conference from within the matrix.
* [Maze Solver]() - Generate, display and solve mazes in an animated way in the terminal.
* [No More Secrets]() - A command line tool that recreates the famous data decryption effect seen in the 1992 movie Sneakers.
* [pipes.sh]() - Animated pipes terminal screensaver.
* [pokeget]() - A bash script you can use to display cool sprites of pokemon in your terminal.
* [ponysay]() - Pony rewrite of cowsay.
* [pyjokes]() - One line jokes for programmers (jokes as a service).
* [Russhian Roulette]() - 1/6 chance of posting your SSH private key on pastebin (do you really want to try?).
* [sha256-animation]() - Animation of the SHA-256 hash function in your terminal.
* [Steam Locomotive](https://github.com/mtoyoda/sl) - A steam locomotive traverses the screen from right to left if `sl` is typed instead of `ls`.  
* [ternimal]() - Simulate a lifeform in the terminal.
* [yosay]() - Like cowsay, but for yeoman.

## <a name="games"></a>Games

* [Angband](https://github.com/angband/angband) - Angband is a free, single-player dungeon exploration game.
* [anonymine](https://gitlab.com/oskog97/anonymine/) - Curses mode minesweeper without guessing and other original features.
* [bastet](https://github.com/fph/bastet/) - (Bastard Tetris) implements the classical Tetris but with a logic to generate the next block which maximizes the difficulty for the player.  
* [Cataclysm: Dark Days Ahead](https://github.com/CleverRaven/Cataclysm-DDA) - Open source turn-based survival RPG development project.
* [chs]() - Play chess against the Stockfish engine in your terminal.
* [clidle]() - Wordle, now over SSH.
* [crappybird-py]() - Flappy bird.
* [Dwarf fortress]() - A fantasy game using ASCII art graphical representation of the game environment; it features a rich environment with many options and possibilities.  
* [Flapioca]() - A Flappy Bird-inspired terminal game written in Go.
* [freesweep]() - A Minesweeper clone for the terminal which allows you to configure settings such as table rows and columns up to 1024x1024!), percentage of bombs, colors and also has a highscores table.
* [gambit]() - Chess board in your terminal.
* [GameShell]() - GameShell was devised as a tool to help university students to engage with a real shell, in a way that encourages learning while also having fun.
* [greed](https://gitlab.com/esr/greed) - A game of consumption. Eat as much as you can before munching yourself into a corner.
* [hangman]() - A Go TUI Hangman game built with the lovely BubbleTea framework.
* [kboard]() - Terminal game to practice keyboard typing.
* [Language-games]() - Dead simple games made with word vectors.
* [mazter]() - A maze in your terminal.
* [minesweeper]() - Cross-platform terminal based minesweeper.
* [Minesweeper Game]() - A small command line Minesweeper Game.
* [Nethack](https://github.com/NetHack/NetHack) - Single player rogue-like dungeon exploration game.
* [Oldrunner](https://github.com/culot/oldrunner) - Character-based remake of Lode Runner; includes all the original 150 levels.  
* [othello-cli]() - othello-cli is a cli version of Othello (Reversi) written in Rust. You can play against another player, the AI, or watch two AIs play each other.
* [Pokete]() - A terminal based Pokemon like game.
* [rpg-cli]() - Your filesystem as a dungeon!
* [sku]() - Simple TUI written in go to play sudoku in the terminal.
* [Slash'EM](https://sourceforge.net/projects/slashem/) - Rogue-like game derived from `nethack` offering extra features, monsters, and items; includes a GUI version.
* [Solitaire TUI]() - Klondike solitaire for the terminal.
* [sssnake]() - (Smart and sexy snake) The classic snake game for the terminal that can plays itself and be use like a screensaver.
* StarWars vision - See Star Wars in ASCII with ``telnet towel.blinkenlights.nl``.  
* [terdle]() - Wordle implemented in Rust.
* [Terminal Phase](https://gitlab.com/dustyweb/terminal-phase) - A space shooter game you can play in your terminal.
* [terminal_board_games]() - Board games for the terminal.
* [terminordle]() - Inspired by the popular online game wordle made, you can play a pretty close replica of the original locally or multiplayer over the network.
* [Typespeed](https://sourceforge.net/projects/typespeed/) - Type words that are flying by from left to right as fast as you can; features different word sets, e.g., UNIX commands, English words, Non-English words.
* [usolitaire]() - Solitaire in your terminal.
* [wordle-curses]() - A simple TUI wordle game with curses.
* [Words]() - A set of word-based puzzle games for the CLI while you wait for the build to run.

## <a name="git"></a>Git and accessories

* [czg]() - Interactively generate standardized commit messages.
* [forgit]() - A utility tool powered by fzf for using git interactively.
* [fzf-git.sh]() - bash and zsh key bindings for Git objects, powered by fzf.
* [gh-f]() - The ultimate, compact and snappy fzf extension for gh cli.
* [gh-s]() - Search github repositories interactively.
* [gh-stars]() - A GitHub CLI extension to show repository stargazers.
* [git](https://github.com/git/git) - The winner across all the existing file versioning tools; distributed versioning; fully controllable from the command-line; plenty of configuration and usage options; behind a number of related project that leverage git as backend.  
* [git commander]() - A git tool with an easy interactive terminal interface.
* [git-all-branches]() - Improved visualization of git branches (`git branch -a`).
* [git-annex](http://source.git-annex.branchable.com/?p=source.git) - Manages files with `git`, without checking the file contents into git; very useful to manage large/binary files.
* [git-cliff]() - A highly customizable Changelog Generator that follows Conventional Commit specifications.
* [git-cz]() - Semantic Git commits.
* [git-extras]() - Little git extras like git-ignore, git-setup, git-changelog, git-release, git-effort and more.
* [git-peek]() - git peek is the fastest way to open a remote git repository in your local text editor.
* [git-remote-aws]() - Management of encrypted git hosting.
* [git-secret]() - A bash tool which stores private data inside a git repo; it uses users' public keys, allowing trusted users to access encrypted data using pgp and their secret keys.
* [git-stats]() - Local git statistics including GitHub-like contributions calendars.
* [gita]() - A command-line tool to manage multiple git repos.
* [Gitea](https://github.com/go-gitea/gitea) - Single binary self-hosted Git service.
* [gitlab-cli]() - Create GitLab merge requests.
* [gitsummary]() - A better git status taht lists stashes, file statuses, branch list, all nicely formatted with color.
* [gitui]() - GitUI provides you with the comfort of a git GUI but right in your terminal
* [GitUI]() - The comfort of a git GUI but right in your terminal, with keyboard only control, scalable UI, and features all the necessary operations of git.
* [grv]() - Git Repository Viewer - A terminal based interface for viewing Git repositories. It allows refs, commits and diffs to be viewed, searched and filtered.
* [onefetch]() - Git repository summary on your terminal.
* [rcz]() - A tool to write a commit message based on “Conventional Commits”.
* [sad]() - CLI search and replace. Show you a nice diff of proposed changes before you commit them.
* [semantic-git-commit-cli]() - Ensure semantic commits messages. With emoji support.
* [Soft Serve]() - Self-hostable Git server for the command line. One distinguished feature is the possibility to create new repositories with a push.
* [stargazer]() - Github stats from the command line.
* [tig]() - An ncurses-based text-mode interface for `git` that can act as a repository browser, but can also assist in staging changes for commit at chunk level.

## <a name="graphics"></a>Graphics

* [Aewan](https://sourceforge.net/projects/aewan/) - Aewan is a multi-layered ASCII graphics/animation editor. It produces stand-alone cat-able ASCII art files and an easy-to-parse format for integration into terminal applications.
* [Artem]() - Convert images from multiple formats (jpg, png, webp, etc…) to ASCII art, written in Rust.
* [chafa]() - Terminal graphics for the 21st century.
* [cli-mandelbrot]() - A cli for traversing the Mandelbrot fractal.
* [D2]() - D2 is a modern diagram scripting language that turns text to diagrams.
* [deviceframe]() - Put device frames around mobile/web/progressive app screenshots.
* [gifgen]() - Simple high quality GIF encoding.
* [gifsicle]() - Create, manipulate, and optimize GIF images and animations.
* [givegif]() - GIFs on the command line.
* [GraphicsMagick](https://sourceforge.net/projects/graphicsmagick/) - Swiss army knife of image processing.
* [ImageMagick](https://github.com/ImageMagick/ImageMagick) - Software suite to create, edit, compose, or convert bitmap images; it handles many file formats (including PDF and SVG) and provides processing tools to "resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves".
* [imgcat]() - Tool to output images in the terminal. Built with bubbletea.
* [imgp]() - A command line image resizer and rotator for JPEG and PNG images. It can resize (or thumbnail) and rotate thousands of images in a go, at lightning speed, while saving significantly on storage.
* [inklayers]() - A command line program that exports layers from an SVG file. It can be used to create slide shows by editing a single SVG file.
* [jp2a](https://sourceforge.net/projects/jp2a/) - Command-line tool that converts images to ASCII art in the Linux terminal.
* [kakikun]() - Kakikun is a tool to paint, draw and create ASCII art in your terminal using unicode characters.
* [Korkut]() - Quick and simple image processing with the following functions: optimize, convert, crop, resize, rotate, watermark, flip.
* [LinuxLogo](https://sourceforge.net/projects/linuxlogo/) - Display the Linux distribution logo in ASCII format.
* [mandelbrot-cli]() - Multiplatform terminal mandelbrot set explorer.
* [MapSCII]() - A Braille & ASCII world map renderer for your console
* [Mercator]() - OpenStreetMap but as terminal user interface (TUI) program.
* [pastel]() - A command-line tool to generate, analyze, convert and manipulate colors.
* [scrot]() - A simple CLI tool to capture screenshots.  
* [svgcleaner]() - Clean up your SVG files from the unnecessary data.
* [SVGO]() - SVG Optimizer is a Node.js-based tool for optimizing SVG vector graphics files.
* [vhs]() - Write terminal GIFs as code for integration testing and demoing your CLI tools.

## <a name="multimedia"></a>Multimedia

Programs to specifically deal audio/video files.

* [BadaBoomBooks]() - Quickly organize audiobooks using a terminal and web-browser.
* [cTune]() - A ncurses based internet radio player written in C for Linux.
* [Editly]() - A tool and framework for declarative NLE (non-linear video editing) using Node.js and ffmpeg.
* [ffmpeg](https://github.com/FFmpeg/FFmpeg) - The Swiss knife of video editing from the command line.
* [ffscreencast]() - A ffmpeg screencast with video overlay and multi monitor support.
* [invidtui]() - Invidious TUI client, which fetches data from invidious instances and displays a user interface in the terminal, and allows for selecting and playing Youtube audio and video.
* [lotc]() - (Lord Of The Clips) Video downloader, trimmer, and merger using the terminal. Supports YouTube, Facebook, Reddit, Twitter, etc. Downloads/trims at multiple points. Merges multiple clips.

## <a name="networking"></a>Networking

Programs to deal with networks and communication.

* [bandwhich]() - Terminal bandwidth utilization tool.
* [bluetuith]() - A TUI-based Bluetooth connection manager, which can interact with Bluetooth adapters and devices. It aims to be a replacement to most Bluetooth managers, like blueman.
* [bore]() - A simple CLI tool for making tunnels to localhost.
* [geoiplookup]() - A little application to find geographical and network information of an IP address based no the geoip C API.
* [hflow]() - A command-line, debugging http/s proxy server.
* [ipcalc](https://github.com/kjokjo/ipcalc) - Takes an IP address and netmask and calculates the resulting broadcast, network, Cisco wildcard mask, and host range.
* [mitmproxy](https://github.com/mitmproxy/mitmproxy) - An interactive HTTPS proxy.
* [mosh](https://github.com/mobile-shell/mosh) - Remote SSH client that achieve good responsiveness in presence of intermittent connectivity and roaming.
* [Optic](https://github.com/opticdev/optic) - Optic's Open Source tools make OpenAPI and API-first practices easy for any team to adopt.
* [PSSH](https://github.com/lilydjwg/pssh) - PSSH provides parallel versions of OpenSSH and related tools. Included are pssh, pscp, prsync, pnuke, and pslurp. The project includes psshlib which can be used within custom applications.
* [quickserve]() - Quickserve is a very simple HTTP server written in Python that is intended for quickly sharing files on an ad-hoc basis. Aside from opening a port in your firewall if you have one, quickserve requires no set-up and should work with no hassle.
* [redive]() - Trace URL redirections in the terminal.
* [rtop](https://github.com/rapidloop/rtop) - rtop is a simple, agent-less, remote server monitoring tool that works over plain SSH. Written in golang, it does not need any software to be installed on the server that you want to monitor. It works by establishing an SSH session, and running commands on the remote server to collect system metrics.
* [Rustcat]() - Netcat Alternative in Rust.
* [serve]() - Serves a static site, single page application, or just a static file, and provides a neat interface for listing the directory's contents.
* [speedtest-net]() - Test internet connection speed and ping using speedtest.net.
* [termishare]() - Peer to peer terminal sharing.
* [TStream]() - Live streaming from the terminal. Requires the connection to a central server, from which the streaming is dispatched.
* [ttyd]() - Share your terminal over the web.
* [Tunnelmole]() - Connect to local servers from anywhere.
* [Wishlist]() - With Wishlist you can have a single entrypoint for multiple SSH endpoints.
* [xiringuito]() - VPN made easy! No configuration. No VPN servers. No hassle. Using SSH capabilities.
* [xxh]() - Bring your favorite shell wherever you go through the ssh.

## <a name="note-taking"></a>Note taking

* [cadmus]() - Shell Scripts to Facilitate Effective Note Taking.
* [dn]() - Daily notes command line tool.
* [dnote]() - A simple command line notebook for the terminal. It also offers a seamless multi-device sync and a web interface.
* [eureka]() - Store your ideas without leaving the terminal.
* [Geeknote]() - A command line client for Evernote that can be use on Linux, FreeBSD and OS X.
* [idea]() - A lightweight tool for keeping ideas in a safe place quick and easy.
* [jnrl]() - Collect your thoughts and notes without leaving the command line.
* [jot]() - Jot is a feature-stripped version of Obsidian focused on rapid note management through the terminal. It uses the same format of storage as Obsidian.
* [kb]() - A minimalist knowledge base manager.
* [nb]() - A command line and local web note‑taking, bookmarking, archiving, and knowledge base application.
* [Noted]() - Notes library, with viewer and shortcuts to add, delete and edit notes.
* [NoteSH]() - Sticky notes App in the Terminal, built with Textual, an amazing TUI framework!
* [posce]() - A note-taking toolkit for your command line.
* [sncli]() - A Python application that gives you access to your Simplenote account via the command line.
* [Standard Unix Notes]() - GPG Encrypted Notes/Notebook manager for BSD/Linux.
* [Terminal velocity](https://github.com/vhp/terminal_velocity) - A fast, cross-platform note-taking application for the UNIX terminal.

## <a name="office"></a>Office tools

Spreadsheet and presentations.

* [conan]() - Find clue about the type of the file.
* [conrad]() - Track conferences and meetups.
* [DeckTape]() - DeckTape is a high-quality PDF exporter for HTML presentation frameworks.
* [Lotus 1-2-3 for Linux]() - A native port of Lotus 1-2-3 Release 3 to Linux.
* [mdp]() - A command-line based markdown presentation tool.
* [Quoter]() - The console based stock quote tool.
* [sc-im]() - Spreadsheet Calculator Improvised -- An ncurses spreadsheet program for terminal. It is rich in functionalities, but the syntax of functions and other details are different from the common spreadsheets such as Excel and Calc, making difficult to "re-cycle" existing knowledge on these programs to work proficiently with sc-im. Neverthless, a nice piece of software."
* [scholarref](https://src.adamsgaard.dk/scholarref/) - Tools to never deal with journal webpages again.
* [sent](https://git.suckless.org/sent/log.html) - Simple plaintext presentation tool.
* [Slides]() - Terminal based presentation tool.
* [Teapot]() - Compact ncurses-based spreadsheet with original syntax, 3D-style and built-in functions.
* [Ticker]() - Terminal stock watcher and stock position tracker.
* [tpp](https://github.com/Kerrick/tpp) - (text presentation program) a ncurses Ruby program that allows to produce nice text-based presentation with simple markup language.
* [translate-shell]() - Command-line translator using Google Translate or other online services.
* [trino]() - Quick and easy translation of words and phrases entered in the command line.  
* [VocabCLI]() - Lightweight CLI that allows users to look up word definitions, examples, synonyms and antonyms directly via the command line; it also offers advanced Text Classification and Processing via the use of Natural Language Processing and Machine Learning algorithms.
* [wikit]() - A command line program for getting Wikipedia summaries easily.

## <a name="organizers"></a>Organizers and calendars

Calendar managers.

* [addrb]() - A lightweight CLI / TUI address book that supports CardDAV.
* [buku]() - A powerful bookmark manager written in Python3 and SQLite3.
* [calcure](https://github.com/anufrievroman/calcure) - Modern TUI calendar and task manager with customizable interface.
* [calcurse](https://git.calcurse.org/calcurse.git/) - A calendar and scheduling application for the command line. It helps keep track of events, appointments and everyday tasks.
* [caldr]() - A lightweight CLI / TUI calendar that supports CalDAV.
* [gcalcli]() - CLI to access Google Calendars; allows to do the main tasks: create, delete, and list events.
* [goobook]() - The purpose of GooBook is to make it possible to use your Google Contacts from the command-line and from MUAs such as Mutt.  It can be used from Mutt the same way as abook.
* [khal]() - CLI and terminal calendar program, able to synchronize with CalDAV servers through [vdirsyncer](https://github.com/pimutils/vdirsyncer).
* [khard]() - Console carddav client written in Pyhton.  
* [Org mode](https://git.savannah.gnu.org/cgit/emacs/org-mode.git) - Super-powerful [Emacs](https://www.gnu.org/software/emacs/) plugin to manage outlines with associated timestamps, priorities, labels, etc.; available views grouped by time (agenda), tags, etc.; plain text storage format.
* [pal](https://sourceforge.net/p/palcal/code/HEAD/tree/) - Calendar program for Unix/Linux systems that can keep track of events; custom, plain text storage format; interesting and fully functional.
* [peroutine]() - Remind you of periodical events. The period can be any positive integer of days, so work around the fact that the number of days in a week is prime.
* [ppl addressbook](https://github.com/henrycatalinismith/ppl) - `ppl` is free software made out of other free software.  It's built on top of Ruby and Git, and the completely free vcard address book format.
* [Remind](https://git.skoll.ca/Skollsoft-Public/Remind) - Calendar program with possibility to set complex rules to define events; custom, powerful text-based storage format.
* [remint]() - A simple terminal UI wrapper for D. Skoll's Remind calendar program
* [vdirsyncer]() - CalDAV synchronization program.
* [Wyrd](https://gitlab.com/wyrd-calendar/wyrd) - Curses front-end for [Remind](https://www.roaringpenguin.com/products/remind) written in OCaml with vertically scrollable time table.  

## <a name="online"></a>Online search and resources

* [arch-wiki]() - Search the Arch Wiki anywhere from the command line.  
* [Awesome CLI]() - Awesome CLI is a simple command line tool to give you a fancy command line interface to dive into Awesome lists.
* [Awesome Finder]() - Search the awesome lists from the command line.
* [ddgr]() - A command line utility to search DuckDuckGo (html version) from the terminal.
* [googler]() - Google Search, Google Site Search, Google News from the terminal.
* [pockyt]() - Read, manage, and automate the collection of articles in [Pocket](https://getpocket.com), an application for managing a reading list of articles from the Internet.
* [Seashells](https://github.com/anishathalye/seashells) - Pipe output to the web.
* [so]() - Terminal interface for Stack Overflow.
* [socialscan]() - Python library and CLI for accurately querying username and email usage on online platforms.
* [socli]() - Stack overflow command line client written in Python.  Search and browse stack overflow without leaving the terminal 

## <a name="password-manager"></a>Password managers

* [Bitwarden CLI](https://github.com/bitwarden/cli) - Command-line interface for Bitwarden, a multi-platform password manager targeted to companies and enterprises.
* [cpass]() - Another console UI for pass.
* [dpg]() - The Deterministic Password Generator - Generates passwords based on a master password and the indication of the website/service/username, without the need of storing anything.
* [gopass](https://github.com/gopasspw/gopass) - gopass is a rewrite of the pass password manager in Go with the aim of making it cross-platform and adding additional features. The target audience are professional developers and sysadmins (and especially teams of those) who are well versed with a command line interface.
* [hide]() - AES-256 bit encrypted password manager with all encrypted passwords stored locally on your machine
* [keydex]() - Manage KeePass databases from your terminal.
* [kpcli](https://sourceforge.net/projects/kpcli/) - A command line interface for KeePass.
* [pa]() - A simple password manager; encryption via age, written in portable posix shell.
* [pass](https://git.zx2c4.com/password-store/) - With pass, each password lives inside of a gpg encrypted file whose filename is the title of the website or resource that requires the password. These encrypted files may be organized into meaningful folder hierarchies, copied from computer to computer, and, in general, manipulated using standard command line file management utilities.
* [passfzf]() - A simple fzf wrapper for pass (the UNIX password-store). It allows fuzzy finding your pass passwords to copy, show, edit, delete, rename and duplicate them.
* [Pswd]() - A secure password generator written in C.
* [safe.sh]() - Pure Bash script to manage secure archives; simple and clean; uses [gnugpg](https://gnupg.org/) for encryption/decryption, thus can leverage tools like [GPG Agent](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html).
* [SpicyPass]() - A light-weight password manager with a focus on simplicity and security.
* [titan](https://github.com/nrosvall/ylva) - Password management belongs to the command line, deep into the Unix heartland, the shell. Titan is written in C and is available under the MIT license.

## <a name="productivity"></a>Productivity

* [ancv]() - Renders your (JSON) resume/CV for online & pretty terminal display.
* [arbtt](https://github.com/nomeata/arbtt) - (automatic, rule-based time tracker) runs in background, collecting information regarding open windows, focussed ones, etc.; it can be configured to display statistics on the collected data, e.g., figuring out the time spent on one specific window.
* [avail]() - Find available times between all your calendars.
* [Bartib]() - Easy to use time tracking tool for the command line. It saves a log of all tracked activities as a plaintext file and allows you to create flexible reports.
* [cambd-cli]() - A CLI tool to automate the process to access the Cambridge dictionary.
* [CLI-Dictionary]() - Scripts for downloading and viewing wiktionary entries from Kaikki.org.
* [cowyo]() - Feature rich wiki webserver for minimalists.
* [dijo]() - Scriptable, curses-based, digital habit tracker.
* [doing]() - A command line tool for remembering what you were doing and tracking what you've done.
* [fasttyper]() - Fasttyper is minimalistic typing test based on user provided exercising text.
* [flash-tui]() - Flashcard app for the terminal.
* [gdir]() - A command line tool which queries Google Directions. The tool displays results as human-readable text.
* [GTT - Google Translate TUI]() - A TUI interface to bring Google Translation in the terminal.
* [h-m-m]() - h-m-m (pronounced like the interjection "hmm") is a simple, fast, keyboard-centric terminal-based tool for working with mind maps.
* [habitctl]() - Minimalist command line tool you can use to track and examine your habits.
* [habitmap]() - A command-line app to track your habits and visualise how committed you are to making or maintaining them with colorful heatmaps.
* [hardv]() - A CLI flashcard app for UNIX-compatible systems, conforming to the UNIX philosophy.
* [hledger](https://github.com/simonmichael/hledger) - A is fast, reliable, free, multicurrency double-entry accounting software to track money, investments, cryptocurrencies, time, or any other quantifiable commodity; uses a future-proof plain text file format.
* [kabmat]() - TUI program for managing kanban boards with vim-like keybindings.
* [ledger](https://github.com/ledger/ledger) - A powerful, double-entry accounting system from the command-line; it uses a simple yet powerful text syntax to specify the items to account.
* [moeda]() - A foreign exchange rates and currency conversion using the command line.
* [Moro]() - A command line tool for tracking work hours, as simple as it can get.
* [paycon]() - Converts pay amounts between different time units.
* [py_flashcards]() - Text-only CLI flashcards parsed from Markdown file.
* [speedread]() - A simple terminal-based open source Spritz-alike filter that shows input text as a per-word RSVP (rapid serial visual presentation) aligned on optimal reading points.
* [speki]() - Manage flashcards in the terminal; similar to anki.
* [Taskell]() - A CLI kanban board/task manager for Mac and Linux.
* [thokr]() - Sleek typing tui with visualized results and historical logging.
* [Timetrap]() - A simple command line time tracker written in Ruby. It provides an easy to use command line interface for tracking what you spend your time on.
* [Timewarrior]() - A time tracking utility that offers simple stopwatch features as well as sophisticated calendar-based backfill, along with flexible reporting.
* [toipe]() - Yet another typing test, but crab flavoured.
* [Translate Shell](https://github.com/soimort/translate-shell) - Command-line translator using Google Translate, Bing Translator, Yandex.Translate, etc.
* [tuxi]() - A CLI tool that scrapes Google search results and SERPs that provides instant and concise answers.
* [tz]() - tz helps you schedule things across time zones. It's an interactive TUI program that displays time across the time zones of your choosing.
* [utt]() - Ultimate Time Tracker - A simple command-line time tracker written in Python.
* [Watson]() - Time tracking CLI to know how much time you are spending on your projects. It can generate nice reports for clients.
* [zeitkatze]() - Simplest stopwatch in a linux console.

## <a name="programming"></a>Programming

* [add-gitignore]() - Interactively generate a .gitignore for software projects.
* [boilr]() - Boilerplate template manager that generates files or directories from template repositories.
* [cgasm]() - Pronounced “SeekAzzem”, it is a standalone, offline terminal-based tool with no dependencies that gives me x86 assembly documentation.
* [chars]() - Display names and codes for various ASCII (and unicode) characters / code points.
* [cloc]() - Tool for counting blank lines, comment lines, and physical lines of source code in many programming languages.
* [clog]() - Creates a changelog automatically from local git metadata.
* [Cookiecutter]() - A cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects.
* [Cppcheck](https://github.com/danmar/cppcheck/) - Static analysis tool for C/C++ code providing unique code analysis to detect bugs and focuses on detecting undefined behaviour and dangerous coding constructs.
* [dtool]() - Collection of development tools.
* [fastmod]() - A tool to assist you with large-scale codebase refactors, and it supports most of codemod's options. It is focused on improving the use case "I want to use interactive mode to make sure my regex is correct, and then I want to apply the regex everywhere".
* [fmake]() - Brings `make`s interface to almost any build system.
* [Frama-C](https://git.frama-c.com/pub/frama-c/) - Open-source extensible and collaborative platform dedicated to source-code analysis of C software. Frama-C can assist from the navigation through unfamiliar projects up to the certification of critical software.
* [gdb-dashboard]() - Modular visual interface for GDB in Python.
* [grex]() - A command-line tool for generating regular expressions from user-provided test cases.
* [hors]() - Instant coding answers via the command line.
* [howdoi]() - Instant coding answers via the command line.
* [kickstart]() - Scaffolding tool to get new projects up and running quickly.
* [Kool]() - CLI tool that brings the complexities of modern software development making these environments lightweight, fast and reproducible.
* [legit]() - Automagically generates a LICENSE file for the current working directory that you are in or a license header for a file where applicable.
* [license-up]() - Create a license quickly for a given name.
* [mklicense]() - CLI tool for easily generating the text of the most common licenses.
* [nbterm]() - Jupyter Notebooks in the terminal.
* [pire]() - Python Interactive Regular Expressions.
* [Proji]() - Powerful cross-platform CLI project templating tool.
* [pvcheck]() - A tool to apply automated testing to programs that produce textual output. The format of the output is very specific, making pvcheck suitable to test programming quizzes.
* [readme-md-generator]() - CLI that generates beautiful README.md files.
* [rebound]() - Fetch Stack Overflow results in your terminal when you get an error. Supported languages: Python, Node.js, Ruby, Golang, and Java.
* [release-it]() - Automate releases for Git repositories and/or Node.js packages.
* [rr](https://github.com/rr-debugger/rr) - Debug the recording, deterministically, as many times as you want.
* [scc]() - Sloc Cloc and Code (scc) is a codebase statistics counter. Goal is to be the fastest code counter possible, but also perform COCOMO calculation like sloccount and to estimate code complexity similar to cyclomatic complexity calculators. In short one tool to rule them all.
* [scons]() - Software construction tool.
* [temci]() - Advanced benchmarking tool written in Python 3 that supports setting up an environment for benchmarking and the generation of visually appealing reports.
* [Tokei]() - Tokei is a program that displays statistics about your code. Tokei will show the number of files, total lines within those files and code, comments, and blanks grouped by language.

## <a name="science"></a>Science

Tools for scientific research and science applications.

* [bib.awk]() - Bibliography manager written in awk.
* [cobib]() - Simple, command-line based bibliography management tool.
* [element]() - Periodic table on the command line.
* [FAWOC]() - FAWOC is a TUI program for manually labelling a list of words. It has been developed to support the efficient clustering of documents based on topic modeling algorithms such as Dirichlet Latent Allocation.
* [Go-L]() - Game of Life with different update rules and on a bunch of different topologies (sphere, torus, klein bottle, etc.).
* [papis]() - Extensible document and bibliography manager.
* [pt.sh]() - CLI periodic table with search and many properties.
* [Pubs]() - Pubs organizes your scientific papers together with their bibliographic data and provides command line access to basic and advanced manipulation of your library.
* [slr-kit]() - Set of CLI tools to assist the writing of Systematic Literature Reviews powered by Natural Language Processing.
* [starfetch]() - Command line tool that displays constellations.

## <a name="security"></a>Security and encryption

Cryptography, ciphered archive managers, encrypted file-systems.

* [acmetool]() - Easy-to-use command line tool for automatically acquiring certificates from ACME servers (such as Let's Encrypt).
* [cipher]() - An Ash module that makes it easy to perform aes-256-cbc encryption for files and directories.  
* [cotp]() - Trustworthy, encrypted, command-line TOTP/HOTP authenticator app with import functionality.
* [cream](https://git.z3bra.org/cream/files.html) - Encrypt and decrypt streams of data with only a master password. The key is derivated from the password + salt combo, and used to encrypt data byte per byte.
* [enc]() - A modern and friendly CLI alternative to GnuPG: generate and download keys, encrypt, decrypt, and sign text and files, and more.
* [encfs](https://github.com/vgough/encfs) - Encrypted filesystem in user-space based on [FUSE](https://it.wikipedia.org/wiki/FUSE); mounts an encrypted directory into a clear one.  
* [feroxbuster]() - A fast, simple, recursive content discovery tool written in Rust.
* [Firejail](https://github.com/netblue30/firejail) - A SUID program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces and seccomp-bpf.
* [GnuPG](https://dev.gnupg.org/source/gnupg/repository/master/) - GnuPG is a complete and free implementation of the OpenPGP standard as defined by RFC4880 (also known as PGP).
* [hashcat](https://github.com/hashcat/hashcat) - A robust and efficient password cracking tool that can help you recover lost passwords, audit password security, benchmark, or just figure out what data is stored in a hash.
* [Image Steganography Tool]() - Simple C++ Encryption and Steganography tool that uses Password-Protected-Encryption to secure a file's contents.
* [LUKS](https://github.com/guardianproject/luks/wiki) - Hard disk encryption tool; it stores all setup information in the partition header, enabling easy data transport or migration.
* [Minisign]() - A dead simple tool to sign files and verify digital signatures.
* [OAuth2c]() - A command-line tool for interacting with OAuth 2.0 authorization servers.
* [ots]() - Share end-to-end encrypted secrets with others via a one-time URL.
* [PaperAge]() - Easy and secure paper backups of secrets, which takes a text and generates an encrypted QRcode to print on paper.
* [pgen]() - Generate passphrases using the wordlists for random passphrases made by the EFF.
* [StegCloak]() - Hide secrets with invisible characters in plain text securely using passwords
* [uacme]() - ACMEv2 client written in plain C with minimal dependencies.
* [wifi-password]() - Get wifi pass.

## <a name="shells"></a>Shells

* [Bash](https://git.savannah.gnu.org/cgit/bash.git) - (Bourne Again SHell) The most widespread system shell to date.  
* [Cat9]() - Cat9 is a user shell script for LASH - a command-line shell that discriminates against terminal emulators, written in Lua.
* [cosh]() - Concatenative command-line shell.
* [Fish](https://github.com/fish-shell/fish-shell) - "A command line shell for the 90s"; focused on user-friendliness, with powerful autosuggestions, colors, "sane scripting" (w.r.t. to Bash).
* [Reptyl]() - A cross-platform command line shell that supports execution of commands in natural language.
* [Spaceship](https://github.com/spaceship-prompt/spaceship-prompt) - Minimalistic, powerful and extremely customizable Zsh prompt.
* [xonsh](https://github.com/xonsh/xonsh) - The xonsh shell lets you easily mix Python and shell commands in a powerful and simplified approach to the command line.
* [Zsh](https://sourceforge.net/p/zsh/code/ci/master/tree/) - Alternative shell designed for interactive use.  

## <a name="music"></a>Sound and music

Music players.

* [Alsamixer](https://github.com/alsa-project) - ALSA mixer with curses interfaces.  
* [beets]() - Beets is the media library management system for obsessive music geeks: catalogs your collection, automatically improving its metadata as it goes.
* [castero]() - A TUI podcast client for the terminal.
* [cmus](https://github.com/cmus/cmus) - A fast and lightweight audio player with configurable keybindings and playlist support.  
* [dzr]() - Command Line deezer.com Player for Linux, BSD, Android, Windows.
* [espeak](https://sourceforge.net/p/espeak/code/HEAD/tree/) - A compact open source software speech synthesizer for English and other languages.
* [Instant Music Downloader]() - Instantly download any song!
* [kord]() - A python framework that provides programmers with a simple api for the creation of music-based applications.
* [MOC]() - (music on console) is a powerful and easy to use console audio player; user interface a la Midnight Commander; plenty of features; fully controllable from the keyboard.  
* [Mp3blaster](https://sourceforge.net/projects/mp3blaster/) - Audio player for the text console.
* [mpg123](https://sourceforge.net/projects/mpg123/) - Quick `mp3` sound file player; no visual interface, just a command-line audio file player for `mp3` files.
* [mps-youtube]() - A curses player for music tracks from Youtube; it allows to search for songs and playlists; it downloads the video, extracts the audio track and plays it; handles local playlists and many configuration parameters.
* [mpvc]() - A minimal mpc-like CLI and TUI for controlling mpv from the shell.
* [muCLIar]() - YouTube automator bringing you your music right on your CLI.
* [MusicPlayerPlus]() - Featureful ncurses based MPD client inspired by ncmpc with integration for Beets, spectrum visualization,Bandcamp/Soundcloud, asciimatics, cantata, and more.
* [musikcube]() - A cross-platform, terminal-based audio engine, library, player and server written in C++.
* [ncmpcpp](https://github.com/ncmpcpp/ncmpcpp) - NCurses Music Player Client (Plus Plus) - featureful ncurses based MPD client inspired by ncmpc. Relevant features: tag editor, playlist editor, easy to use search engine, media library, music visualizer, ability to fetch artist info from [last.fm](https://www.last.fm/), new display mode, alternative user interface, ability to browse and add files from outside of MPD music directory.
* [ogg123](https://gitlab.xiph.org/xiph) - Quick `ogg` sound file player; no visual interface, just a command-line audio file player for the free and open `ogg` file format.
* [PyRadio]() - Curses based internet radio player.
* [Siren](https://www.kariliq.nl/git/siren/) - Siren is a text-based audio player for UNIX-like operating systems.
* [Spotify TUI]() - A Spotify client for the terminal written in Rust.
* [spotify-player]() - spotify-player is a fast, easy to use, and configurable terminal music player having feature parity with the official Spotify application.
* [Tera]() - Terminal Radio: an easy-to-use CLI music player to play favorite music, radio stations and explore various radio stations from the terminal only.
* [termusic]() - Terminal Music Player written in Rust.
* [Tizonia]() - Command-line cloud music player for Linux with support for Spotify, Google Play Music, YouTube, SoundCloud, TuneIn, iHeartRadio, Plex servers and Chromecast devices.
* [yt-audio]() - A simple, configurable youtube-dl wrapper to download and manage youtube audio.

## <a name="monitor"></a>System monitoring

* [below]() - A time traveling resource monitor for modern Linux systems
* [bpytop]() - Linux/OSX/FreeBSD resource monitor with a nice interface.
* [Chokidar CLI]() - Fast cross-platform command line utility to watch file system changes.
* [dmidecode](http://git.savannah.gnu.org/cgit/dmidecode.git/) - System information utility.
* [Fastfetch]() - Like neofetch, but much faster because written in C.
* [glances](https://github.com/nicolargo/glances) - A comprehensive and detailed system monitoring tool; monitored parameters include: CPU, memory, load, process list, network interfaces, disk I/O, sensors, filesystems, docker, system info, uptime.
* [htop](https://github.com/htop-dev/htop) - An interactive process viewer for Unix; improves the UI of `top`, by adding real-time meters and colors.
* [hyperfine]() - A command-line benchmarking tool.
* [inxi](https://github.com/smxi/inxi) - A comprehensive system information script; provides information about CPU, graphics, audio and network devices, drives and partitions, sensors; implemented as a Bash script.
* [iotop](https://repo.or.cz/w/iotop.git) - "A Python program with a top like UI used to show of behalf of which process is the I/O going on".
* [lfs]() - A thing to get information on your mounted disks
* [multitail](https://github.com/folkertvanheusden/multitail) - A command to open multiple log files in a single terminal window and monitor them in real-time.  
* [neofetch]() - Neofetch is a CLI system information tool written in BASH. Neofetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice.
* [ngrep](https://github.com/jpr5/ngrep/) - (Network grep) applies the `grep` logic to the network layer, allowing to match regular expressions against data payloads of packets; it recognizes IPv4/6, TCP, UDP, ICMPv4/6, IGMP and Raw across Ethernet, PPP, SLIP, FDDI, Token Ring and null interfaces.
* [noti]() - Monitor a process and trigger a notification.
* [nvitop]() - An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management.
* [powertop](https://github.com/fenrus75/powertop) - A `top`-like utility to monitor the sources of power consumption; allows to turn on/off many components; quite useful to track possible power-related issues.  
* [ramfetch]() - A fetch which displays memory info using /proc/meminfo.
* [screenFetch]() - It can be used to generate one of those nifty terminal theme information + ASCII distribution logos. It auto-detects the distribution and display an ASCII version of that distribution's logo and some valuable information to the right.
* [smem](https://selenic.com/repo/smem) - Python program that reports memory usage; it can report the "proportional set size" (PSS), a meaningful representation of the amount of memory used by libraries and applications in a virtual memory system; it has built-in chart generation.
* [sysdig](https://github.com/draios/sysdig) - Sysdig captures system calls and events from the Linux kernel.  You can save, filter, and analyze the data with our CLI or our desktop app.  Think of sysdig as strace + tcpdump + htop + iftop + lsof + wireshark for your entire system.
* [The Logfile Navigator](https://github.com/tstack/lnav) - An advanced and colorful log file viewer with TUI interface.
* [tiptop]() - A command-line system monitoring tool in the spirit of top, written in Python. It displays various interesting system stats and graphs them. Works on all operating systems.
* [top]() - The classical Unix utility that provides a rolling display of top cpu using processes.  
* [ttop]() - top-like system monitoring tool with TUI, historical data service and triggers.
* [ttyload](https://github.com/lindes/ttyload) - ttyload is a lightweight utility which is intended to offer a color-coded graph of load averages over time on Linux and other Unix-like systems. It enables a graphical tracking of system load average in a terminal (“tty“).
* [watch]() - Periodically runs a command in the console while temporarily clearing the screen content; it makes it easy to check differences between the output of two subsequent commands; it provides "diff" functionality to highlight the changing characters between outputs.
* [watcher]() - Watches all the files present in a directory and whenever a file is changed or a file is created/deleted from the directory, it runs a specified command.
* [whowatch]() - Monitor Linux Users and Processes in Real Time.
* [wtf]() - The personal information dashboard for your terminal.
* [ytop]() - TUI system monitor written in Rust.
* [zfxtop]() - Self described as “fetch top written by bubbletea enjoyer”.

## <a name="system"></a>System tools

* [active-win-cli]() - Get the title/id/etc of the active window.
* [asdf](https://github.com/asdf-vm/asdf) - Manage multiple runtime versions with a single CLI tool.
* [atuin]() - Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.
* [Bevel]() - Command line history in an SQLite database for effective re-use.
* [bin]() - Manages binary files downloaded from different sources.
* [brightnessctl]() - Read and control device brightness. Devices, by default, include backlight and LEDs - searched for in corresponding classes.
* [checksum.sh](https://github.com/gavinuhma/checksum.sh) - Checksum.sh is a simple way to download, review, and verify install scripts. If the checksum is OK the script will be printed to stdout, which can be piped to sh or elsewhere.
* [cli-tools-info]() - An overview of you CLI tools, if they are installed and what version they are on.
* [conspy](https://sourceforge.net/p/conspy/code/ci/default/tree/) - "Conspy allows a (possibly remote) user to see what is displayed on a Linux virtual console, and send keystrokes to it." 
* [ContainerSSH]() - An SSH Server that Launches Containers in Kubernetes and Docker on demand.
* [Devbox]() - Devbox is a command-line tool that lets you easily create isolated shells and containers by defining the list of packages required by the environment.
* [docker](https://github.com/docker/docs) - Self-sufficient runtime for containers.
* [fkill-cli]() - Simple cross-platform process killer.
* [has]() - Checks presence of various command line tools on the PATH and reports their installed version.
* [hiSHtory]() - A better shell history that stores context (directory, succeeded or failed, how long it took, etc). The history is stored locally and end-to-end encrypted for syncing to other computers.
* [hstr]() - A tool for managing the history; powerful visual search and execution of previous commands; history editing capabilities.  
* [just]() - just is a handy way to save and run project-specific commands.
* [lshw](https://ezix.org/src/pkg/lshw) - A small tool to provide detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc.
* [mackup]() - Keep your application settings in sync (OS X/Linux).
* [mprocs]() - mprocs runs multiple commands in parallel and shows output of each command separately.
* [Mxflow-cli]() - A modern, general purpose CLI task runner with human readable yaml config file.
* [nala]() - apt package manager front-end with cleaner interface.
* [Ntfy]() - Cross-platform Python utility that enables you to automatically get desktop notifications on demand or when long running commands complete. It can as well send push notifications to your phone once a particular command completes.
* [parallel](https://git.savannah.gnu.org/cgit/parallel.git) - A shell tool from GNU for executing jobs in parallel using one or more computers; it can split the input and pipe it into commands in parallel.  
* [procmux]() - A TUI utility for running multiple commands in parallel in easily switchable terminals.
* [pulsemixer]() - CLI and curses mixer for PulseAudio.
* [pypi-command-line]() - A powerful, colorful, beautiful command-line-interface for pypi.org.
* [sake]() - A command runner for local and remote hosts. You define servers and tasks in sake.yaml file and then run the tasks on the servers.
* [stew]() - An independent package manager for compiled binaries.
* [sysm]() - Makes your system play custom sounds when any configured system or external event happens.
* [systeroid]() - A more powerful alternative to sysctl(8) with a terminal user interface.
* [task-spooler]() - A Unix batch system that can be used to add the Linux commands to the queue and execute them one after the other in numerical order (ascending order, to be precise). This can be very useful when you have to run a lots of commands, but you don't want to waste time waiting for one command to finish and run the next command. You can queue it all up and Task Spooler will execute them one by one. In the mean time, you can do other activities.

## <a name="terminal"></a>Terminals

* [byobu](https://github.com/dustinkirkland/byobu) - A text-based window manager and terminal multiplexer; it features enhanced profiles, convenient keybindings, configuration utilities, and toggle-able system status notifications; compatible with `screen` and `tmux`.
* [dtach]() - A program written in C that emulates the detach feature of screen.
* [mtm]() - Micro Terminal Multiplexer - Simple but usable, stable and minimalistic terminal multiplexer.
* [mx]() - A tmux session manager written as a single Bash script.
* [screen](https://git.savannah.gnu.org/cgit/screen.git) - Terminal multiplexer that split a physical terminal between several processes, typically interactive shells.
* [Tmate](https://github.com/tmate-io/tmate) - A fork of tmux that allows to share the terminal with other users. AFAIK, it connects to a centralized server to establish the connection. Someone may see this inconvenient for privacy issues.
* [tmux](https://github.com/tmux/tmux) - Terminal multiplexer; born to improve `screen`; client-server architecture, `vi` and `emacs` key-bindings, search in window feature and many more.
* [warp]() - Secure and simple terminal sharing.  
* [Zellij]() - A workspace aimed at developers, ops-oriented people and anyone who loves the terminal. At its core, it is a terminal multiplexer.

## <a name="text-processing"></a>Text processing

* [alex]() - Catch insensitive, inconsiderate writing, by finding gender favoring, polarizing, race related, or other unequal phrasing in text.
* [amber]() - Code search / replace tool.
* [anew]() - Tool for adding new lines to files, skipping duplicates.
* [as-tree]() - Print a list of paths as a tree of paths.
* [brok]() - Find broken links in text documents.
* [ccat]() - A `cat` command with colorized output.  
* [choose]() - NCurses based token selector with a nice terminal user interface for selecting tokens. Selecting a line from the bash history is only one of its use cases.
* [deadlink]() - Parses text files for HTTP URLs and checks if they are still valid. Good to use on markdown documentation files.
* [delta]() - A syntax-highlighter for git and diff output.
* [detect-indent-cli]() - Detect the indentation of code.
* [diff-so-fancy]() - Make your diffs human readable instead of machine readable.
* [diff2html-cli]() - Parse git diffs as JSON and generate pretty HTML.
* [Difftastic]() - Syntax-aware structured diff tool.
* [DocToc]() - Generates table of contents for markdown files inside local git repository. Links are compatible with anchors generated by github or other sites.
* [espanso]() - Cross-platform Text Expander written in Rust. Not limited to the command line.
* [fullname-cli]() - Get the fullname of the current user.
* [fzf]() - (FuZzy Finder) is a general-purpose command-line finder with fuzzy search/filter capabilities; good integration with `vim`.  
* [fzy]() - Better fuzzy finder.
* [grc]() - (Generic Colouriser) can be configured to parse a given text stream and to colorize it according to regexp written in configuration files; different patterns can be associated to file types.  
* [gzip-size-cli]() - Get the gzipped size of a file.
* [HASHA CLI]() - Hashing made simple. Get the hash of text or stdin.
* [hck]() - A sharp cut clone.
* [hget]() - A CLI to convert HTML into plain text. Can be used to fetch a site's HTML version and convert it into plain text, or to deliver plain text versions of your site dynamically.
* [huniq]() - Command line utility to remove duplicates from the given input. Note that huniq does not sort the input, it just removes duplicates.
* [kill-tabs]() - Kill all Chrome tabs to improve performance, decrease battery usage, and save memory.
* [leven-cli]() - Measure the difference between two strings using the Levenshtein distance algorithm.
* [lolcat]() - Ruby Gem to colorize the output of the cat command.
* [luneta]() - Interactive filter that can be easily composed within any script.
* [pdf-diff]() - A tool for visualizing differences between two pdf files. Mainly dedicated to editors that usually spends a lot of hours on several pdf.
* [percol]() - A Python script that "1) receives input lines from `stdin` or a file, 2) lists the input lines and waits for input that filter/select the line(s), 3) outputs the selected line(s) to `stdout`"; can be used to add interactivity to many regular shell commands.
* [pick]() - Utility that allows users to choose one option from a set of choices using an interface with fuzzy search functionality.  
* [pup]() - Parsing HTML at the command line.
* [pv](https://github.com/a-j-wood/pv) - The pv command is used to monitor the progress of data through pipe.
* [rare]() - Realtime regex-extraction and aggregation into common formats such as histograms, bar graphs, numerical summaries, tables, and more!
* [sd]() - s[earch] & d[isplace] - An intuitive find & replace CLI; a possible replacement for sed.
* [skim]() - Fuzzy Finder in rust.
* [squeeze]() - Enables to extract rich information from any text (raw, JSON, HTML, YAML, etc).
* [swordfish-rs]() - Mimics real person behavior with realtime typing into terminal; uses a screenplay where text and timings are specified.
* [teip]() - Select partial standard input and replace with the result of another command.
* [to-double-quotes]() - Convert matching single-quotes to double-quotes.
* [to-single-quotes]() - Convert matching double-quotes to single-quotes.
* [tuc]() - You want to cut on more than just a character, perhaps using negative indexes or format the selected fields as you want... Maybe you want to cut on lines (ever needed to drop first and last line?)... That's where tuc can help.
* [Ultimate Plumber]() - Helps to interactively and incrementally explore textual data in Linux, by making it easier to quickly build complex pipelines, thanks to a fast feedback loop.
* [ydiff]() - View colored, incremental diff.

## <a name="text-search"></a>Text search

* [ack](https://github.com/beyondgrep/ack3) - A tool like `grep` optimized for programmers; written in Perl, it speeds up searches thanks to skipping non interesting directories, such as `.git`.
* [ag]() - (The silver searcher) is a text search utility targeted to source code; it skips versioning systems data directories; it is inspired by `ack`, but faster.
* [jiq]() - jid on jq - interactive JSON query tool using jq expressions.
* [paragrep](https://github.com/bmc/paragrep) - Greps regular expressions in a text file(s) and prints out the paragraphs containing those expressions; a paragraph is defined as a block of text delimited by an empty or blank line; fully customizable via command line parameters.  
* [ripgrep]() - Recursively searches directories for a regex pattern.
* [ripgrep-all]() - grep in text files but also search in PDFs, E-Books, office documents, zip, tar.gz, etc.
* [sift](https://github.com/svent/sift) - Fast and powerful open source alternative to grep; it targets flexibility and performance: can be as fast as "regular" grep and allows to specify complex expressions to find text.
* [todocheck]() - Static code analyzer for annotated TODO comments.
* [ugrep]() - Ultra fast grep with interactive TUI, fuzzy search, boolean queries, hexdumps and more.
* [vgrep]() - User-friendly pager for grep.

## <a name="todo-manager"></a>Todo managers

* [CLI-Manager]() - Command Line Interface for managing tasks locally on the fly.
* [devtodo](https://github.com/droundy/goopt) - A hierarchical command-line task manager, with data storage in JSON format.
* [Dooit]() - Todo manager with interactive and beautiful UI, and vim keybindings.
* [dstask]() - Single binary terminal-based TODO manager with git-based sync + markdown notes per task.
* [grit]() - A multitree-based personal task manager.
* [iKog](https://github.com/boyska/ikog) - A fully-featured task manager incapsulated within a Python script (just carry around the script to retain all the TODOs). When the script is run, a Python shell is opened, where task-related commands can be entered (ADD, LIST, etc.); a pity that commands are uppercase, which requires the annoying use of the Shift key.
* [mdt]() - A simple command-line markdown todo list manager inspired by t.
* [t]() - A command-line todo list manager for people that want to finish tasks, not organize them.
* [taskbook]() - Tasks, boards & notes for the command-line habitat.
* [taskell]() - Interactive kanban board/task manager.
* [TaskWarrior](https://github.com/GothenburgBitFactory/taskwarrior) - Todo manager with advanced features; dedicated synchronization server available; many plugins and related tools; healthy software project.  
* [td-cli]() - A command line todo manager, where you can organize and manage your todos across multiple projects.
* [todo.txt](https://github.com/todotxt/todo.txt-cli) - Minimalistic todo manager that uses a simple plain text file to keep track of items; implemented as a shell script.  
* [todolist]() - A minimal clone of [Wunderlist](https://www.wunderlist.com/), with 30% of its features. GTD oriented. It stores the task list in a hidden JSON file in the home directory, making it easy to backup or share them.
* [todotxt-machine](https://github.com/AnthonyDiGirolamo/todotxt-machine) - Interfacce for todo.txt.
* [topydo]() - A powerful todo list application for the console, using the todo.txt format.
* [tsk]() - Terminal task management app with an emphasis on simplicity, efficiency and ease of use.
* [TuDu](https://github.com/meskio/tudu) - A comand line interface to manage hierarchical todos.  Each task has a title, a long text description, a deadline (tudu warns you when the date is close), and a scheduled date. There are categories and priorities.
* [Ultralist](https://github.com/ultralist/ultralist) - A simple, powerful, open source task management system for the command line.
* [xit]() - A plain-text file format for todos and check lists. So, not really a program, but I believe it is worth to list :-)
* [Yokadi](https://github.com/agateau/yokadi) - Project-based todo manager: every task must be specified with a mandatory project indication. Tasks are stored within a SQLlite DB. Written in Python.  

## <a name="torrent"></a>Torrent

BitTorrent clients.

* [Deluge](https://git.deluge-torrent.org/deluge) - A lightweight, Free Software, cross-platform BitTorrent client; a terminal curses interface, web interface and command line client can connect to a running daemon to manage torrent downloads.
* [Mabel]() - Deriving its name from the Hebrew word "מבול," meaning flood, deluge, or (loosely) torrent, Mabel is a fancy BitTorrent client for the terminal.
* [rtorrent]() - Bittorrent client uses ncurses and is ideal for use with tmux, screen or dtach.
* [Stig]() - Stig is a client application to connect and control the BitTorrent Transmission client app.
* [torrentCLI]() - Get torrents from the Terminal.
* [Transgression TUI]() - A remote TUI client for the Transmission bittorrent program.
* [Transmission](https://github.com/transmission/transmission) - Fast, easy and free bittorrent client.

## <a name="utility"></a>Utilities

* [asciinema]() - Terminal session recorder.
* [ata]() - Ask the Terminal Anything: OpenAI GPT in the terminal.
* [Autocomplete]() - IDE-style autocomplete for your existing terminal & shell.
* [bbl]() - Read, search Holy Bible in command line.
* [bible]() - Read the Holy Bible via the command line.
* [chatgpt]() - Simple command line integration to Chat GPT.
* [cligpt]() - ChatGPT but in the terminal.
* [Clipboard]() - Cut, copy, and paste anything, anywhere, all from the terminal! Save time and effort the easy way.
* [Cloudcash]() - Check your cloud spending from the CLI, from Waybar, and from the macOS menu bar!
* [cointop]() - A fast and lightweight interactive terminal based UI application for tracking cryptocurrencies.
* [dasht](https://github.com/sunaku/dasht) - Search API docs offline, in your terminal or browser.
* [dateutils](https://github.com/hroptatyr/dateutils) - Dateutils are a bunch of tools that revolve around fiddling with dates and times in the command line with a strong focus on use cases that arise when dealing with large amounts of financial data.
* [flog]() - A fake log generator for log formats such as apache-common, apache error and RFC3164 syslog.
* [Gaze]() - Runs a command, right after you save a file.
* [GoTTY]() - A program to turn CLI tools into web applications; basically, it runs a command and starts a server so that the output can be displayed in a web page.
* [guesswidth]() - Guess the width output without delimiters in commands that output to the terminal.
* [just]() - Handy way to save and run project-specific commands.
* [Keep]() - Simple alerting tool, with declarative syntax and builtin providers.
* [Lakshmi]() - Investing library and command-line interface inspired by the Bogleheads philosophy.
* [mkdesk]() - A program/command to create .desktop files (program launchers) using the terminal.
* [movie]() - A CLI for getting information about a movies and comparing two movies.
* [moviemon]() - A Python program that displays all the information about all your movies in the command line.
* [MyTimer]() - Simple timer for the terminal with timer-mode and alarm.
* [oji]() - Interactive text emoji creator.
* [ora]() - Elegant terminal spinner.
* [peaches]() - A smart switcher for the terminal. Based on tmux.
* [pmenu]() - A dynamic terminal-based menu inspired by dmenu.
* [powerline]() - Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile.
* [Python re(gex)? exercises]() - TUI application intended to help you practice Python regular expressions; there are more than 100 exercises covering both the builtin re and third-party regex module.
* [rofi]() - A window switcher, application launcher and dmenu replacement.
* [rss-cli]() - A unix-inspired cli application for interacting with RSS feeds.
* [sauce]() - A novelty CLI tool that identifies an anime from an image and yields key data about it.
* [shmenu]() - Menu TUI tool written solely in bash.
* [sshto]() - Small bash script to manage your ssh connections. It builds menu (via dialog) from your ~/.ssh/config. It can not only connect but also to run commands, copy files, tunnel ports.
* [Starship](https://github.com/starship/starship) - The cross-shell prompt for astronauts.
* [teetail]() - Like tee, but only the tail goes in the file.
* [termsaver]() - termsaver to enjoy fancy ASCII screensavers like matrix, clock, starwars, and a couple of not-safe-for-work screens.
* [ttyscheme]() - Collection of Color Schemes for the TTY.
* [unix-permissions]() - Swiss Army knife for Unix permissions.
* [upnup]() - A command line utility that generates a LICENSE file in the current working directory.
* [Viddy]() - Modern watch command. Time machine and pager etc.
* [weather-cli]() - Check the weather for your city from the terminal.
* [welcome.sh]() - A nice little script that greets you on every launch, with some helpful (and customizable!) information.
* [yank]() - Reads input from stdin and display a selection interface that allows a field to be selected and copied to the clipboard.

## <a name="versioning"></a>Versioning

* [Bazaar]() - Multiplatform version control system supporting diffferent workflows; it is part of the GNU Project, and it is free software sponsored by Canonical.
* [fossil](https://github.com/drhsqlite/fossil-mirror) - A simple, high-reliability, distributed software configuration management system with these advanced features: project management, built-in web interface, friendly self-hosting, simple networking, all-in-one standalone executable, and much more.
* [gee]() - CLI repository manager and automation tool written in rust.
* [Gistup]() - Create a gist from terminal, then use git to update it.
* [Mercurial](https://www.mercurial-scm.org/repo/hg) - Free, distributed source control management tool.
* [SnowFS]() - A high-performance application and node library for binary file versioning, initially made for the graphics industry.

## <a name="viewers"></a>Viewers

* [bat]() - A cat clone with syntax highlighting and Git integration.
* [cacaview](https://github.com/cacalabs/libcaca) - A library and a program to display JPG, PNG, GIF or BMP images in the terminal using ASCII characters.
* [Canto Curses]() - Curses frontend for [Canto daemon](https://github.com/themoken/canto-next) for RSS feeds.
* [feh](https://git.finalrewind.org/feh) - "X11 image viewer aimed mostly at console users" (cit.); with no fancy GUI, it is controlled via commandline arguments and configurable key/mouse actions.
* [fx]() - Command-line JSON viewer.
* [glow]() - Render markdown on the CLI, with pizzazz!
* [Grip]() - GitHub Readme Instant Preview - Preview markdown files as GitHub would render them.
* [haxor-news]() - Browse Hacker News like a haxor: A Hacker News command line interface (CLI).
* [hexyl]() - Command-line hex viewer.
* [jc]() - Serializes the output of command line tools to JSON.
* [jless](https://github.com/PaulJuliusMartinez/jless) - Command-line JSON viewer designed for reading, exploring, and searching through JSON data.
* [jqview]() - Simplest possible native GUI for inspecting JSON.
* [mdt]() - MarkDown in the Terminal. A markdown viewer with themes defined by JSON files and interactive mode to open links and word-wrapping adaptable to the terminal width.
* [medium-cli]() - Medium for Hackers - Read [medium.com](https://medium.com/) stories in the terminal.
* [mplayer]() - One of the most popular video/audio players around; plays most audio and video formats (using ASCII characters) in the shell; provides a GUI for graphical visualization.  
* [mpv](https://github.com/mpv-player/mpv/) - A cross-platform media player with many features such as frame timing, MKV chapters and subtitles. It is a responsive video player with minimal layout customizable with themes. A good alternative media player to VLC since it can handle almost all the media formats as VLC, but using much less resources.
* [Newsbeuter]() - "The Mutt of RSS Feed Readers": Newsbeuter is an open-source RSS/Atom feed reader for text terminals. Has great configurability and vast number of features, making it a slick and fast feed reader that can be completely controlled via keyboard.
* [Newsboat](https://github.com/newsboat/newsboat) - An RSS/Atom feed reader for the text console. It's an actively maintained fork of Newsbeuter.
* [nom]() - RSS reader for the terminal.
* [ov]() - Feature-rich terminal-based text viewer.
* [rReader]() - RSS reader client with TUI interface.
* [tabview]() - Python curses command line CSV and tabular data viewer.
* [Terminal Markdown Viewer]() - Python based Markdown viewer for the terminal.
* [TerminalImageViewer]() - Small C++ program to display images in a (modern) terminal using RGB ANSI codes and unicode block graphics characters.
* [termv]() - A terminal iptv player written in bash.
* [texel]() - Command line interface for reading spreadsheets inside terminal.
* [Textual Markdown Browser]() - Experimental "Markdown browser" for the terminal, built with Textual.
* [TV]() - Cross-platform CSV pretty printer made to maximize viewer enjoyment.
* [viu]() - Command-line application to view images from the terminal written in Rust.
* [vj]() - JSON Humanizer makes JSON human readable by applying visual formatting.
* [youtube-viewer]() - Lightweight application that searches and streams videos from YouTube.

## <a name="browser"></a>Web browser

* [Amfora]() - Amfora aims to be the best looking Gemini client with the most features. It does not support Gopher or other non-Web protocols.
* [asuka](https://git.sr.ht/~julienxx/asuka) - A Gemini Project client written in Rust with NCurses.
* [Bombadillo](https://tildegit.org/sloum/Bombadillo) - A non-web browser, designed for a growing list of protocols operating outside of the web. Currently supports Gemini, Finger and Gopher.
* [browsh](https://github.com/browsh-org/browsh) - It renders anything that a modern browser can; HTML5, CSS3, JS, video and even WebGL. Its main purpose is to be run on a remote server and accessed via SSH/Mosh or the in-browser HTML service in order to significantly reduce bandwidth and thus both increase browsing speeds and decrease bandwidth costs.
* [cli-arxiv]() - CLI tool for exploring arXiv.
* [Elinks](https://repo.or.cz/w/elinks.git) - "Advanced and well-established feature-rich text mode web browser"; started as a fork of `Links`; it supports background download with queueing, some support from CSS, text box editing in external text editor.
* [gplaces]() - Simple but powerful terminal Gemini client.
* [Graphene]() - A text-based web browser that's a joy to use.
* [Gremlin]() - Gemini browser for the terminal.
* [Links]() - A textual Web browser with tables and frames.  
* [Lynx]() - A highly configurable text-based web browser; one of the oldest CLI browser I'm aware of.  
* [min]() - A Gemini browser with Vim style keyboard navigation, client certificate support and history and bookmarks saved in TSV files.
* [Romulus]() - A cross platform Gemini console client in C# with a simple user interface, interactive menus and mouse support.
* [s]() - Web search from the terminal. Just opens in your browser.
* [Telescope](https://github.com/omar-polo/telescope) - Gemini client with UI that is strongly inspired from Emacs and W3M.
* [w3m](https://sourceforge.net/projects/w3m/) - A text-based web browser as well as a pager like `less`; it can be used as a text formatting tool which typesets HTML into plain text.  

## <a name="webdev"></a>Web development

Static site generators, load test tools..

* [ain]() - An HTTP API client for the terminal.
* [crawley]() - Unix-way web crawler: crawls web pages and prints any link it can find.
* [Discharge]() - Deploy static websites to Amazon S3.
* [http-tanker]() - Terminal application used for API testing; easily create, manage and execute http requests from the terminal.
* [HTTPie]() - HTTPie for Terminal: human-friendly CLI HTTP client for the API era.
* [Hugo](https://github.com/gohugoio/hugo) - The world’s fastest framework for building websites.
* [iola]() - A command-line socket client with REST API. It helps to work with socket servers using your favorite REST client.
* [is-up-cli]() - Check whether a website is up or down using the [isitup.org](https://isitup.org/) API.
* [linkchecker]() - Check links in web documents or full websites.
* [lychee]() - Fast, async, resource-friendly link checker written in Rust.
* [Metalsmith](https://github.com/metalsmith/metalsmith) - An extremely simple static site generator; all functionalities are provided by plugins that can be combined and chained; written and extendable in Javascript.  
* [Mycorrhiza Wiki](https://github.com/bouncepaw/mycorrhiza) - A lightweight file-system wiki engine that uses Git for keeping history.
* [nanoc](https://github.com/nanoc/nanoc) - Static site generator written in Ruby; extremely powerful and customizable; support many formats to generate HTML content.  
* [pageres-cli]() - Capture screenshots of websites in various resolutions. A good way to make sure your websites are responsive.
* [Reachable]() - Check if a domain is up.
* [s3cmd]() - Command line tool for managing Amazon S3 and CloudFront services.
* [siege](https://github.com/JoeDog/siege) - An http load testing and benchmarking utility designed to let web developers stress their code.  
* [snallygaster]() - Tool to scan for secret files on HTTP servers.
* [surge](https://github.com/sintaxi/surge) - Static web publishing on surge.sh CDN.
* [Tsung](https://github.com/processone/tsung) - A multi-protocol distributed load testing tool that can be used to stress HTTP, WebDAV, SOAP, PostgreSQL, MySQL, LDAP and Jabber/XMPP servers.
* [urlhunter]() - Recon tool that allows searching on URLs that are exposed via shortener services.
* [xpe]() - A commandline xpath tool that is easy to use.


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



