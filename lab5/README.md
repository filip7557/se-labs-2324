# Lab 6 - Django from scratch

## Merge bez konflikata

Inače povlačite promjene pomoću ove tri naredbe. U ovom slučaju `merge` naredba je izmjenjena tako da ignorira moje izmjene i ostavi vaše u slučaju konflikta. Ovo bi trebalo smanjiti broj konflikata.
Argument ` -Xours ` govori gitu da u slučaju konflikta ostavi naše promjene, a odbaci promjene s upstreama.


```
git remote add upstream https://gitlab.com/levara/se-labs-2324-sr
git fetch upstream master
git merge -Xours upstream/master

```



## Konfiguriraj python virtual environment 

https://realpython.com/python-virtual-environments-a-primer/

Ne zaboravi dodati environment datoteke u ` .gitignore `.


#  Interaktivna vježba

Pratite upute nastavnika
