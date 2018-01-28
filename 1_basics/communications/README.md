# Communications

## Security by default

### Love encryption

Allways use secure communications, even when the contents are not important. That creates lot more trafic that needs to be analyzed and decrypted making harder for any attacker to obtain critical information.

### Updates

Update you software whenever is possible.

## End to end encryption

### What is encryption

Taking plaintext and a random generated key and performing mathematical operations to hide it's original content.
Decryption is taking the ciphered test, and WITH THE CORRECT KEY performing mathematical operations to recover the original plaintext.

### What does it protect me from?

Someone that wants to look at the data

### What does it NOT protect me from? Limits of the encryption

If the device is already compromised (Key logger, surveiled...).
Anyone surveying the network (live or just stocking the information) will still know that I talked with you today at 22h for 35 minutes
They will know that after I called my doctor
They will know that then I visited a pharmacy web site

### How does it work?

Only the persons taking part on the conversation can decrypt the message, not the service providers.

1. Marie and Robert want to hide the content of their conversations
1. Marie and Robert will generate each of them a couple of keys, a public key and a private key.
1. They will give each other their public keys
1. When Marie wants to send an email to Robert she will encrypt it with Roberts public key

### End to End vs Transport encryption

Transport encryption means that the information is encrypted while it's travelling on the network, the provider can still see the content.

End to End ecryption means that only the individuals taking part on the conversation are able to see it.

## Instant messaging

### Signal

#### Why?

End to end encryption
Created by a non-profit organization
Open source

#### What does it do?

- Messages and calls
- Encrypt messages BETWEEN SIGNAL USERS, doesn't encrypt standard SMS
- Allows group conversations
- Has a desktop version
- Send disappearing messages
- Disable lock-screen notifications

Even if it's my recommendation for personal isntant messaging, they aren't perfect and therefore they need to stroe some minimal metadata on their servers.

#### Safety numbers...

It allows you to verify that the conversation hasn't been intercepted by someone

#### What does it doesn't do?

- Encrypt old SMS communications
- Encrypt  messages on the phone, this requires disk encryption.
- It's useless if the device is already compromised

### WhatsApp

#### What does it do?

- Shares information with Facebook
- Messages and calls
- Allows group conversations
- Has a desktop version
- More widely used than Signal

### Facebook private messaging

## Email

### Secure email

#### HTTPS

Don't open your email never with a non https connection.

#### Two factor authentication  2FA

What it is ?

You login with two different elements:
These elements usually are somehting you  know (passphrase) and something you have (your phone)

How  to use it?

Most email and social network providers allow you to activate it

#### From field

If an email seems supicious, check the FROM field, before anything else.
The attacker may have used an address similar to the original, carefully check the spelling.

#### Attachements

First rule: try to don't download an attachement, specially if it isn't something you have been waiting for!
Second rule: if you need to open an attachement try to open it on a safe environment (Google drive), a  computer that isn't connected to the network, a virtual machine...
Take care specially of `.js`  and `.wsh` files. Set your browser  settings to don't run automatically these files or configure your OS to use a text editor.

#### Links

Avoid clicking links on emails.
Validate that the domain exists and you know it.
Specially if they are  shrotened urls.

### Encrypted email - PGP

#### What is encrpyted and what isn't

- Subject: Use generic subjects don't include any specific information

#### Doucle check security

- Verify public key fingerprint
- Verify friends public key

### How does it work

### Anonymous email

#### Rise Up

Requires invitation

##### What does it do?

- Email
- VPN
- Won't give infromation to any third party,  including governments
- Won't save logs, making hard to obtain information about real owners of the accounts
- Provide mailing lists

#### Tutanota

##### What does it do?

- Web, android and iPhone apps
- Emails are stored encrypted on their servers and on the device if using their app
- Automatically encrypts emails between tutanota users
- [Allows to easily send encrypted emails to anyone](https://tutanota.uservoice.com/knowledgebase/articles/470795-how-do-i-send-an-encrypted-email-to-an-external-re)
- No PGP, custom protocol that uses RSA and AES

#### Protonmail

## Calls

### Voice calls

Your standard voice calls aren't ciphered.

### VoIP calls

Some providers that offer voice calls:

- Signal
- Whatsapp

## Remember,remember...

If your, or any person you love, physical security or freedom depends or may depend on the information you want to share, don't do it online.
Allways prefer to see your interlocutor in person and in a safe place when possible.

## Related  articles

- [Attack of the Week: Group Messaging in WhatsApp and Signal](https://blog.cryptographyengineering.com/2018/01/10/attack-of-the-week-group-messaging-in-whatsapp-and-signal/)

## Sources

- [Freedom of the press - Email secuirity tips](https://freedom.press/training/email-security-tips/)
- [EFF - Communicating with others](https://ssd.eff.org/en/module/communicating-others)
- [RiseUp - OpenPGP](https://riseup.net/en/security/message-security/openpgp)
