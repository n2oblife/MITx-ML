def get_sum_metrics(predictions, metrics=None):
	print("-----------------")
	if metrics == None:
		metrics = []
	for i in range(0,3):
		metrics.append(lambda x, i=i : x + i)
		print("la longueur de metrics est", len(metrics))

	sum_metrics = 0
	for i in range(len(metrics)):
				print("i est", i)
				metric = metrics[i]
				print(metric(predictions))
				sum_metrics += metric(predictions)
	return sum_metrics


def main():
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    identite = lambda x : x
    print(get_sum_metrics(3, [identite]))  # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9

if __name__ == "__main__":
    main()
