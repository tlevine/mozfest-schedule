download:
	test -e schedule.json || wget -O schedule.json http://schedule.mozillafestival.org/schedule
unnest:
	python2 reshape.py
