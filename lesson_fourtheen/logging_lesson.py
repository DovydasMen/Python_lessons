import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="%d/%m/%Y %H:%M:%S")
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def add_few_number(a: int, b: int) -> int:
    logging.debug(f" Recieved numbers: a {a} and b {b}")
    return a+b

add_few_number(a=6, b=7)
add_few_number(a=6, b=8)

# def money_collected(amount: float) -> None:
#     logging.info(f"Ammounf of money recieved {amount}")
#       if amount == 0:
#            logging.warning("Expected amount larger than 0")
#            #doing smth else


# try:
#     #some code here
# except Exception as e:
#     logging.error(f"Error recieved {e}")



def emergancy_stop(is_stop_event: bool) -> None:
    if is_stop_event:
        logging.critical(f"Had to stop device due to unexpected stop event")
        #func stop


emergancy_stop(True)