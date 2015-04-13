## What is Fortune?

Fortune is a simple Unix program that displays a random message from a database of quotations.

```
$ fortune

"What we see is mainly what we look for."
  ~Unknown
```

This repo contains some fortune database files.

- fortunes: quotes in English, 5472 items
- chinese: quotes in Chinese, 25919 items
- tang300: poems of Tang Dynasty in Chinese, 313 items
- song100: poems of Song Dynasty in Chinese, 95 items

## Install

First install [fortune package](http://linux.die.net/man/6/fortune). If you have already installed it, skip this step. The following is how to do it in Debian/Ubuntu.

```bash
$ sudo apt-get install fortune
# or
$ sudo apt-get install fortune-mod
```

Then install the repo.

```bash
$ git clone git@github.com:ruanyf/fortunes.git
$ sudo mv fortunes/* /usr/share/games/fortunes/
```

## Usage

```bash
$ fortune [OPTIONS] [/path/to/fortunes]
```

Options

```
- -c     Show the cookie file from which the fortune came.
- -f     Print out the list of files which would be searched, but don't print a fortune.
- -e     Consider all fortune files to be of equal size.
```

Example of `-c`

```bash
$ fortune -c

(fortunes)
%
"Don't waste life in doubts and fears."
  ~Ralph Waldo Emerson
```

Example of `-f`

```bash
$ fortune -f

100.00% /usr/share/games/fortunes
    17.21% fortunes
    81.51% chinese
     0.98% tang300
     0.30% song100
```

Example of `-e`

```bash
$ fortune -e chinese fortunes
#  is equivalent to
$ fortune 50% chinese 50% fortunes

$ fortune -e chinese fortunes tang300 song100
#  is equivalent to
$ fortune 25% chinese 25% fortunes 25% tang300  25% song100
```

## How to make your own fortune database file

(1) Write your fortune items into a file.

(2) Append a percent sign (%) after each item. The percent sign should take a new line. The following is an example.

```
A day for firm decisions!!!!!  Or is it?
%
A few hours grace before the madness begins again.
%
A gift of a flower will soon be made to you.
%
A long-forgotten loved one will appear soon.

Buy the negatives at any price.
%
A tall, dark stranger will have more fun than you.
```

(3) Generate the index file.

```bash
strfile -c % your-fortune-file your-fortune-file.dat
```

(4) Move the fortune file and its index file into `/usr/share/games/fortunes/`.

## License

BSD licensed
