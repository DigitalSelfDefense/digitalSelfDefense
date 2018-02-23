# Private browsing

## Firefox

- Allows tracking protection by default (v57+)
- [Sandboxing the browser](http://www.morbo.org/2017/11/linux-sandboxing-improvements-in.html)

### Hardening firefox

Most of the follwing information has been taken from VikingVPN's [Hardening Mozilla Firefox Quantum For Privacy & Security 2018 Edition](https://vikingvpn.com/cybersecurity-wiki/browser-security/guide-hardening-mozilla-firefox-for-privacy-and-security)

Some basic privacy and security settings

- Set duck [DuckDuckGo](https://duckduckgo.com/) default search engine
- On the privacy and Security page
  - Disable password remember
  - Enable warn when installing add-ons
  - Send `do not track` signal to servers
  - If you are serious about privacy, you should also think about dissabling history
  - Be sure that when a site request your personal certificate:
    - Ask you every time
    - Queries OCSP

### Hardening firefox - Advanced

- Type `about:config` on the search bar, this will open the advanced settings
  - Disable the WebRTC service
    - `media.peerconnection.enabled` = FALSE
  - Disable DES(weak) cipher
    - `security.ssl3.rsa_des_ede3_sha` = false
  - Force TLS 1.2
    - `security.tls.version.min` = 3
  - Require safe negotiation
    - `security.ssl.require_safe_negotiation` = TRUE
    - `security.ssl.treat_unsafe_negotiation_as_broken` = TRUE
  - Disable form autocomplete
    - `browser.formfill.enable` = FALSE
  - Tell firefox to resist fingerprinting
    - `privacy.resistFingerprinting` = TRUE
  - Disable face detection using cameras
    - `camera.control.face_detection.enabled` = FALSE
  - Disable cache to disk
    - `browser.cache.disk.enable` = FALSE
    - `browser.cache.disk_cache_ssl` = FALSE
  - Disable clipboard manipulation
    - `dom.event.clipboardevents.enabled` = FALSE
  - Disable geolocation
    - `geo.enabled` = FALSE
  - Throw away all cookies every time you close the browser
    - `network.cookie.lifetimePolicy` = 2
  - Disable telemtry
    - Search `telemetry` and set all true/false options to false

## Chrome

Go to chrome advanced settings:

- Disable third party cookies
- Enable cookie reset after every browsing session

## Mobile

Give a try to [Firefox Focus](https://www.mozilla.org/en-US/firefox/mobile/), mozillas privacy aware mobile browser, it has integrated  some interesting feautes like:

- Ad and tracking blockers
- Delete  you history wiht a single click
- Fast

Advice: dsable data collecting

- Settings > "send anonymous usage data" > off

## Tracking

### What?

```(plain-text)
If you're not paying for a service, you're the product, not the customer.
```

Sites you visit, time you spent there, articles you read... all these areavailable informations for people that want to know more about you.
They want their version fo your profile to be as complete as possible so thay can sell it for advertising.

### Who?

### How?

- Cookies
- Browser fingerprin
- Personal information

### How to protect you

- Take care of places you visit
- Use tracking protection extensions like:
  - [Privacy badger](https://www.eff.org/privacybadger) (EFF)
  - [Ghostery](www.ghostery.com)
  - [uMatrix](https://addons.mozilla.org/en-US/firefox/addon/umatrix/)
  - [Disconnect](https://addons.mozilla.org/en-US/firefox/addon/disconnect/)
- Ad blocking extension helps also:
  - [uBlock](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)
- Prevent fingerprinting:
  - [Canvas Defender](https://addons.mozilla.org/en-US/firefox/addon/no-canvas-fingerprinting/)

## Search engines

- [Duckduckgo](https://duckduckgo.com/)

## Https

### How to protect you

- [HTTPS Everywhere](https://www.eff.org/https-everywhere)

## VPN

Virtual private networks (vpn)

### Why are they useful

- hide your real IP from the sites you visit, allowing you to prevent censure
- encrypt the trafic before you trafic reaches the network, protecting you from attackers on your own network

### When they can become dangerous

- VPN doesn't make you anonymous, they still know your real identity. If your  online activity requires complete anonimity [TOR](https://www.torproject.org/) may be a better option.

### VPN providers

- [ProtonVPN](https://protonvpn.com) - Available on mobile
- RiseUp
- VikingVpn

## Social networks

### General tips

- Do not use them
- If you use them:
  - Don't use them from mobile devices
  - Provide them as few personal information as possible
  - Provide single use email
  - Don't keep logged in. ANyone with access to you computer will have access to it.

### Facebook

Run away it's evil !

If you need to use it [here](https://www.techlicious.com/tip/complete-guide-to-facebook-privacy-settings/) you have a nice guide about how to improve Facebook's security.
[Wired](https://www.wired.com/video/facebook-security/) did a nice video too.

### Twitter

Possible to create an anonymous account:
These are extremlly simplified explanations of the process, follow them at your own risk

- What do you need:
  - PC with Tails or Qubes and TOR browser installed
  - Single use SIM card + burner phone (Never used before, bought in cash in a place without cameras)
  - Public internet connection in a place with no cameras
  - Anonymous email
- How to do it:
  1. Go to a place with a public network
  1. Try to avoid surveillance cameras
  1. Connect to twitter using TOR browser
  1. Put the SIM card on the phone and activate it
  1. Sign up using your anonymous emaila address an phone number
  1. Have fun ! And never connect this account from a mobile device and use TOR on you main PC

## Downloads

- Open downloaded files in sandboxed environments
- Do not click on any file you haven't requested
- Delete files or move them away from Downloads folder, that will allow you to see all download files easily and detect unexpected files

## Sources

- [Hardening Mozilla Firefox Quantum For Privacy & Security 2018 Edition](https://vikingvpn.com/cybersecurity-wiki/browser-security/guide-hardening-mozilla-firefox-for-privacy-and-security)
