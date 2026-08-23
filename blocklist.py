"""
blocklist.py 
This file just contains the blocklist of the JWT tokens.
It will be imported by app and the logout resource so that tokens can be added 
to the blocklist when the user logs out.
"""
# It is better to use the DB or Reddis to store your blocklist because 
# python set() dont persist between restarts. It goes away when you restart the app. 
BLOCKLIST = set()