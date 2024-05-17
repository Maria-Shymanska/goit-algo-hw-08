import heapq

def min_cost_to_connect_cables(cables):
    # Перетворюємо список кабелів у мін-купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабеля
    while len(cables) > 1:
        # Виймаємо два найменших кабеля
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)
        
        # Об'єднуємо їх
        cost = first_min + second_min
        total_cost += cost
        
        # Додаємо результат об'єднання назад до купи
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
