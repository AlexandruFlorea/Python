import pandas as pd
import os
import time
# import glob


# excel_file_path = input("Enter the full path to the file you want to split: ").strip()
# column_name = input('Enter the column name to filter on: ')
month = 'August 2021'
excel_file_path = r'C:\Users\30213305\Desktop\UTC\Audit reports\Otis\2021_09\Monthly audit report masterfile - Otis test1.xlsx'
column_name = 'Country'
start_time = time.time()
directory = 'Output'
parent_dir = os.path.dirname(excel_file_path)
dir_path = os.path.join(parent_dir, directory)

# Create output directory
try:
    os.mkdir(dir_path)
except OSError as error:
    print(error)
finally:
    print('Moving on')

# Removing duplicate rows
print("Removing duplicate rows")

df = pd.read_excel(excel_file_path)
df.drop_duplicates(subset=None, inplace=True)
df.to_excel(excel_file_path, index=False)

print("Duplicate rows removed")

# Split data per unique values
print(f"Splitting data by {column_name}")
df = pd.read_excel(excel_file_path, header=1, sheet_name="Output_data")

unique_values = df[column_name].unique()
files_to_create = len(list(unique_values))
replace_symbols = ['', ' ', 0]
completed = 0

print(f"""
Files to create: {files_to_create}
Engaging Hyperdrive Core
Approaching Mass Relay""")

# Conditional formatting
def color_coding(cell_value):
    if cell_value in ["Passed", "Compliant"]:
        return f"background-color: lightgreen;"
    elif cell_value in ["Failed   ( No Response )", "Non-compliant"]:
        return f"background-color: #ff7373"
    elif cell_value == "Warning":
        return f"background-color: orange"
    else:
        return None


# Generating files
for unique_value in unique_values:
    df_output = df[df[column_name].replace(replace_symbols, 'Blank').str.contains(unique_value)]
    df_output = df_output.style.applymap(color_coding)
    output_path = os.path.join(dir_path, unique_value + '_Audit report_' + 'Aug 2021' + '.xlsx')
    df_output.to_excel(output_path, sheet_name='Data', index=False)
    completed += 1

    print(f'Generating file: {completed}/{files_to_create}')

# # Applying final touches
# excel_files = glob.glob(os.path.join(dir_path, "*.xlsx"))
#
# for file in excel_files:
#     writer = pd.ExcelWriter(file, engine='xlsxwriter')
#     workbook = writer.book
#     worksheet = writer.sheets["Data"]
#     for i, width in enumerate(get_col_widths(writer)):
#         worksheet.set_column(i, i, width)

runtime = time.time() - start_time
print('--- Program complete ---')
print(f'--- Execution time: {runtime: .02f} seconds ---')
