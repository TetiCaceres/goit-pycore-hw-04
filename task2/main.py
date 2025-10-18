def get_cats_info(path) -> list:

    cat_information = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                parts = line.split(",")
                if len(parts) < 3:
                    continue  # Skip lines with missing data

                # Create a dictionary for each cat
                cat_dict = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": int(parts[2]),
                }

                # Add the cat dictionary to the list
                cat_information.append(cat_dict)

    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return cat_information


# Usage example
cats_info = get_cats_info("task2/cats_file.txt")

# Formatted output
print("[")
for cat in cats_info:
    print(f"    {cat}")
print("]")
