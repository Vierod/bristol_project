import numpy as np

a = np.array([[[1,2,2],[2,3,3]],[[1,2,3],[1,2,2]],[[2,2,2],[2,3,3]],[[1,2,3],[1,2,2]]])

print(np.unique(a))

cases = []

for k in range(64):

	for i in range(a.shape[0]):
		for j in range(a.shape[1]):
			cases.append(tuple(a[i,j,:]))
			
print(set(cases))

for l in range(20000):

	if tuple(np.array([1,2,3])) in set(cases):
		print("WOOO")
	else:
		print("No...")