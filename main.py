import heapq


def get_minimum_cost_order(cables):
    total_cost = 0
    cables_order = []
    heapq.heapify(cables)

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        merge_cost = cable1 + cable2
        total_cost += merge_cost

        heapq.heappush(cables, merge_cost)
        cables_order.append((cable1, cable2))

    return total_cost, cables_order
