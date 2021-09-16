# dash_latest
Been working on a CLI dashboard for over a year, decided to rework everything from scratch :)

## CHANGELOG

### v1.1.2

**Added** <br/>
- Error messages when entering an invalid/unavailable command
- Added `rest(n)` function (more info in **changes** section)
- Added a `kill` command which shuts down the dashboard
- Added a 'fixes' section to the changelog

**Changes** <br/>
- Replaced every `s.sleep(n)` line with new `rest(n)` function for better/easier formatting
- Updated development overview
- As seen in the source code, I put a note containing a print funtion for a protip setting, which I will configure later when SQLite is all set up (check development overview for more info)
- Updated the `allCommands` list to prefix a bug that might've appeared later on

**Removed** <br/>
- All `s.sleep(n)` lines (check the **changes** section for more info)

**Fixes** <br/>
- Fixed a few spelling mistakes

### v1.1.1

**Added** <br/>
 None

**Changes** <br/>
- Replaced every print("") line with new enter() function, which is such a small change I don't even know why I'm mentioning it here
- A few minor bug fixes

**Removed** <br/>
- Removed Developer mode midway of creating it because a lot in it was bugged, gonna get reworked soon

### v1.1.0

**Added** <br/>
- Updated main.py file
- Logs setting
- Development overview setting

**Changes** <br/>
- Changed the version variable to v1.1.0 (duh)

**Removed** </br>
  None

*This repository is protected using the Apache 2.0 license. Check LICENSE.md for more information.*
