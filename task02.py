import heapq

def merge_k_lists(lists):
    # Створюємо мін-купу
    min_heap = []
    
    # Ініціалізуємо мін-купу першим елементом кожного списку
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    merged_list = []
    
    # Виконуємо злиття
    while min_heap:
        # Виймаємо найменший елемент з купи
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # Якщо в цьому списку залишились елементи, додаємо наступний елемент до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_element = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_element, list_idx, element_idx + 1))
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
