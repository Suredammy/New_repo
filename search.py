import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

def binary_search(array, item):
    logging.debug("Function called " + str(array))

    if len(array) == 0:
        return False

    else:
        middle = len(array) // 2
        if array[middle] == item:
            return True
        else:
            if item < array[middle]:
                return binary_search(array[:middle], item)
            else:
                return binary_search(array[middle + 1 :], item)


print(binary_search([17, 20, 26, 31, 44, 54, 55, 65, 77, 93], 77))
