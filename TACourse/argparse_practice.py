import argparse

def main():
    parser = argparse.ArgumentParser(description="Test Function")
    parser.add_argument("name", help="Your name")
    parser.add_argument("pronounce", help="Your pronounce")
    parser.add_argument("-g", "--greeting", default="Hello", help="Greeting message")
    parser.add_argument("-o", "--order", default="None", help="Order your dish")
    args = parser.parse_args()
    if (args.order == "None"):
        print(f"{args.greeting}, {args.pronounce} {args.name}!")
    else:
        print(f"{args.greeting}, {args.pronounce} {args.name}! Here is your order: {args.order}")

if __name__ == "__main__":
    main()



# prog -- The name of the program (default: os.path.basename(sys.argv[0]))
# usage -- A usage message (default: auto-generated from arguments)
# description -- A description of what the program does
# epilog -- Text following the argument descriptions
# parents -- Parsers whose arguments should be copied into this one
# formatter_class -- HelpFormatter class for printing help messages
# prefix_chars -- Characters that prefix optional arguments
# fromfile_prefix_chars -- Characters that prefix files containing additional arguments
# argument_default -- The default value for all arguments
# conflict_handler -- String indicating how to handle conflicts
# add_help -- Add a -h/-help option
# allow_abbrev -- Allow long options to be abbreviated unambiguously
# exit_on_error -- Determines whether or not ArgumentParser exits with error info when an error occurs