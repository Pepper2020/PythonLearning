import os
import logging


class BatchRenamer:
    def __init__(self, 
                 filepath          = None,
                 new_folder        = None,
                 copy_files        = False,
                 overwrite         = False,
                 filetypes         = None,
                 strings_to_find   = None,
                 string_to_replace = '',
                 prefix            = None,
                 suffix            = None):
        self.filepath          = filepath
        self.new_folder        = new_folder
        self.copy_files        = copy_files
        self.overwrite         = overwrite
        self.filetypes         = filetypes
        self.strings_to_find   = strings_to_find
        self.string_to_replace = string_to_replace
        self.prefix            = prefix
        self.suffix            = suffix

        self.initialize_logger()


    def initialize_logger(self, print_to_screen = False):
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
        self.logger = logging.getLogger(f'{app_title} Logger')
        self.logger.setLevel(logging.INFO)
        
        ###############################
        # Formatter and Handler Setup #
        ###############################
        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(logging.INFO)
        # formatting information we want (time, self.logger name, version, etc.)
        formatter = logging.Formatter(f'%(asctime)s - %(name)s {version_number} - '
                                    '%(levelname)s - %(message)s')
        # setting the log file format
        file_handler.setFormatter(formatter)
        # clean up old handlers
        self.logger.handlers.clear()

        # add handler
        self.logger.addHandler(file_handler)

        # allowing to print to screen
        if print_to_screen:
            # create a new "stream handler" for logging/printing to screen
            console = logging.StreamHandler()
            self.logger.addHandler(console)
            # setting the print log format
            console.setFormatter(formatter)

        self.logger.info('Logger Initiated')


    def modify_file(self, existing_name, new_name, copy_mode=True, force=False):
        """
        Renames a file if it exists
        Only overwrites files if force is True

        Args:
            existing_name: full filepath a file that should already exist
            new_name: full filepath for new name
            copy_mode: copy instead of rename
            force: allows overwriting files
        """
        pass


    def process_folder(self):
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

        source_path = 'A FILEPATH YOU WILL CONSTRUCT'
        target_path = 'A FILEPATH YOU WILL CONSTRUCT'

        self.modify_file(source_path, target_path, copy_mode=self.copy_files, force=self.overwrite)


if __name__ == '__main__':
    # This part will not be executed when importing
    testing_folder = r"D:\...\testing_files"
    # Create batch renamer object
    br = BatchRenamer(filepath=testing_folder)

    # Example usage for Models
    br.filetypes = '.ma'
    br.prefix = 'M_'
    br.strings_to_find = ['_file_01', '_file_final_new_02']
    br.process_folder()
