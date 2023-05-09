class Calculator:
    def __init__(self):
        self.memory = None
        self.results = []

    def add(self, x, y):
        result = x + y
        self.memory = result
        self.results.append(result)
        print(result)

    def subtract(self, x, y):
        result = x - y
        self.memory = result
        self.results.append(result)
        print(result)

    def multiply(self, x, y):
        result = x * y
        self.memory = result
        self.results.append(result)
        print(result)

    def divide(self, x, y):
        if y == 0:
            print("Error: division by zero")
        else:
            result = x / y
            self.memory = result
            self.results.append(result)
            print(result)

    def memorize_result(self):
        if self.memory is not None:
            print("Result in memory:", self.memory)
        else:
            print("Memory is empty")

    def show_results(self):
        print("Results:", self.results)

    def show_memory(self):
        if self.memory is not None:
            print("Memory:", self.memory)
        else:
            print("Memory is empty")


            

# создаем объект калькулятора
calc = Calculator()

# выполняем операции
calc.add(5, 3)
calc.subtract(5, 3)
calc.multiply(5, 3)
calc.divide(5, 3)

# сохраняем результат в память калькулятора
calc.memorize_result()

# отображаем результаты операций
calc.show_results()

# отображаем результат, сохраненный в памяти калькулятора
calc.show_memory()