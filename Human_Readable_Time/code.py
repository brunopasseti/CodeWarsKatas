def make_readable(sec):
	h = (sec // 3600)
	sec = (sec % 3600)
	m = (sec // 60)
	sec = (sec % 60)
	return "{:02d}:{:02d}:{:02d}".format(h,m,sec)
  


def test():
	assert make_readable(0) == "00:00:00"
	assert make_readable(5) == "00:00:05"
	assert make_readable(60) == "00:01:00"
	assert make_readable(86399) == "23:59:59"
	assert make_readable(359999) == "99:59:59"
	pass

if __name__ == "__main__":
	test()
	pass