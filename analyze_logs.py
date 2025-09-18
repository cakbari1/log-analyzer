def analyze_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    errors = []
    for line in lines:
        if "ERROR" in line:
            errors.append(line.strip())

    if errors:
        print("Suspicious entries found:")
        for error in errors:
            print(error)
    else:
        print("No suspicious entries found.")

if __name__ == "__main__":
    log_file = "sample.log"
    analyze_log(log_file)
