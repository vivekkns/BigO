import random
import heapq


def merge(lists):
    merged_list = []
    heap = [(lst[0], li, 0) for li, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, li, ei = heapq.heappop(heap)
        merged_list.append(val)

        if ei < len(lists[li]) - 1:
            heapq.heappush(heap, (lists[li][ei+1], li, ei+1))

    return merged_list


if __name__ == '__main__':
    lists = []
    for _ in range(5):
        lists.append(sorted(random.sample(range(1, 100), 3)))

    print(lists)
    print(merge(lists))
