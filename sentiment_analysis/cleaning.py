# coding=utf-8
import codecs
f = open('movies.txt', 'r+')

export_file = codecs.open('test_movie.txt', encoding='utf-8', mode='w+')
for line in f:
	if line.startswith("review/text:"):
		# unicode_str = line.decode('ascii')
		utf8_str = line.encode('utf-8')
		# fix_encoding = lambda line: line.decode('utf8', 'ignore')
		export_file.write(str(utf8_str	)+'\n')
		