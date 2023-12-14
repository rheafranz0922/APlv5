import json

# Function to get student details from the user
def get_student_details():
    name = input("Enter student name: ")
    id = input("Enter ID: ")
    course_details = input("Enter your course: ")
    return {"Name": name, "ID": id, "Course": course_details}

# Function to write student details to a JSON file
def write_to_json_file(data, filename='StudentJson.json'):
    try:
        with open(filename, 'r') as file:
            student_details = json.load(file)
        # Append another dictionary to the existing data
        student_details["Student1"] = data
    except FileNotFoundError:
        # If the file doesn't exist, create a new one
        student_details = {"Student1": data}

    with open(filename, 'w') as file:
        json.dump(student_details, file)
    print("Data written to", filename)

# Function to read and display student details from a JSON file
def read_from_json_file(filename='StudentJson.json'):
    try:
        with open(filename, 'r') as file:
            student_details = json.load(file)
            for key, value in student_details.items():
                print(f"\nStudent Details for {key}:")
                print("Name:", value["Name"])
                print("ID:", value["ID"])
                print("Course+details:", value["Course"])
    except FileNotFoundError:
        print(f"{filename} not found. No data to display.")

if __name__ == "__main__":
    # Step 1: Get student details from the user
    get_student_details = get_student_details()

    # Step 2: Write student details to a JSON file
    write_to_json_file(get_student_details)

    # Step 3: Read and display student details from the JSON file
    read_from_json_file()
