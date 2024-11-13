from tkinter import ttk
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter.font as tkFont
from PIL import Image, ImageTk


class ImpulseLawApp:
    def __init__(self, master):
        self.master = master
        master.title("Закон сохранения импульса")

        # Устанавливаем фиксированный размер окна
        self.master.geometry("700x650")  # Ширина x Высота
        self.master.resizable(False, False)  # Запрет на изменение размера окна

        # Центрируем окно
        self.center_window()

        # Создание объекта шрифта
        font_style = tkFont.Font(family="Helvetica", size=11)

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill='both', expand=True)

        # Вкладка теории
        self.theory_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.theory_tab, text='Теория')
        self.create_theory_tab(font_style)

        # Вкладка примеров
        self.examples_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.examples_tab, text='Примеры')
        self.create_examples_tab()

        # Вкладка вычисления импульса
        self.calculation_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.calculation_tab, text='Вычисление импульса')
        self.create_calculation_tab()

        # Вкладка расчета параметров
        self.parameter_calculation_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.parameter_calculation_tab,
                          text='Расчет параметров')
        self.create_parameter_calculation_tab()

        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

    def on_tab_change(self, event):

        current_tab = self.notebook.index(self.notebook.select())

        if current_tab == 2:  # Вкладка "Вычисление импульса"
            self.mass1_entry.delete(0, tk.END)
            self.velocity1_entry.delete(0, tk.END)
            self.mass2_entry.delete(0, tk.END)
            self.velocity2_entry.delete(0, tk.END)
            self.result_label.config(text="")
            self.demo_button.pack_forget()  # Скрываем кнопку при смене вкладки

        elif current_tab == 3:  # Вкладка "Расчет параметров"
            self.param_result_label.config(text="")
            for widget in self.input_frame.winfo_children():
                widget.destroy()  # Очищаем все поля ввода в параметрах

    def center_window(self):
        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Вычисляем координаты для центрирования окна
        x = (screen_width // 2) - (700 // 2)  # 600 - ширина окна
        y = (screen_height // 2) - (650 // 2)  # 400 - высота окна

        # Устанавливаем позицию окна
        self.master.geometry(f"+{x}+{y}")

    def create_theory_tab(self, font_style):

        theory_text = "Закон сохранения импульса представляет собой ключевую концепцию в физике, которая не только объясняет поведение тел в движении, но и служит основой для          более сложных теорий и приложений."\

        theory_label = tk.Label(
            self.theory_tab, text=theory_text, justify='center', wraplength=600, font=font_style)
        theory_label.pack(padx=20, pady=10)

        self.load_image()

    def load_image(self):
        # Замените 'path/to/your/image.png' на путь к вашему изображению
        image_path = 'ph3.png'
        image = Image.open(image_path)
        # Измените размер изображения по необходимости
        image = image.resize((700, 500), Image.LANCZOS)

        # Конвертируем изображение в формат Tkinter
        self.image_tk = ImageTk.PhotoImage(image)

        image_label = tk.Label(self.theory_tab, image=self.image_tk)
        image_label.pack(pady=10)  # Добавляем изображение в вкладку

    def create_calculation_tab(self):

        self.load_image5()

        self.image_label = tk.Label(self.calculation_tab, image=self.image_tk5)
        self.image_label.grid(row=0, column=2, rowspan=3, padx=10, pady=10)
        # Масса первого тела
        self.mass1_label = tk.Label(
            self.calculation_tab, text="Масса первого тела (кг):")
        self.mass1_label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.mass1_entry = tk.Entry(self.calculation_tab)
        self.mass1_entry.grid(row=0, column=1, padx=5, pady=5)

        # Скорость первого тела
        self.velocity1_label = tk.Label(
            self.calculation_tab, text="Скорость первого тела (м/с):")
        self.velocity1_label.grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.velocity1_entry = tk.Entry(self.calculation_tab)
        self.velocity1_entry.grid(row=1, column=1, padx=5, pady=5)

        # Масса второго тела
        self.mass2_label = tk.Label(
            self.calculation_tab, text="Масса второго тела (кг):")
        self.mass2_label.grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.mass2_entry = tk.Entry(self.calculation_tab)
        self.mass2_entry.grid(row=2, column=1, padx=5, pady=5)

        # Скорость второго тела
        self.velocity2_label = tk.Label(
            self.calculation_tab, text="Скорость второго тела (м/с):")
        self.velocity2_label.grid(row=3, column=0, sticky='e', padx=5, pady=5)
        self.velocity2_entry = tk.Entry(self.calculation_tab)
        self.velocity2_entry.grid(row=3, column=1, padx=5, pady=5)

        # Кнопка для расчета импульса
        self.calculate_button = tk.Button(
            self.calculation_tab, text="Рассчитать импульс", command=self.calculate_impulse)
        self.calculate_button.grid(row=4, column=1, columnspan=1, pady=10)

        # Поле для отображения результатов
        self.result_label = tk.Label(
            self.calculation_tab, text="", wraplength=400)
        # Изменено на 'w' для выравнивания влево
        self.result_label.grid(row=4, column=2, sticky='e', padx=5, pady=10)

        # Кнопка демонстрации столкновения, изначально скрыта
        self.demo_button = tk.Button(
            self.calculation_tab, text="Демонстрация столкновения", command=self.visualize_collision)
        # Изменено на 5 строку
        self.demo_button.grid(row=4, column=0, pady=10)

    def load_image5(self):
        image_path = 'imp.png'  # Укажите путь к вашему изображению
        image = Image.open(image_path)
        # Измените размеры по необходимости
        image = image.resize((200, 100), Image.LANCZOS)
        self.image_tk5 = ImageTk.PhotoImage(image)

    def create_parameter_calculation_tab(self):
        self.parameter_label = tk.Label(
            self.parameter_calculation_tab, text="Выберите тип взаимодействия:")
        self.parameter_label.pack(pady=10)

        self.interaction_var = tk.StringVar()
        self.interaction_dropdown = ttk.Combobox(
            self.parameter_calculation_tab, textvariable=self.interaction_var)
        self.interaction_dropdown['values'] = (
            "Абсолютно упругий удар", "Абсолютно неупругий удар")
        self.interaction_dropdown.pack(pady=10)
        self.interaction_dropdown.bind(
            "<<ComboboxSelected>>", self.update_parameter_options)

        self.parameter_label = tk.Label(
            self.parameter_calculation_tab, text="Выберите параметр для расчета:")
        self.parameter_label.pack(pady=10)

        self.parameter_var = tk.StringVar()
        self.parameter_dropdown = ttk.Combobox(
            self.parameter_calculation_tab, textvariable=self.parameter_var)
        self.parameter_dropdown.pack(pady=10)
        self.parameter_dropdown.bind(
            "<<ComboboxSelected>>", self.update_input_fields)

        self.input_frame = ttk.Frame(self.parameter_calculation_tab)
        self.input_frame.pack(pady=10)

        self.calculate_param_button = tk.Button(
            self.parameter_calculation_tab, text="Рассчитать", command=self.calculate_parameters)
        self.calculate_param_button.pack(pady=10)

        self.param_result_label = tk.Label(
            self.parameter_calculation_tab, text="", wraplength=400)
        self.param_result_label.pack(pady=10)

    def update_parameter_options(self, event):
        interaction_type = self.interaction_var.get()
        if interaction_type == "Абсолютно упругий удар":
            self.parameter_dropdown['values'] = (
                "Конечная скорость первого тела",
                "Конечная скорость второго тела",
                "Начальная скорость первого тела",
                "Начальная скорость второго тела",
                "Масса первого тела",
                "Масса второго тела"
            )
        elif interaction_type == "Абсолютно неупругий удар":
            self.parameter_dropdown['values'] = (
                "Конечная скорость обоих тел",
                "Начальная скорость первого тела",
                "Начальная скорость второго тела",
                "Масса первого тела",
                "Масса второго тела"
            )
        self.parameter_dropdown.set('')  # Сбросить выбор

    def update_input_fields(self, event):
        # Очищаем текст результата при выборе нового параметра
        self.param_result_label.config(text="")  # Сбросить текст результата
        for widget in self.input_frame.winfo_children():

            widget.destroy()

        selected_param = self.parameter_var.get()

        if selected_param in ["Конечная скорость первого тела", "Конечная скорость второго тела", "Начальная скорость первого тела", "Начальная скорость второго тела", "Масса первого тела", "Масса второго тела"]:
            self.create_input_fields_for_final_velocity(selected_param)

    def create_input_fields_for_final_velocity(self, selected_param):

        if selected_param == "Конечная скорость первого тела":
            tk.Label(self.input_frame, text="Масса первого тела (кг):").pack()
            self.mass1_entry_param = tk.Entry(self.input_frame)
            self.mass1_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Скорость первого тела (м/с):").pack()
            self.velocity1_entry_param = tk.Entry(self.input_frame)
            self.velocity1_entry_param.pack()

            tk.Label(self.input_frame, text="Масса второго тела (кг):").pack()
            self.mass2_entry_param = tk.Entry(self.input_frame)
            self.mass2_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Скорость второго тела (м/с):").pack()
            self.velocity2_entry_param = tk.Entry(self.input_frame)
            self.velocity2_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Конечная скорость второго тела (м/с):").pack()
            self.final_velocity2_entry = tk.Entry(self.input_frame)
            self.final_velocity2_entry.pack()

        elif selected_param == "Конечная скорость второго тела":
            tk.Label(self.input_frame, text="Масса первого тела (кг):").pack()
            self.mass1_entry_param = tk.Entry(self.input_frame)
            self.mass1_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Скорость первого тела (м/с):").pack()
            self.velocity1_entry_param = tk.Entry(self.input_frame)
            self.velocity1_entry_param.pack()

            tk.Label(self.input_frame, text="Масса второго тела (кг):").pack()
            self.mass2_entry_param = tk.Entry(self.input_frame)
            self.mass2_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Скорость второго тела (м/с):").pack()
            self.velocity2_entry_param = tk.Entry(self.input_frame)
            self.velocity2_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Конечная скорость первого тела (м/с):").pack()
            self.final_velocity1_entry = tk.Entry(self.input_frame)
            self.final_velocity1_entry.pack()

        elif selected_param == "Начальная скорость первого тела":
            tk.Label(self.input_frame,
                     text="Начальная скорость второго тела (м/с):").pack()
            self.velocity2_entry_param = tk.Entry(self.input_frame)
            self.velocity2_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Конечная скорость второго тела (м/с):").pack()
            self.final_velocity2_entry = tk.Entry(self.input_frame)
            self.final_velocity2_entry.pack()

            tk.Label(self.input_frame, text="Масса первого тела (кг):").pack()
            self.mass1_entry_param = tk.Entry(self.input_frame)
            self.mass1_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Конечная скорость первого тела (м/с):").pack()
            self.final_velocity1_entry = tk.Entry(self.input_frame)
            self.final_velocity1_entry.pack()

            tk.Label(self.input_frame, text="Масса второго тела (кг):").pack()
            self.mass2_entry_param = tk.Entry(self.input_frame)
            self.mass2_entry_param.pack()

        elif selected_param == "Начальная скорость второго тела":
            tk.Label(self.input_frame,
                     text="Конечная скорость второго тела (м/с):").pack()
            self.final_velocity2_entry = tk.Entry(self.input_frame)
            self.final_velocity2_entry.pack()

            tk.Label(self.input_frame, text="Масса первого тела (кг):").pack()
            self.mass1_entry_param = tk.Entry(self.input_frame)
            self.mass1_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Конечная скорость первого тела (м/с):").pack()
            self.final_velocity1_entry = tk.Entry(self.input_frame)
            self.final_velocity1_entry.pack()

            tk.Label(self.input_frame,
                     text="Начальная скорость первого тела (м/с):").pack()
            self.velocity1_entry_param = tk.Entry(self.input_frame)
            self.velocity1_entry_param.pack()

            tk.Label(self.input_frame, text="Масса второго тела (кг):").pack()
            self.mass2_entry_param = tk.Entry(self.input_frame)
            self.mass2_entry_param.pack()

        elif selected_param == "Масса первого тела":
            tk.Label(self.input_frame,
                     text="Начальная скорость второго тела (м/с):").pack()
            self.velocity2_entry_param = tk.Entry(self.input_frame)
            self.velocity2_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Конечная скорость первого тела (м/с):").pack()
            self.final_velocity1_entry = tk.Entry(self.input_frame)
            self.final_velocity1_entry.pack()

            tk.Label(self.input_frame,
                     text="Начальная скорость первого тела (м/с):").pack()
            self.velocity1_entry_param = tk.Entry(self.input_frame)
            self.velocity1_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Конечная скорость второго тела (м/с):").pack()
            self.final_velocity2_entry = tk.Entry(self.input_frame)
            self.final_velocity2_entry.pack()

            tk.Label(self.input_frame, text="Масса второго тела (кг):").pack()
            self.mass2_entry_param = tk.Entry(self.input_frame)
            self.mass2_entry_param.pack()

        elif selected_param == "Масса второго тела":
            tk.Label(self.input_frame,
                     text="Начальная скорость второго тела (м/с):").pack()
            self.velocity2_entry_param = tk.Entry(self.input_frame)
            self.velocity2_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Конечная скорость первого тела (м/с):").pack()
            self.final_velocity1_entry = tk.Entry(self.input_frame)
            self.final_velocity1_entry.pack()

            tk.Label(self.input_frame,
                     text="Начальная скорость первого тела (м/с):").pack()
            self.velocity1_entry_param = tk.Entry(self.input_frame)
            self.velocity1_entry_param.pack()

            tk.Label(self.input_frame,
                     text="Конечная скорость второго тела (м/с):").pack()
            self.final_velocity2_entry = tk.Entry(self.input_frame)
            self.final_velocity2_entry.pack()

            tk.Label(self.input_frame, text="Масса первого тела (кг):").pack()
            self.mass1_entry_param = tk.Entry(self.input_frame)
            self.mass1_entry_param.pack()

    def calculate_parameters(self):
        selected_param = self.parameter_var.get()
        try:
            # Получаем значения из полей ввода
            m1 = float(self.mass1_entry_param.get()
                       ) if 'mass1_entry_param' in dir(self) else None
            m2 = float(self.mass2_entry_param.get()
                       ) if 'mass2_entry_param' in dir(self) else None
            v1 = float(self.velocity1_entry_param.get()
                       ) if 'velocity1_entry_param' in dir(self) else None
            v2 = float(self.velocity2_entry_param.get()
                       ) if 'velocity2_entry_param' in dir(self) else None
            v1_final = float(self.final_velocity1_entry.get()
                             ) if 'final_velocity1_entry' in dir(self) else None
            v2_final = float(self.final_velocity2_entry.get()
                             ) if 'final_velocity2_entry' in dir(self) else None

            # Выполняем расчеты в зависимости от выбранного параметра
            if selected_param == "Конечная скорость первого тела":
                result = ((m2 * v2_final) + (m1 * v1) - (m2 * v2)) / m1
                self.param_result_label.config(
                    text=f"Конечная скорость первого тела: {result:.2f} м/с")

            elif selected_param == "Конечная скорость второго тела":
                result = ((m1 * v1) - (m2 * v2) - (m1 * v1_final)) / m2
                self.param_result_label.config(
                    text=f"Конечная скорость второго тела: {result:.2f} м/с")

            elif selected_param == "Масса первого тела":
                result = ((m2 * v2) - (m2 * v2_final)) / (v1_final - v1)
                self.param_result_label.config(
                    text=f"Масса первого тела: {result:.2f} кг")

            elif selected_param == "Масса второго тела":
                result = (m1 * v1 - m1 * v1_final) / (v2_final - v2)
                self.param_result_label.config(
                    text=f"Масса второго тела: {result:.2f} кг")

            elif selected_param == "Начальная скорость первого тела":
                result = (m1 * v1_final + m2 * v2_final - m2 * v2) / m1
                self.param_result_label.config(
                    text=f"Начальная скорость первого тела: {result:.2f} м/с")

            elif selected_param == "Начальная скорость второго тела":
                result = (m2 * v2_final + m1 * v1_final - m1 * v1) / m2
                self.param_result_label.config(
                    text=f"Начальная скорость второго тела: {result:.2f} м/с")

        except Exception as e:
            self.param_result_label.config(text="Ошибка: " + str(e))

    def create_examples_tab(self):

        self.load_image1()
        self.example1_button = tk.Button(
            self.examples_tab, text="Абсолютно упругий удар", command=self.example_collision_1)
        self.example1_button.pack(pady=10)
        self.load_image2()
        self.example2_button = tk.Button(
            self.examples_tab, text="Абсолютно неупругий удар", command=self.example_collision_2)
        self.example2_button.pack(pady=10)

    def load_image1(self):
        image_path = 'ayp.png'
        image = Image.open(image_path)
        # Замените ANTIALIAS на LANCZOS
        image = image.resize((700, 225), Image.LANCZOS)
        self.image_tk1 = ImageTk.PhotoImage(image)

        image_label = tk.Label(self.examples_tab, image=self.image_tk1)
        image_label.pack(pady=15)

    def load_image2(self):
        image_path = 'any.png'
        image = Image.open(image_path)
        # Замените ANTIALIAS на LANCZOS
        image = image.resize((700, 235), Image.LANCZOS)
        self.image_tk2 = ImageTk.PhotoImage(image)

        image_label = tk.Label(self.examples_tab, image=self.image_tk2)
        image_label.pack(pady=15)

    def validate_inputs(self, m1, v1, m2, v2):
        if m1 <= 0:
            messagebox.showerror(
                "Ошибка", "Масса первого тела должна быть положительной и не равной нулю.")
            return False
        if m2 <= 0:
            messagebox.showerror(
                "Ошибка", "Масса второго тела должна быть положительной и не равной нулю.")
            return False
        if v1 < 0:
            messagebox.showerror(
                "Ошибка", "Скорость первого тела не может быть отрицательной.")
            return False
        if v2 < 0:
            messagebox.showerror(
                "Ошибка", "Скорость второго тела не может быть отрицательной.")
            return False
        return True

    def calculate_impulse(self):
        try:
            m1 = float(self.mass1_entry.get())
            v1 = float(self.velocity1_entry.get())
            m2 = float(self.mass2_entry.get())
            v2 = float(self.velocity2_entry.get())

            if not self.validate_inputs(m1, v1, m2, v2):
                return

            impulse1 = m1 * v1
            impulse2 = m2 * v2
            total_impulse = impulse1 + impulse2

            result_text = (f"Импульс первого тела: {impulse1:.2f} кг*м/с\n"
                           f"Импульс второго тела: {impulse2:.2f} кг*м/с\n"
                           f"Общий импульс: {total_impulse:.2f} кг*м/с")
            self.result_label.config(text=result_text)

            # Активируем вкладки графиков и демонстрации

        except ValueError:
            messagebox.showerror(
                "Ошибка", "Пожалуйста, введите корректные числовые значения.")

    def visualize_collision(self):
        try:
            m1 = float(self.mass1_entry.get())
            v1 = float(self.velocity1_entry.get())
            m2 = float(self.mass2_entry.get())
            v2 = float(self.velocity2_entry.get())

            if not self.validate_inputs(m1, v1, m2, v2):
                return

            # Параметры для анимации
            x1_initial = 0
            x2_initial = 10
            x1 = x1_initial
            x2 = x2_initial

            fig, ax = plt.subplots(figsize=(6, 3))

            fig.canvas.manager.toolbar.pack_forget()

            fig.patch.set_edgecolor('black')  # Устанавливаем цвет рамки
            fig.patch.set_linewidth(2)

            ax.set_xlim(-1, 12)
            ax.set_ylim(-1, 1)
            ax.set_aspect('equal')
            ax.set_facecolor('white')
            ax.axis('off')

            fig.canvas.manager.set_window_title("Демонстрация")

            ball1 = plt.Circle((x1, 0), 0.5, color='#F08080')
            ball2 = plt.Circle((x2, 0), 0.5, color='#87CEFA')
            ax.add_artist(ball1)
            ax.add_artist(ball2)

            root = tk.Tk()
            root.withdraw()  # Скрываем главное окно
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()

            # Получаем размеры окна
            window_width = fig.get_window_extent().width
            window_height = fig.get_window_extent().height

            # Вычисляем позицию для центрирования
            # Преобразуем в int
            x = int((screen_width // 2) - (window_width // 2))
            # Преобразуем в int
            y = int((screen_height // 2) - (window_height // 2)+110)

            # Устанавливаем позицию окна
            fig.canvas.manager.window.wm_geometry(f'+{x}+{y}')

            fig.canvas.manager.window.resizable(False, False)

            # Функция обновления для анимации

            def update(frame):
                nonlocal x1, x2, v1, v2
                # Обновляем позиции шаров
                x1 += v1 * 0.1
                x2 -= v2 * 0.1

                # Проверка на столкновение
                if x1 + 0.5 >= x2 - 0.5:  # Учитываем радиусы шаров
                    # Обработка столкновения (расчет новых скоростей)
                    v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
                    v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
                    v1, v2 = v1_final, v2_final  # Обновляем скорости после столкновения

                    # Перемещаем шары, чтобы они не пересекались
                    x1 = x2 - (0.5 + 0.5)  # Устанавливаем позицию первого шара

                    # Устанавливаем направление движения
                    if v1 > 0:
                        v1 = abs(v1)  # Первое тело движется вправо
                    else:
                        v1 = -abs(v1)  # Первое тело движется влево

                    if v2 > 0:
                        v2 = -abs(v2)  # Второе тело движется влево
                    else:
                        v2 = abs(v2)  # Второе тело движется вправо

                # Проверка на выход за пределы границ
                if x1 < -1 or x1 > 12 or x2 < -1 or x2 > 12:
                    # Сбросим позиции и скорости
                    x1 = x1_initial
                    x2 = x2_initial
                    v1 = float(self.velocity1_entry.get())  # Сброс скорости
                    v2 = float(self.velocity2_entry.get())  # Сброс скорости

                # Обновляем положение шаров
                ball1.center = (x1, 0)
                ball2.center = (x2, 0)

                return ball1, ball2

            # Запускаем анимацию
            ani = animation.FuncAnimation(
                fig, update, frames=np.arange(0, 100), interval=100)
            plt.show()

        except ValueError:
            messagebox.showerror(
                "Ошибка", "Пожалуйста, введите корректные числовые значения.")

    def example_collision_1(self):
        m1, m2 = 2, 2  # Массы для первого примера
        v1, v2 = 4, 4  # Первое тело неподвижно, второе движется

        self.run_collision_animation1(m1, v1, m2, v2)

    def example_collision_2(self):
        m3, m4 = 3, 2  # Массы для второго примера
        v3, v4 = 2, 3  # Шар с большим размером движется к меньшему

        self.run_collision_animation2(m3, v3, m4, v4)

    def run_collision_animation1(self, m1, v1, m2, v2):
        x1_initial = 0
        x2_initial = 10
        x1 = x1_initial
        x2 = x2_initial


# Задаем размер рисунка
        fig, ax = plt.subplots(figsize=(6, 2))

        fig.canvas.manager.toolbar.pack_forget()

        fig.patch.set_edgecolor('black')  # Устанавливаем цвет рамки
        fig.patch.set_linewidth(2)

        ax.set_xlim(-1, 12)
        ax.set_ylim(-1, 1)
        ax.set_aspect('equal')
        ax.set_facecolor('white')
        ax.axis('off')

        fig.canvas.manager.set_window_title("Абсолютно упругий удар")

        ball1 = plt.Circle((x1, 0), 0.5, color='#01A5E7')
        ball2 = plt.Circle((x2, 0), 0.5, color='#FF25AD')
        ax.add_artist(ball1)
        ax.add_artist(ball2)

        root = tk.Tk()
        root.withdraw()  # Скрываем главное окно
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Получаем размеры окна
        window_width = fig.get_window_extent().width
        window_height = fig.get_window_extent().height

        # Вычисляем позицию для центрирования
        x = int((screen_width // 2) - (window_width // 2))  # Преобразуем в int
        # Преобразуем в int
        y = int((screen_height // 2) - (window_height // 2))

        # Устанавливаем позицию окна
        fig.canvas.manager.window.wm_geometry(f'+{x}+{y}')

        fig.canvas.manager.window.resizable(False, False)

        def update(frame):
            nonlocal x1, x2, v1, v2
            x1 += v1 * 0.1
            x2 -= v2 * 0.1

            if x1 + 0.5 >= x2 - 0.5:
                v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
                v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
                v1, v2 = v1_final, v2_final
                x1 = x2 - (0.5 + 0.5)

                if v1 > 0:
                    v1 = abs(v1)
                else:
                    v1 = -abs(v1)

                if v2 > 0:
                    v2 = -abs(v2)
                else:
                    v2 = abs(v2)

            # Проверка на выход за границы
            if x1 < -1 or x1 > 12 or x2 < -1 or x2 > 12:
                # Сброс позиций и скоростей
                x1, x2 = x1_initial, x2_initial
                v1, v2 = 4, 4  # Можно задать начальные скорости заново

            ball1.center = (x1, 0)
            ball2.center = (x2, 0)

            return ball1, ball2

        ani = animation.FuncAnimation(
            fig, update, frames=np.arange(0, 100), interval=100)
        plt.show()

    def run_collision_animation2(self, m3, v3, m4, v4):
        x3_initial = 0
        x4_initial = 10
        x3 = x3_initial
        x4 = x4_initial

        fig, ax = plt.subplots(figsize=(6, 2))
        fig.canvas.manager.toolbar.pack_forget()

        fig.patch.set_edgecolor('black')  # Устанавливаем цвет рамки
        fig.patch.set_linewidth(2)

        ax.set_xlim(-1, 12)
        ax.set_ylim(-1, 1)
        ax.set_aspect('equal')
        ax.set_facecolor('white')
        ax.axis('off')

        fig.canvas.manager.set_window_title("Абсолютно неупругий удар")

        ball3 = plt.Circle((x3, 0), 0.4, color='#01A5E7')
        ball4 = plt.Circle((x4, 0), 0.5, color='#FF25AD')
        ax.add_artist(ball3)
        ax.add_artist(ball4)

        root = tk.Tk()
        root.withdraw()  # Скрываем главное окно
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Получаем размеры окна
        window_width = fig.get_window_extent().width
        window_height = fig.get_window_extent().height

        # Вычисляем позицию для центрирования
        x = int((screen_width // 2) - (window_width // 2))  # Преобразуем в int
        # Преобразуем в int
        y = int((screen_height // 2) - (window_height // 2))

        # Устанавливаем позицию окна
        fig.canvas.manager.window.wm_geometry(f'+{x}+{y}')

        fig.canvas.manager.window.resizable(False, False)

        def calculate_velocities(m3, v3, m4, v4):
            v_final = (m3 * v3 + m4 * v4) / (m3 + m4)
            return v_final, v_final

        def update(frame):
            nonlocal x3, x4, v3, v4
            x3 += v3 * 0.1
            x4 -= v4 * 0.1

            if x3 + 0.3 >= x4 - 0.5:
                v_final = calculate_velocities(m3, v3, m4, v4)
                v3 = v_final[0]
                v4 = v_final[0]
                x3 = x4 - (0.3 + 0.5)

            if x3 < -1 or x3 > 12 or x4 < -1 or x4 > 12:
                # Сброс позиций и скоростей
                x3, x4 = x3_initial, x4_initial
                v3, v4 = 2, 3

            ball3.center = (x3, 0)
            ball4.center = (x4, 0)

            return ball3, ball4

        ani = animation.FuncAnimation(
            fig, update, frames=np.arange(0, 100), interval=100)
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImpulseLawApp(root)
    root.mainloop()
