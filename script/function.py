from modules import *
def pereschet_all(n):
    n = str(n)
    counter = 0
    for i in n:
        counter += 1
    return counter

code_string_p_a = '\n'.join(['    ' + line for line in inspect.getsource(pereschet_all).split('\n')])

def pereschet_lit(n, a):
    n = str(n)
    a = str(a)
    counter = 0
    for i in n:
        if i == a:
            counter += 1
    return counter

code_string_p_l = '\n'.join(['    ' + line for line in inspect.getsource(pereschet_lit).split('\n')])

def delet(a, k, n): #*что удалять*, кол-во раз, *последовательность символов из которой удалять*
    n = str(n)
    k = int(k)
    a = str(a)
    while k > 0:
        if a in n:
            n = n.replace(a, '', 1)
        k -= 1
    return n

code_string_del = '\n'.join(['    ' + line for line in inspect.getsource(delet).split('\n')])

def delet_all(a, n): #*что удалять*, *последовательность символов из которой удалять*
    n = str(n)
    a = str(a)
    if a in n:
        n = n.replace(a, '')
    return n

code_string_del_all = '\n'.join(['    ' + line for line in inspect.getsource(delet_all).split('\n')])

def spisok(s, n): 
    n = str(n)
    s = str(s)
    vars = {}
    if n[0] != ' ':
        li = n.split(" ")
    else:
        n = n[1:]
        li = n.split(" ")
    vars[s] = li
    var = str(vars)
    var = var.replace('{', '').replace('}', '').replace(':', '=')
    var = var.replace("'", "",1)
    var = var.replace("'", "",1)
    return var

code_string_spis = '\n'.join(['    ' + line for line in inspect.getsource(spisok).split('\n')])

def variuos_pr(n, k): 
    n = str(n)
    count = 0
    k = int(k)
    for i in product(n, repeat = k):
        count += 1 
    return count 

code_string_v_pr = '\n'.join(['    ' + line for line in inspect.getsource(variuos_pr).split('\n')])

def variuos_per(n, k):
    n = str(n)
    k = int(k)
    count = 0
    for i in permutations(n, k):
        count += 1
    return count

code_string_v_per = '\n'.join(['    ' + line for line in inspect.getsource(variuos_per).split('\n')])

def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Ошибка: деление на ноль!"

    # Простой пользовательский интерфейс
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выйти")

        choice = input("Введите номер операции (1/2/3/4/5): ")

        if choice == '5':
            print("Выход из калькулятора.")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            else:
                print("Некорректный ввод. Пожалуйста, выберите операцию от 1 до 5.")
        else:
            print("Некорректный ввод. Пожалуйста, выберите операцию от 1 до 5.")

code_string_calc = '\n'.join(['    ' + line for line in inspect.getsource(calculator).split('\n')])

def window(x, y): #*ширина* и *высота* окна


    # Создание главного окна
    root = tkinter.Tk()
    root.title("Название окна")

    # Задание размеров окна
    width = x
    height = y
    root.geometry(f"{width}x{height}")

    # Запуск основного цикла событий
    root.mainloop()

code_string_window = '\n'.join(['    ' + line for line in inspect.getsource(window).split('\n')])

def basic_vidjets(): #базовый набор виджетов для окна
    #root - переменная в которой хранится само "окно", разумно, что без шаблона "окно" шаблон "базовые виджеты" не имеет смысла
    #Метод pack() используется для упаковки (размещения) виджета внутри родительского контейнера (в данном случае, главного окна root).
    #pady=10: это аргумент метода pack, который устанавливает вертикальный отступ (padding) между виджетами.
    def on_button_click():
        label.config(text="Привет, " + entry.get())

    label = tkinter.Label(root, text="Введите ваше имя:")#надпись
    label.pack(pady=10) 
    entry = tkinter.Entry(root)#окно для ввода
    entry.pack(pady=10)
    
    button = tkinter.Button(root, text="Привет", command=on_button_click)#кнопка
    button.pack(pady=10)

code_string_basic_vid = '\n'.join(['    ' + line for line in inspect.getsource(basic_vidjets).split('\n')])   

def add_command(data_to_append):
    # Открываем целевой файл для записи в конец
    with open('script/function.py', 'a') as target_file:
        # Записываем содержимое в конец целевого файла

        target_file.write(data_to_append)
        
def f(a, k):    
    l = a + k    
    return l

code_string_f = '\n'.join(['    ' + line for line in inspect.getsource(f).split('\n')])