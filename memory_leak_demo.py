# memory_leak_demo.py

import time

# Simulated memory leak using a list that never gets cleared
leaky_list = []

def generate_report_simulation():
    print("Starting report generation...")
    for i in range(100000):
        leaky_list.append("Some large data " * 1000)  # Simulate large memory use
        if i % 10000 == 0:
            print(f"Generated part {i}, memory growing...")

    print("Report generation complete.")

if __name__ == "__main__":
    try:
        while True:
            generate_report_simulation()
            time.sleep(2)  # Wait before generating again
    except KeyboardInterrupt:
        print("Process stopped by user.")

