import os
import logging
import argparse
import shutil



#need to handle folder already exist error
#need to handle overwrite
#need to add documentation


def initialize_logger(print_to_screen = False):
    """
    Creates a logger

    Args:
        print_to_screen: for printing to screen as well as file
    """

    ###############
    # Basic Setup #
    ###############
    app_title = 'Test'
    version_number = '1.0.0'
    # get the path the script was run from, storing with forward slashes
    source_path = os.path.dirname(os.path.realpath(__file__))
    # create a log filepath
    logfile_name = f'{app_title}.log'
    logfile = os.path.join(source_path, logfile_name)

    # tell the user where the log file is
    print(f'Logfile is {logfile}')

    # more initialization
    logger = logging.getLogger(f'{app_title} Logger')
    logger.setLevel(logging.INFO)
    
    ###############################
    # Formatter and Handler Setup #
    ###############################
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.INFO)
    # formatting information we want (time, logger name, version, etc.)
    formatter = logging.Formatter(f'%(asctime)s - %(name)s {version_number} - '
                                  '%(levelname)s - %(message)s')
    # setting the log file format
    file_handler.setFormatter(formatter)
    # clean up old handlers
    logger.handlers.clear()

    # add handler
    logger.addHandler(file_handler)

    # allowing to print to screen
    if print_to_screen:
        # create a new "stream handler" for logging/printing to screen
        console = logging.StreamHandler()
        logger.addHandler(console)
        # setting the print log format
        console.setFormatter(formatter)

    # return logger so it can be used
    return logger


def parse_arguments():
    """
    Parses arguments provided via command line with argparse

    """
    # setup
    parser = argparse.ArgumentParser(
        prog='BatchRenamer',
        description='Renames files in specified folder')
    parser.add_argument('-fp', '--filepath',
                        required=True, type=str,
                        help='filepath to look at')
    parser.add_argument('-find', '--strings_to_find',
                        action='append',
                        help='Strings to be replaced')
    parser.add_argument('-rep', '--string_to_replace',
                        help='String to replace found strings with')
    parser.add_argument('-n', '--new_folder', 
                        type=str, help="The target folder path")
    parser.add_argument('-cpy', '--copy_files', action="store_true",
                        help="If you want to copy the files")
    parser.add_argument('-ovr', '--overwrite',  action="store_true",
                        help="If you want to overwrite when the files already exist")
    parser.add_argument('-tp', '--filetypes', nargs="+",
                        help="List all file types you want to include")
    parser.add_argument('-pr', '--prefix', default='',
                        type=str, help='If you want to add a prefix to the new files, type here.')
    parser.add_argument('-suf', '--suffix', default='',
                        type=str, help='If you want to add a suffix to the new files, type here.')
    # create a bool argument
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='sets the logger to print to screen')
    # parser
    args = parser.parse_args()
    return args



def modify_file(logger, existing_name, new_name, copy_mode=True, force=False):

    if not force and os.path.exists(new_name):
        logger.info(f'File at {new_name} already exist, operation aborted.')
        return
    
    if existing_name == new_name:
        logger.info(f'Path {existing_name} is the same as {new_name}, operation aborted.')
        return
    
    if copy_mode:
        shutil.copy(existing_name, new_name)
        logger.info(f'Copied file {existing_name} to {new_name}')
    else:
        shutil.move(existing_name, new_name)
        logger.info(f'Moved file {existing_name} to {new_name}')



def process_folder(logger,
                   filepath,
                   new_folder,
                   copy_files,
                   overwrite,
                   filetypes,
                   strings_to_find,
                   string_to_replace,
                   prefix,
                   suffix):

    if not os.path.isdir(filepath):
        logger.error(f'Filepath {filepath} does not exist.')
        return
    
    source_path = 'A FULL FILEPATH YOU WILL CONSTRUCT'
    target_path = 'A FULL FILEPATH YOU WILL CONSTRUCT'

    #find files meet limit
    filenames_to_handle = find_files_meet_limit(logger, filepath, strings_to_find, filetypes)
    if type(filenames_to_handle) == type(None) or len(filenames_to_handle) == 0:
        logger.warning(f'No files meet the limit were found, operation aborted.')
        return
 
    #if new_folder is not offered, files will be put into the original folder
    if type(new_folder) == type(None) or len(new_folder) == 0:
        target_folder_path = os.path.abspath(filepath)

    #if a new_folder is offered, create the folder before create files
    else:
        if not os.path.isdir(new_folder):
            os.makedirs(new_folder)
        target_folder_path = os.path.abspath(new_folder)

    #only handle files meet limit
    for filename_to_handle in filenames_to_handle:
        new_filename = filename_to_handle
        #string_to_replace is '' by defualt
        #it doesn't break anything to apply to all target paths
        #the same thing to prefix and suffix
        for string_to_find in strings_to_find:
            new_filename = new_filename.replace(string_to_find, string_to_replace)
        new_filename = prefix + os.path.splitext(new_filename)[0] + suffix + os.path.splitext(new_filename)[1]

        target_path = os.path.join(target_folder_path, new_filename)
        source_path = os.path.join(os.path.abspath(filepath), filename_to_handle)
        modify_file(logger, source_path, target_path, copy_files, overwrite)
                
                

        
    
def find_files_meet_limit(logger, filepath, strings_to_find, filetypes):

    filenames_to_handle = []
    type_limit = type(filetypes) != type(None) and len(filetypes) != 0
    string_limit = type(strings_to_find) != type(None) and len(strings_to_find) != 0

    for filename in os.listdir(filepath):

        #if types are offered, check if they have the correct extensions
        if type_limit and os.path.splitext(filename)[1] not in filetypes:
            logger.info(f'Filtering files with specific extensions: {type_limit}.')
            #skip those without a correct extension
            continue

        if not string_limit:
            #add all filenames if strings_to_find is not offered
            filenames_to_handle.append(filename)
            #skip extra operation
            continue
        
        #if strings_to_find are offered, check if they contain the strings
        for string_to_find in strings_to_find:
            #add only filenames include required strings
            if string_to_find in filename:
                filenames_to_handle.append(filename)
                logger.info(f"Found string {string_to_find} in qualified file {filename}.")
    return filenames_to_handle


def main(renamer_args):
    # Logger
    logger = initialize_logger(True)
    logger.info('Logger Initiated')
    # Using dictionary here to make it easy to run main with a single arg
    logger.debug = renamer_args['verbose']
    process_folder(
        logger,
        filepath = renamer_args['filepath'],
        new_folder = renamer_args['new_folder'],
        copy_files = renamer_args['copy_files'],
        overwrite = renamer_args['overwrite'],
        filetypes = renamer_args['filetypes'],
        strings_to_find = renamer_args['strings_to_find'],
        string_to_replace = renamer_args['string_to_replace'],
        prefix = renamer_args['prefix'],
        suffix = renamer_args['suffix']
    )


if __name__ == '__main__':
    arguments = parse_arguments()
    # converting argparse data to a dictionary
    renamer_args_dict = {
        'filepath' : arguments.filepath,
        'new_folder' : arguments.new_folder,
        'copy_files' : arguments.copy_files,
        'overwrite' : arguments.overwrite,
        'filetypes' : arguments.filetypes,
        'strings_to_find' : arguments.strings_to_find,
        'string_to_replace' : arguments.string_to_replace,
        'prefix' : arguments.prefix,
        'suffix' : arguments.suffix,
        'verbose' : arguments.verbose
    }
    main(renamer_args_dict)
