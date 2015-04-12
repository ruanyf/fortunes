## How to use

```bash
$ git clone git@github.com:ruanyf/fortunes.git
$ sudo mv fortunes/* /usr/share/games/fortunes/
```

Now you can type `fortune` into your command line to see its effect.

```
$ fortune

"What we see is mainly what we look for."
  ~Unknown
```

## What is Fortune?

Fortune is a simple Unix program that displays a random message from a database of quotations.

Command line Options

- -c     Show the cookie file from which the fortune came.

```bash
$ fortune -c

(fortunes)
%
"Don't waste life in doubts and fears."
  ~Ralph Waldo Emerson
```

- -f     Print out the list of files which would be searched, but don't print a fortune.

```bash
$ fortune -f

100.00% /usr/share/games/fortunes
    17.43% fortunes
    82.57% chinese
```

- -e     Consider all fortune files to be of equal size.

```bash
$ fortune -e funny not-funny
#  is equivalent to
$ fortune 50% funny 50% not-funny
```

## How to make your own fortune file

**Step one**: Put your fortune items into a file.

**Step two**: Append a percent sign (%) after each item. The percent sign should take a new line.

An example.

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

**Step 3**: Generate the index file.

```bash
strfile -c % your-fortune-file your-fortune-file.dat
```

**Step 4**: Move the fortune file and its index file into `/usr/share/games/fortunes/`.

## License

BSD licensed
