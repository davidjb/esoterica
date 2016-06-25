# Esoterica
## A short review of some curious esoteric languages.

---

<!-- .slide: data-background="#00AFFF" -->
## About me

* David Beitey
* @davidjb / @davidjb_
* Developer, Sys Admin, Enthusiast

---

![Arnie](img/arnie.jpg) <!-- .element style="height: 200px" -->

# ArnoldC

Keywords and sytax are quotes from Schwarzenegger movies.

---

~~~bash
LISTEN TO ME VERY CAREFULLY SKYNET
I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE JOHN
GIVE THESE PEOPLE AIR
GET TO THE CHOPPER JOHN
HERE IS MY INVITATION JOHN
GET UP 1
ENOUGH TALK
I'LL BE BACK JOHN
HASTA LA VISTA, BABY

IT'S SHOWTIME
HEY CHRISTMAS TREE CODEATHON
YOU SET US UP 2016
TALK TO THE HAND "Welcome to Codeathon"
TALK TO THE HAND CODEATHON
GET YOUR ASS TO MARS CODEATHON
DO IT NOW SKYNET CODEATHON
TALK TO THE HAND "See you around in"
TALK TO THE HAND CODEATHON

YOU HAVE BEEN TERMINATED
~~~

---

## Output

~~~bash
$ arnoldc src/codeathon.arnoldc
Welcome to Codeathon
2016
See you around in
2017
~~~

---

## Exceptions

~~~
Exception in thread "main" org.parboiled.errors.ParsingException:
WHAT THE **** DID I DO WRONG:
Invalid input ''', expected ' ', '\t', Operand or '"' (line 11, pos 18):
TALK TO THE HAND 'true'
        at org.arnoldc.ArnoldParser.parse(ArnoldParser.scala:203)
        at org.arnoldc.ArnoldGenerator.generate(ArnoldGenerator.scala:10)
        at org.arnoldc.ArnoldC$.main(ArnoldC.scala:21)
        at org.arnoldc.ArnoldC.main(ArnoldC.scala)
~~~

---

## Why use it

* If I was obsessed with Arnie
* If I had a better knowledge of these movies
* Good documentation
* Decent debugging
* Funny exceptions

---

## Why not

* ![MA15+](img/ma-rating.png) <!-- .element class="plain middle" style="height: 150px" -->
* No comment syntax: `# Awww`
* Only has 16-bit signed int variables (!!)
* No less-than operator
* It's written in Java.  Eww.
* Hard to install

---

![TS](img/trumpscript.jpg) <!-- .element style="height: 150px"-->

# TrumpScript

Language based upon speeches, political propaganda and more centered on Donald
Trump.

---

~~~
I tell you now "the codeathon is over"
Make sure "your programs work"
Just tell us you're sure!

Make this year great in "2016"
Make next year better in "2017"

Tell us that "we'll see you soon, in "; say next year?

Even I agree "the codeathon was fun"!
Tell us all that "this script Trumps all others"
Donald took down the web site.
America is great.
~~~

---

## Output

~~~bash
$ TRUMP src/codeathon.ts
Compiled, starting execution
-------------------

the codeathon is over
your programs work
we'll see you soon, in
2017
this script trumps all others
~~~

---

## Exceptions

`2016` is too small a variable, has to be over 1000000:

~~~
Parsing error:
What are you doing on line 2?

  File "/home/david/dev/src/esoterica/langs/TrumpScript/src/trumpscript/tokenizer.py", line 329, in _error
    raise Utils.SystemException(message_code)

trumpscript.utils.SystemException:
Part of the beauty of me is I'm very rich.
~~~

---

## Why use it

* Write programs from common language
* Easily mix in comments (ignores non-keywords)
* Uses Python 3
* Guaranteed single end point to a program

---

## Why not

* No floats and ints must be > 1,000,000
* No i18n
* No Windows support (Trump is non-PC)
* Docs+Wiki disappeared from public repo on Saturday!
* Debugging is awful
* File extension collision with TypeScript

---

![LOLcode](img/lolcode.png)

# LOLCode

I can haz Internet memes as syntax.

---

~~~
~~~

---

## Output

~~~bash
$ lci src/codeathon.lols
~~~

---

### Exceptions

~~~
~~~

---

## Why use it

* Complete language!
* Versioned, well supported and spec docs
* Well supported and great docs
* Whitespace!
* *HILARIOUS*

---

## Why not

* `NUMBR` vs `NUMBAR`
* `IM IN YR LOOPZ UPPIN/NERFIN` don't work yet

---

---

# Python

Or, we just use Python

~~~python
from datetime import datetime
print('%s days til Codeathon!' % (datetime(int(input('Future Year? ')), 6, 25) - datetime.now()).days)
~~~

## Brainf***

---



---

## Ook!

---

    Example

---

## Anguish

Language written entirely in non-printable Unicode characters

* Simple substitution for BF

---

    Example

---


