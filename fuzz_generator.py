import datetime
import random
import string
import concurrent.futures
import logging

def fuzz_generator(symbols,word_length:int):
        res = random.choices(symbols,k=word_length)
        return(''.join(res))


# def exec_process(symbols,word_length:int,words_amount:int=10):
#     start = datetime.datetime.now()
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         futures = []
#         for i in range (words_amount):
#             futures.append(executor.submit(fuzz_generator,symbols,word_length))
#         for future in concurrent.futures.as_completed(futures):
#             res=future.result()
#             print(res)
#     finish=datetime.datetime.now()
#     print("Execution speed(concurrency-Process)",finish-start)


def exec_thread(symbols,word_length:int,words_amount:int=10):
    logging.basicConfig(level=logging.DEBUG)
    start = datetime.datetime.now()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range (words_amount):
            futures.append(executor.submit(fuzz_generator,symbols,word_length))
        for future in concurrent.futures.as_completed(futures):
            res=future.result()
            print(res)
    finish=datetime.datetime.now()
    execution_speed = finish-start
    logging.debug(f"Execution_speed = {execution_speed}")



# def gener_yield(symbols,word_length:int,words_amount:int=10):
#     for i in range(words_amount):
#         yield fuzz_generator(symbols,word_length)
#
#
# def exec_yield(symbols,word_length:int,words_amount:int=10):
#     start = datetime.datetime.now()
#     res = gener_yield(string.ascii_lowercase + string.digits, 20, 10)
#     for el in list(res):
#         print(el)
#     finish = datetime.datetime.now()
#     print("Execution speed(yield)",finish - start)



if __name__=="__main__":
    # exec_process(string.ascii_lowercase+string.digits,20,10)
    exec_thread(string.ascii_lowercase + string.digits, 20,10)
    # exec_yield(string.ascii_lowercase + string.digits, 20,10)



