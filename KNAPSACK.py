s, n = tuple(map(int, input().split()))
v = []
w = []
for _ in range(n):
	wv_new = tuple(map(int, input().split()))
	w.append(wv_new[0])
	v.append(wv_new[1])
	
knapsack_memo = {}

def knapsack_solve(i, w_remaining):
	# i is the number of items avaliable
	if (i, w_remaining) in knapsack_memo:
		return knapsack_memo[(i, w_remaining)]
	if i == 0:
		knapsack_memo[(i, w_remaining)] = 0
		return 0
	if w_remaining == 0:
		knapsack_memo[(i, w_remaining)] = 0
		return 0
	if w[i - 1] > w_remaining:
		knapsack_memo[(i, w_remaining)] = knapsack_solve(i - 1, w_remaining)
		return knapsack_memo[(i, w_remaining)]
	else:
		knapsack_memo[(i, w_remaining)] = max(knapsack_solve(i - 1, w_remaining), 												knapsack_solve(i - 1, w_remaining - w[i - 1]) + v[i - 1])
		return knapsack_memo[(i, w_remaining)]
		
print(knapsack_solve(n, s))
