def total_salary(file_path):
    try:
        salary_list = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue # Skip empty lines
                try:
                    # Split the line by comma and attempt to convert the salary (index 1) to float
                    salary = float(line.split(",")[1])
                    salary_list.append(salary)

                # Handle cases where the line is malformed (IndexError) 
                # or the salary is not a valid number (ValueError)
                except (IndexError, ValueError):
                    print(f"Skipped incorrect line: {line}")

        # Calculate total sum using the built-in sum() function
        total = sum(salary_list)
        # Calculate average salary
        average = total / len(salary_list) if salary_list else 0.0

        return total, average

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0.0, 0.0


# Usage example:
file_path = "task1/workers.txt"  # Just a string with the file path
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
