n_4 ="""
21 	36 	37 	2.3
167 	192 	215 	-4.5
242 	471 	479 	1.7
717 	967 	1033 	-1.1
2111 	2285 	2620 	2.4
8191 	16253 	16509 	12.9
16893 	27753 	28660 	1.4
16382 	32506 	33018 	1.6
64493 	85903 	92037 	2.4
49152 	97534 	99070 	-8.1
74191 	118430 	122748 	3.7
"""

n_9  ="""
68 	69 	74 	1.2
279 	392 	394 	1.1
6817 	10727 	10747 	5.3
21860 	25208 	25903 	24.7
43720 	50416 	51806 	3.1
51454 	105711 	105729 	2.1
53490 	69811 	70490 	2.5
"""

n_14 ="""
4433 	4519 	4706 	-1.1
1636734 	2037442 	2044083 	1.6
1441026 	2675720 	2675753 	-4.0
5418289 	6182083 	6247134 	3.4
"""

n_20 ="""
4110 	4693 	4709 	4.3
17764 	22616 	22625 	-1.3
35816 	37074 	37835 	-1.7
255738 	347841 	347878 	2.5
852068 	866702 	890301 	0.3
2674998 	3567225 	3567788 	-1.4
2593096 	2880825 	2897442 	6.1
3198945 	4913429 	4913475 	-1.2
7706288 	7937911 	8114575 	1.1
"""
import unittest
from fermatrieman import getFermatMiss

def lnmake(ln):
	ln_4 = [l.split("\t") for l in ln.split('\n') if len(l) > 4]
	return ln_4

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '%.12f' % f
    i, p, d = s.partition('.')
    v = '.'.join([i, (d+'0'*n)[:n]])

    return float(v)

class TestFermat(unittest.TestCase):
	def test_Fermat_n4(self):
		ln_4l = lnmake(n_4)
		for ln_4 in ln_4l:
			# print(ln_4)
			self.assertIn(getFermatMiss(int(ln_4[0]), int(ln_4[1]),int(ln_4[2]), 4)['miss'],
				 [round(float(ln_4[3]),1),round(float(ln_4[3])+0.1, 1),round(float(ln_4[3])-0.1, 1)]), f"Should be {ln_4[3]}"

	def test_Fermat_n9(self):
		ln_4l = lnmake(n_9)
		for ln_4 in ln_4l:
			self.assertIn(getFermatMiss(int(ln_4[0]), int(ln_4[1]),int(ln_4[2]), 9)['miss'],
				 [round(float(ln_4[3]),1),round(float(ln_4[3])+0.1, 1),round(float(ln_4[3])-0.1, 1)]), f"Should be {ln_4[3]}"

	# def test_Fermat_n14(self):
	# 	ln_4l = lnmake(n_14)
	# 	for ln_4 in ln_4l:
	# 		# print(ln_4)
	# 		self.assertIn(getFermatMiss(int(ln_4[0]), int(ln_4[1]),int(ln_4[2]), 14)['miss'],
	# 			 [round(float(ln_4[3]),1),round(float(ln_4[3])+0.1, 1),round(float(ln_4[3])-0.1, 1)]), f"Should be {ln_4[3]}"
	
	# def test_Fermat_n20(self):
	# 	ln_4l = lnmake(n_20)
	# 	for ln_4 in ln_4l:
	# 		# print(ln_4)
	# 		self.assertIn(truncate(getFermatMiss(int(ln_4[0]), int(ln_4[1]),int(ln_4[2]), 20)['miss'], 1),
	# 			 [round(float(ln_4[3]),1),round(float(ln_4[3])+0.1, 1),round(float(ln_4[3])-0.1, 1)]), f"Should be {ln_4[3]}"

   

if __name__ == '__main__':
    unittest.main()