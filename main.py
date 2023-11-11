import customtkinter
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('green')


# добавить в список компьютеры
list_of_pc = ['notebook'
              ]

from robocopy import robocopy

win = customtkinter.CTk()
win.geometry("400x480+300")


def show_info():
    CTkMessagebox(title="Info", message='Все удачно скопировалось')



frame_1 = customtkinter.CTkFrame(master=win, corner_radius=15)
frame_2 = customtkinter.CTkFrame(master=win, corner_radius=15)

frame_1.pack(pady=20, padx=20, fill='both', expand=True)
frame_2.pack(pady=20, padx=20)

# clear_button=customtkinter.CTkButton(master=frame_1, text='clear', command=show_info)
# clear_button.grid(pady=20, padx=10, column=1, row=0)
check1 = customtkinter.CTkCheckBox(master=frame_1, text="Junior_1")
check1.grid(column=1, row=1)

check2 = customtkinter.CTkCheckBox(master=frame_1, text="Junior_2")
check2.grid(column=1, row=2)

check3 = customtkinter.CTkCheckBox(master=frame_1, text="Junior_3")
check3.grid(column=1, row=3)

check4 = customtkinter.CTkCheckBox(master=frame_1, text="Junior_4")
check4.grid(column=1, row=4)

check5 = customtkinter.CTkCheckBox(master=frame_1, text="Junior_5")
check5.grid(column=1, row=5)

check6 = customtkinter.CTkCheckBox(master=frame_1, text="Junior_6")
check6.grid(column=1, row=6)

checkboxes = [check1, check2, check3, check4, check5, check6]

check_middle_0 = customtkinter.CTkCheckBox(master=frame_1, text="Middle_1")
check_middle_0.grid(column=0, row=1)
check_middle_1 = customtkinter.CTkCheckBox(master=frame_1, text="Middle_2")
check_middle_1.grid(column=0, row=2)

check_middle_2 = customtkinter.CTkCheckBox(master=frame_1, text="Middle_3")
check_middle_2.grid(column=0, row=3)

check_middle_3 = customtkinter.CTkCheckBox(master=frame_1, text="Middle_4")
check_middle_3.grid(column=0, row=4)

check_middle_4 = customtkinter.CTkCheckBox(master=frame_1, text="Middle_5")
check_middle_4.grid(column=0, row=5)

check_middle_5 = customtkinter.CTkCheckBox(master=frame_1, text="Middle_6")
check_middle_5.grid(column=0, row=6)

check_high_0 = customtkinter.CTkCheckBox(master=frame_2, text="High_1")
check_high_0.grid(column=0, row=1)
check_high_1 = customtkinter.CTkCheckBox(master=frame_2, text="High_2")
check_high_1.grid(column=0, row=2)

check_high_2 = customtkinter.CTkCheckBox(master=frame_2, text="High_3")
check_high_2.grid(column=0, row=3)

check_high_3 = customtkinter.CTkCheckBox(master=frame_2, text="High_4")
check_high_3.grid(column=0, row=4)

check_high_4 = customtkinter.CTkCheckBox(master=frame_2, text="High_5")
check_high_4.grid(column=0, row=5)

check_high_5 = customtkinter.CTkCheckBox(master=frame_2, text="High_6")
check_high_5.grid(column=0, row=6)

checkboxes.append(check_middle_0)
checkboxes.append(check_middle_1)
checkboxes.append(check_middle_2)
checkboxes.append(check_middle_3)
checkboxes.append(check_middle_4)
checkboxes.append(check_middle_5)

checkboxes.append(check_high_0)
checkboxes.append(check_high_1)
checkboxes.append(check_high_2)
checkboxes.append(check_high_3)
checkboxes.append(check_high_4)
checkboxes.append(check_high_5)


def check():
    for i, checkbox in enumerate(checkboxes):
        if checkbox.get() == 1:
            select_dir = checkbox._text[:-2]
            for x in list_of_pc:
                options = '/s'

                dist = f"\\\\{x}\\c$\\Users\\Администратор\\AppData\\Roaming\\.minecraft\\saves\\{checkbox._text}"
                start_dist = "C:\\pythonProject2" + "\\" + select_dir + "\\" + checkbox._text
                # robocopy.copy(f'C:\pythonProject2\{select_dir}\{checkbox._text}', dist, options='MIR')
                robocopy.copy(start_dist, dist, options)
    show_info()


my_button = customtkinter.CTkButton(master=frame_1, text='Run', command=check)
my_button.grid(pady=20, padx=10, column=0, row=0)

win.mainloop()
