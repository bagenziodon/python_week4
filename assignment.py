def read_modify_and_save_file():
    # Get the input filename from the user
    input_filename = input("Please enter the filename to read: ")
    output_filename = input("Please enter the filename to save the modified content: ")

    try:
        # Open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read content of the file
        
        # Modify the content (e.g., make all text uppercase)
        modified_content = content.upper()

        # Save the maodified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"Error: Unable to read or write to file. Details: {e}")

# Run the function to process the file
read_modify_and_save_file()
