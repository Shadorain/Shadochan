###########################################################################

                                Shadochan 1.0
      This is an intensive Script to handle any basic Shado-kun needs!

                  Shado-chan will support in any way I can!
          Shado-kun shouldn't have to worry about pointless stuff,
                              I'll help you :)!

############################################################################

Usage:
    shadochan todo list [ --cat <type> ] FILE
    shadochan todo add <category> <due_date> <description> [ -n <notes> ] FILE
    shadochan todo ( new | delete ) FILE
    shadochan calc [ -v | -q ] ( sqr | cub ) <x>
    shadochan calc [ -v | -q ] ( add | sub | mul | div | exp ) <x> <y>
    shadochan spent [ -v ] ( init | view )
    shadochan spent log <amount> <category> <message>
    shadochan (-h | --help)
    shadochan --version

----------------------------------------------------------------------------

Global Options:
    --version   Displays current version of Shadochan
    -v          Outputs more than normal
    -q          Only prints main output

----------------------------------------------------------------------------

Todo Options:
    -c, --cat <type>     Only will display rows of specified category
    -n, --notes <notes>  Optional notes [default: ""]
    list                 Displays specified list
    new                  Will add a new file with the name being FILE
    add                  Will be prompted to provide details, creates new item to be added to later specified list
    delete               Will display list with line numbers, will be prompted to delete chosen line

Calc Options:
    <x>         Placeholder for first value
    <y>         Placeholder for second value

Spent Options:
    init        Creates table if not already made
    view        Displays table list
    log         Logs the date, amount, category, and message

----------------------------------------------------------------------------
