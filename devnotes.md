# DEVELOPMENT NOTES: v2.2

## Update Notes:
- GitHub, Replit, UptimeRobot integration - bot is now on replit and kept up 24/7 using UptimeRobot except during development, and GitHub repository now exists
- .md files utilisation - README.md for information on the project (GitHub), and devnotes.md for storing devnotes
- bot token hidden using environment variables
- fixed various typos
- variables now use snake_case
- fixed date calculation errors by importing pytz and setting timezones to Europe/London and subtracting only the date in the calculation, whereas originally time was also subtracted, causing results to round incorrectly
- Created keep_alive.py to handle the webserver and used UptimeRobot to ping the server every 30 mins to keep the bot online

## Upcoming Features:
- New release version 2.2
- Major new release version 3.0

## To Do: v3.0
-  command revamps
-  .json file fighters database
-  data input
-  and more!