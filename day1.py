import pandas as pd
file_path_alt = "C:/Users/Admin/Downloads/student_exam_scores (1).csv"

try:
    df = pd.read_csv(file_path_alt)
    print("--- File Loaded Successfully (using forward slashes) ---")
    print(df.head())

except FileNotFoundError:
    print(f"Error: File not found at path: {file_path_alt}")
except Exception as e:
    print(f"An error occurred: {e}")
    #testing nbvbnvvb