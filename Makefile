run: import-schema bottle.py
	python3 bot.py

bottle.py:
	wget http://bottlepy.org/bottle.py

test-bot: import-schema
	python3 testbot.py

import-schema:
	sqlite3 logs < create_tables.sql
	touch import-schema

clean-database:
	sqlite logs < drop_tables.sql
	rm -f import-schema
