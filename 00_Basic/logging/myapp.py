import logging
import mylib  # to import any python file within the cwd

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.doSomething()
    logging.info('Finished')

if __name__ == '__main__':
    main()
