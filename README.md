    # Football champion viewer
    #### Video Demo:  <https://youtu.be/jMVnxvtvpWk>
    #### Description: this is a project that shows you, who is the current leader in a country from a user's input, with an additional comment whether it is a leadership in a consecutive season or not.
    ####Firstly, program asks user to input a country.
    ####Then, function league_getter is called.
    To trim and lowercase the name of the country and to check if data for this country's football league is available. if so, it return a shortened name of the league, otherwise exits with a message 'Competition is not available, sorry!'.
    ####Ather that, function team_getter is called to get the shortened name of the league from the previous function, insert it in API link (from https://www.football-data.org) and get a JSON for this league, containing data about current standings there. Function gets short name of a current leader and return f-string 'It is {team_name}!', that is printed by the main function.
    ####Finally, result_compare function starts.
    To compares the output from team_getter with hardcoded names of previous year champions. If it matches, return 'Again!' message, in other case 'After some time! Finally!'. Message is printed by the main function
    ####Testing
    Every function is covered by tests.
    To check the league_getter, test_league_getter gives it some appropriate inputs and awaits corresponding league names. Also, test_sysexit checks whether project exits with a 'Competition is not available, sorry!' message if there is no data for a user input
    To check the team_getter, test_team_getter is implemented, which tries to get the correct output from some valid input
    To check the result_compare, test_result_compare is given a name of a reigning champion and a new leader to assert, if result_compare gives back correct comments