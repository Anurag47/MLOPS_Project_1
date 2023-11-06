import sys
from src.logger import logging

def error_message_details(error, error_details:sys):
    '''
    Docstring
    '''
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = 'Error occured in script [{0}], line number [{1}], error_details [{2}]'.format(file_name, line_no, str(error))

    return error_message


class CustomException(Exception):
    '''
    Docstring
    '''
    def __init__(self, error, error_details:sys):
        super().__init__(error)
        self.error_message = error_message_details(error, error_details)

    def __str__(self):
        return self.error_message


if __name__=='__main__':
    try:
        a=1/0
    except Exception as e:
        logging.exception('Divide by 0 error')
        raise CustomException(e,sys)