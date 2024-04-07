import os
import logging
import shutil


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
        if not force and os.path.exists(new_name):
            self.logger.info(f'File at {new_name} already exist, operation aborted.')
            return

        if existing_name == new_name:
            self.logger.info(f'Path {existing_name} is the same as {new_name}, operation aborted.')
            return

        if copy_mode:
            shutil.copy(existing_name, new_name)
            self.logger.info(f'Copied file {existing_name} to {new_name}')
        else:
            shutil.move(existing_name, new_name)
            self.logger.info(f'Moved file {existing_name} to {new_name}')


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
        if not os.path.isdir(self.filepath):
            self.logger.error(f'Filepath {self.filepath} does not exist.')
            return
        source_path = 'A FILEPATH YOU WILL CONSTRUCT'
        target_path = 'A FILEPATH YOU WILL CONSTRUCT'
        #find files meet limit
        filenames_to_handle = self.find_files_meet_limit()
        if type(filenames_to_handle) == type(None) or len(filenames_to_handle) == 0:
            self.logger.warning(f'No files meet the limit were found, operation aborted.')
            return
 
        #if new_folder is not offered, files will be put into the original folder
        if type(self.new_folder) == type(None) or len(self.new_folder) == 0:
            target_folder_path = os.path.abspath(self.filepath)

        #if a new_folder is offered, create the folder before create files
        else:
            if not os.path.isdir(self.new_folder):
                os.makedirs(self.new_folder)
            target_folder_path = os.path.abspath(self.new_folder)

        #only handle files meet limit
        for filename_to_handle in filenames_to_handle:
            new_filename = filename_to_handle
            #string_to_replace is '' by defualt
            #it doesn't break anything to apply to all target paths
            #the same thing to prefix and suffix
            for string_to_find in self.strings_to_find:
                new_filename = new_filename.replace(string_to_find, self.string_to_replace)
            new_filename = self.prefix + os.path.splitext(new_filename)[0] + self.suffix + os.path.splitext(new_filename)[1]

            target_path = os.path.join(target_folder_path, new_filename)
            source_path = os.path.join(os.path.abspath(self.filepath), filename_to_handle)
            self.modify_file(self, source_path, target_path, self.copy_files, self.overwrite)

    def find_files_meet_limit(self):    

        filenames_to_handle = []
        type_limit = type(self.filetypes) != type(None) and len(self.filetypes) != 0
        string_limit = type(self.strings_to_find) != type(None) and len(self.strings_to_find) != 0  

        for filename in os.listdir(self.filepath):  

            #if types are offered, check if they have the correct extensions
            if type_limit and os.path.splitext(filename)[1] not in self.filetypes:
                self.logger.info(f'Filtering files with specific extensions: {type_limit}.')
                #skip those without a correct extension
                continue    

            if not string_limit:
                #add all filenames if strings_to_find is not offered
                filenames_to_handle.append(filename)
                #skip extra operation
                continue
            
            #if strings_to_find are offered, check if they contain the strings
            for string_to_find in self.strings_to_find:
                #add only filenames include required strings
                if string_to_find in filename:
                    filenames_to_handle.append(filename)
                    self.logger.info(f"Found string {string_to_find} in qualified file {filename}.")
        return filenames_to_handle

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
