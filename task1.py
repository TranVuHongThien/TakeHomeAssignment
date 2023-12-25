import csv

def calculate_average_age(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            age_sum = 0
            count = 0

            for row in reader:
                try:
                    age = int(row['Age'])
                    age_sum += age
                    count += 1
                except ValueError:
                    print(f"Skipping invalid age value for {row['Name']}.")

            if count > 0:
                average_age = age_sum / count
                print(f"Average age: {average_age:.2f}")
            else:
                print("No valid age values found in the CSV file.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "data.csv"
    calculate_average_age(file_path)
