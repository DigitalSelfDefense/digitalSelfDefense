---
category: secrets
permalink: /secrets/passwords/
---
# Passwords

This part is different from others, it's a bit shorter and explains what is a safe password and how to store them.

```
Passwords are like underwear: you don't let people see it, you should change it very often, and you shouldn't share it with strangers.
- Chris Pirillo
```

## Secure passwords

Secure passwords don't need to be:

- Hard to remember
- With many special charactes

Secure passwords will:

- Have at least 15 characters (depending on the situation)
- Be random
- Easy to remember

It may look impossible meeting all these conditions at the same time, but... is easier  that it looks like.

### Creating secure passwords

- Prases are easier to remember than words, they are longer and therefore more secure
- Words are easier to remember than isolated characters
- Use words in many languages
- Use proper names
- Add some special characters

There is no [100% secure](https://archive.org/details/how-to-make-a-super-secure-password)

#### Diceware passphrase generation

Roll 5 dices, do it 7 times, check the list.  Get your new password !

1. Search diceware word list EFF has a good one.
    - Download the file and avoid search
1. Roll 5 dices and note the number of each dice (ex. 1,5,3,4,2 (15342))
1. Search the equivalent word that correspond to that number
1. Repeat it 6 times for standard password and 7+ for your more important ones

## Storing passwords

Tools designed to store your passwords encrypted using a master password.

Single point of failure, if it’s compromised = Game Over :(

### On the cloud

Some provider allow you to synchronize on the cloud

- Easier to use across multiple devices
- They ***WILL*** know which service you use and when
- They ***MAY*** know your password

### KeePassX

```(plain-text)
KeePassX is an application for people with extremly high demands on secure personal data management. - KeePassX
```

- Free
- Open Source
- Available in many devices

#### Databases

Passwords are stored  on databases
Each database is protected by a password, key file, or both

|               For               |                       Against                      |
|:-------------------------------:|:--------------------------------------------------:|
| Harder to guess than a password | Like a physical key, if you lose it you are fucked |

#### Mobile devices

Same db can be used across many platforms.
Mobile devices are less secure, copy just the passwords you will need when you are outdoors

## Password maintenance

Passwords should be changed on a regular basis
Don't reuse the same password, or varaitions of it multiple times
