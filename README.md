# Paste to Pastebin
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)　<br>
This script may provide you to easily way to paste your text/log etc. to [Pastebin.com](https://pastebin.com).

### Important
Before using this script, you've got to change dev_key to your unique developer API key.
See [https://pastebin.com/api](https://pastebin.com/api).

### Requirement
Python 3 or higher.

### Usage
<pre><code>
    pastebin.py <file>
    pastebin.py [-f | --file] [-t | --title] [-s | --syntax] [-e | --expire] [-l | --login] [-p | --private]
    pastebin.py [-h | --help]
</code></pre>
Options:
<pre><code>
    -f --file <file>        Your paste file.
    -t --title <string>     The name or title of your paste
    -s --syntax <string>    Your paste format.
    -e --expire <string>    The expiration date of your paste.
                            N = Never, 10M = 10 mins, 1H = 1 hour, 1D = 1 day, 2W = 2 weeks,
                            1M = 1 month, 6M = 6 months, 1Y = 1 year.
    -l --login              Your paste will belong to your account.
    -p --private <int>      1 -> Private, 2 -> Unlisted, 0 -> Public. (Default:0)
</code></pre>
Examples:
<pre><code>
    $ python pastebin.py ~/paste.py
      https://pastebin.com/hKDj1gPu
      
    $ python pastebin.py ~/paste.py -t paste.py -s python -l -p 2
      https://pastebin.com/VWFTMg2u
</code></pre>
