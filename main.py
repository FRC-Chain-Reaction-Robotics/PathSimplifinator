import csv
import math

def dist(x1, y1, x2, y2):
	return math.sqrt(abs(y2-y1)**2 + abs(x2-x1)**2)

def find_TTA(x1, y1, x2, y2, x3, y3):
	lx1 = x2-x1
	lx2 = x3-x2
	ly1 = y2-y1
	ly2 = y3-y2
	
	try: # jank
		return math.degrees(math.acos(
			(lx1*lx2 + ly1*ly2)
			/ math.sqrt((lx1**2 + ly1**2) * (lx2**2 + ly2**2))
		))
	except:
		return 0

def main():
	rows = []

	with open("Pathweaver/Paths/test.path", 'r') as csvfile:
		csvreader = csv.reader(csvfile)

		for row in list(csvreader):
			rows.append(row)

	# ignoring the first line
	rows = rows[1:]
	rows.append(rows[-1])

	if len(rows) == 2:
		for i in range(len(rows)-1):
			x1, y1 = float(rows[i][0]), float(rows[i][1])
			x2, y2 = float(rows[i+1][0]), float(rows[i+1][1])

			print(dist(x1, y1, x2, y2))
	else:
		for i in range(len(rows)-2):
			x1, y1 = float(rows[i][0]), float(rows[i][1])
			x2, y2 = float(rows[i+1][0]), float(rows[i+1][1])
			x3, y3 = float(rows[i+2][0]), float(rows[i+2][1])

			print("Drive", dist(x1, y1, x2, y2))
			print("Turn", find_TTA(x1, y1, x2, y2, x3, y3))

if __name__ == "__main__":
	main()