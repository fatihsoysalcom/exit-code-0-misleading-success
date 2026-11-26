import sys
import os

def process_file(filename):
    """
    Simulates processing a file. This function will always indicate an internal
    'success' to the calling script, but its actual outcome depends on file existence.
    """
    if not filename:
        sys.stderr.write("Error: No filename provided for processing.\n")
        return False # Internal logic indicates failure

    if os.path.exists(filename):
        sys.stdout.write(f"INFO: Successfully processed data from '{filename}'.\n")
        # In a real application, actual file operations would occur here.
        return True  # Internal logic indicates success
    else:
        sys.stderr.write(f"WARNING: File '{filename}' not found. No processing performed.\n")
        return False # Internal logic indicates failure

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: python main.py <filename_to_process>\n")
        sys.stderr.write("       (Try with 'existing_file.txt' and 'non_existing_file.txt')\n")
        sys.exit(0) # Even for missing arguments, we exit 0 to emphasize the point.

    target_filename = sys.argv[1]

    # Create a dummy file if the specific name 'existing_file.txt' is used
    # to allow for a 'successful' internal run demonstration.
    if target_filename == "existing_file.txt":
        with open(target_filename, "w") as f:
            f.write("This is some dummy content for processing.\n")
        sys.stdout.write(f"INFO: Created dummy file '{target_filename}' for demonstration.\n")

    # Call the function that simulates a task.
    # The return value of process_file indicates its internal success/failure.
    task_completed_internally = process_file(target_filename)

    # This is the core demonstration of the article's concept:
    # The program *always* exits with code 0, regardless of whether the
    # intended task (processing the file) was actually performed or failed internally.
    # A user relying solely on the exit code would be misled.
    sys.exit(0) # Always exit with 0, masking potential internal issues.