# Info    
This little program scrapes user-specified RSS feeds for all available article titles, then generates a matrix effect in the terminal that reflects the word count distribution of the scraped data.

- I have only run it on Linux.
- run 'python3 cli.py --help' for execution info. (or read help.txt)
- I have not provided any sample RSS feeds on gh but you can find a sample on this pastebin:
    - https://pastebin.com/Cv1vJQLG
- You can adjust "self.loop_delay" and "self.density_factor" in "grid.py" to manipulate the scroll speed and word density respectively. I might add command line options for this later...
