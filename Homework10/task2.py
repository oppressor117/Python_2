class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        matching_numbers = []
        for num in list1:
            if num in list2:
                matching_numbers.append(num)

        if len(matching_numbers) != 0:
            print(f'Совпадающие числа: {matching_numbers}')
            print(f'Количество совпадающих чисел: {len(matching_numbers)}')
        else:
            print("Совпадающих чисел нет.")


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()













