import zmq

def main():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5558")

    while True:
        # Read user input
        user_input = input("Enter 'start', 'stop', or 'close' to stop the server: ").strip().lower()

        # Check if input is valid
        if user_input not in ["start", "stop", "close"]:
            print("Invalid input. Please enter 'start', 'stop', or 'close'.")
            continue

        # If user input is 'close', break out of the loop and stop the server
        if user_input == "close":
            break

        # Publish the input on the "phase" topic
        publisher.send_string("phase " + user_input)

    # Close the socket and context when done
    publisher.close()
    context.term()

if __name__ == "__main__":
    main()