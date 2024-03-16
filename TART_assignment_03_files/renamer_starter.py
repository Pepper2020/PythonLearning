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
    # create a string argument that is required
    parser.add_argument('-fp', '--filepath',
                        required=True,
                        help='filepath to look at')
    parser.add_argument('-find', '--strings_to_find',
                        action='append',
                        help='Strings to be replaced')
    parser.add_argument('-rep', '--string_to_replace',
                        default='',
                        help='String to replace found strings with')
    # ADD MISSING ARGUMENTS HERE
    parser.add_argument('-n', '--new_folder', 
                        type=str, help="The target folder path")
    parser.add_argument('-cpy', '--copy_files', action="store_true",
                        help="If you want to copy the files")
    parser.add_argument('-ovr', '--overwrite',  action="store_true",
                        help="If you want to overwrite when the files already exist")
    parser.add_argument('-tp', '--filetypes', type = str, 
                        nargs="+", default="None",
                        help="List all file types you want to include")
    # parser.add_argument('-tp', '--filetypes', action="append",
    #                     help="List all file types you want to include")
    # parser.add_argument('-fd', '--strings_to_find', 
    #                     type=str, default="", help='String you want to find in target filenames')
    # parser.add_argument('-rp', '--string_to_replace',
    #                     type=str, help='String you want to replace with.')
    parser.add_argument('-pr', '--prefix',
                        type=str, help='If you want to add a prefix to the new files, type here.')
    parser.add_argument('-suf', '--suffix',
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
    if copy_mode:
        shutil.copy(existing_name, new_name)
    else:
        shutil.move(existing_name, new_name)

    """
    Renames a file if it exists
    Only overwrites files if force is True

    Args:
        existing_name: full filepath a file that should already exist
        new_name: full filepath for new name
        copy_mode: copy instead of rename
        force: allows overwriting files
    """

    '''
    REMINDERS
    # 
    Make sure existing_name is a file using os.path.isfile
    Log an error if file doesn't exist

    Make sure new_name is not already a file using os.path.isfile
    Rename files using shutil.move
    Copy files using shutil.copy
    make sure to import it at the top of the file
    '''
    pass


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
    source_filename = 'A FILENAME YOU WILL CONSTRUCT'
    target_filename = 'A FILENAME YOU WILL CONSTRUCT'

    # logger.info(f"{filepath} is a real direcotry. Here are all files in this folder: ")
    # for filename in os.listdir(filepath):
    #     logger.info(f'Found file {filename} in folder {filepath}.')

    os.makedirs(new_folder)
    if copy_files and type(new_folder) != type(None):
        for filename in os.listdir(filepath):
                new_filename = filename + '_copy'
                source_path = os.path.join(os.path.abspath(filepath), filename)
                target_path = os.path.join(os.path.abspath(new_folder), new_filename)
                shutil.move(source_path, target_path)
                logger.info(f'Copied {source_path} to {target_path}.')
    else:
        if type(strings_to_find) == type(None) or len(strings_to_find) == 0:
            if type(new_folder) == type(None) or len(new_folder) == 0:
                logger.error(f'Trying to copy / move files to the themselves. Operation aborted.')
                return
        
        
            for filename in os.listdir(filepath):
                source_filename = filename
                target_filename = 
                new_filename = filename + '_renamed'
                os.rename(filename, new_filename)
                logger.info(f'Renamed {filename} to {new_filename}.')
        else:
            filenames_to_replace = find_names_with_string_to_replace(logger, filepath, strings_to_find)
            if type(filenames_to_replace) == type(None):
                return
            if type(strings_to_find) == type(None):
                for filename_to_replace in filenames_to_replace:
                    new_filename = new_filename + '_copy'
                    source_path = os.path.join(os.path.abspath(filepath), filename_to_replace)
                    target_path = os.path.join(os.path.abspath(new_folder), new_filename)
                    shutil.copy(source_path, target_path)
                    logger.info(f'Copied {source_path} to {target_path}.')
            else:
                for filename_to_replace in filenames_to_replace:
                    new_filename = filename_to_replace
                    for string_to_find in strings_to_find:
                        new_filename = new_filename.replace(string_to_find, string_to_replace)
                    source_path = os.path.join(os.path.abspath(filepath), filename_to_replace)
                    target_path = os.path.join(os.path.abspath(new_folder), new_filename)
                    logger.info(f'Copying and renamed {source_path} to {target_path}.')
                    shutil.copy(source_path, target_path)
                    logger.info(f'Copied and renamed {source_path} to {target_path}.')
                    


    

    modify_file(logger,
                source_path,
                target_path,
                copy_mode=copy_files,
                force=overwrite)


        
    

                        

                   
    """
    Checks the given folder
    Gathers files in the folder
    Optionally limits files to modify
    Optionally does find and replace
    Optionally adds prefixes and suffixes

    Args:
        filepath: full filepath to a folder to find files in
        new_folder: full filepath to a folder to copy or move files to
        copy_mode: setting to copy files instead of rename them
        filetypes: filetypes to modify
        strings_to_find: list of strings to find in filename
        string_to_replace: string to replace and strings_to_find with
        prefix: string to add to the beginning of all modified files
        suffix: string to add to the end of all modified files
    """

    '''
    REMINDERS
    # FILEPATHS #
    Check to see if the filepath is a valid folder using the os.path.isdir
    Avoid using filepaths with spaces for this assignment
    If new_folder is given, use os.makedirs if it doesn't exist
    Loop through files in a folder using a for loop and os.listdir
    Construct paths using os.path.join rather than string formatting
    
    # LIMITING FILES MODIFIED #
    Limit files modified by using os.path.splittext to get file extension
    Only do this if filetypes argument is provided

    # REPLACING #
    Rename using the .replace string method
    strings_to_find could be empty meaning no replacement should be done
    If strings_to_find is not empty replace every string in strings_to_find
    with the single string from string_to_replace
    To avoid replacing partial strings 
    (e.g. replacing tex before texture)
    use strings_to_find.sort(reverse=True) 
    to put longest strings first

    # PREFIXES AND SUFFIXES #
    Use string formatting
    Add a prefix if given
    Add a suffix if given
    Make sure not to modify the filetype

    # FINAL CHECK #
    Make sure source_path is not the same as target_path
    '''

def find_names_with_string_to_replace(logger, filepath, strings_to_find):
    filenames_to_replace = []
    for filename in os.listdir(filepath):
        for string_to_find in strings_to_find:
            if string_to_find in filename:
                filenames_to_replace.append(filename)
                logger.info(f"Found string {string_to_find} in {filename}.")
    if len(filenames_to_replace) == 0:
        logger.warning(f'No files meet the limit were found.')
        return None
    return filenames_to_replace


def main(renamer_args):
    # Logger
    logger = initialize_logger(True)
    logger.info('Logger Initiated')
    # Using dictionary here to make it easy to run main with a single arg
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
        'suffix' : arguments.suffix
    }
    main(renamer_args_dict)
