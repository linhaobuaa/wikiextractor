#-*-coding: utf-8-*-

urlset = set()
f = open("dbpedia_leader_results.json")
fw = open("dbpedia_leader_results_final.txt", "w")
for line in f:
	data = line.strip().split("|.|")
	url = data[0]
	q2 = data[-1]
	weiyi = url + q2
	if weiyi not in urlset:
		urlset.add(weiyi)
		fw.write("%s\n" % line.strip())
fw.close()
f.close()
