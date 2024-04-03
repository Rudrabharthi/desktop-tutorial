import os
import datetime

def datewise(root_folder, start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        folder_name = current_date.strftime('%Y-%m-%d')
        folder_path = os.path.join(root_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        current_date += datetime.timedelta(days=1)

def alphanumeric(root_folder, num_folders_per_letter):
    for letter in range(65, 65 + 26):  # ASCII values for uppercase letters A-Z
        letter = chr(letter)
        for i in range(1, num_folders_per_letter + 1):
            folder_name = f"{letter}-{i:02}"
            folder_path = os.path.join(root_folder, letter, folder_name)
            os.makedirs(folder_path, exist_ok=True)

# Example usage
root_folder_datewise = "E:\RK\ex_of_foc_2_datewise"
root_folder_alphanumeric = "E:\wallpaper\ex_foc_2_alphanumeric"

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 12, 31)
datewise(root_folder_datewise, start_date, end_date)

num_folders_per_letter = 1
alphanumeric(root_folder_alphanumeric, num_folders_per_letter)