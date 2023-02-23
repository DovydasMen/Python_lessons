import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="%d/%m/%Y %H:%M:%S")
logging.basicConfig(level=logging.DEBUG,filename='data_task_two.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# first_sentence = input("Please enter sentence: ")
# secound_sentence = float(input("Please enter float numbers sequance:"))
# third_sentence = int(input("Please define int number :" ))


# def input_logging_machine(sentence_one: str, sentence_two: float, sentence_three: int) -> None:
#     logging.info(f"Client entered {sentence_one} it's data type {sentence_one.__class__}")
#     logging.info(f"Client entered {sentence_two} it's data type {sentence_two.__class__}")
#     logging.info(f"Client entered {sentence_three} it's data type {sentence_three.__class__}")

# try:
#     input_logging_machine(first_sentence, secound_sentence, third_sentence)
# except TypeError:
#     logging.warning(f"You're entered values are incorect")
# except ValueError:
#     logging.warning(f"You'reentered value are incorect")


my_list = [1, 2, 3, 1, 5, 4, 5, 15, 1, 1, 3, 7, 8]
number_to_transfer_to_end = int(input("Define which number to sort to the end: "))

def move_same_elements_in_list_to_end(entered_list: list, number_to_end: int) -> list:
    logging.info(f"This is imported list sample {entered_list}")
    for item in entered_list:
        if item == number_to_end:
            entered_list.remove(item)
            entered_list.append(item)
            logging.info(f"This is how looks list found {entered_list}")
    return entered_list

try:
    move_same_elements_in_list_to_end(my_list, number_to_transfer_to_end)
    logging.info(F"User entered: {number_to_transfer_to_end}")
except TypeError:
    logging.error(f"Entered value is not a list")
except Exception as e:
    logging.debug(f"There is something wrong!!")

