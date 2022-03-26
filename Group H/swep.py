#Baseball League

number_of_teams_in_baseball_league = int(input("Enter the number of teams in the Baseball League: "))
baseball_league = []
for i in range(1, number_of_teams_in_baseball_league+1):
    team = {}
    team_name = input(f'Enter the name of number{i} team including the city: ')
    team['Team_name'] = team_name
    wins = int(input(f'How many match was won by the team: '))
    team['wins'] = wins
    loses = int(input(f'How many match was lost by the team: '))
    team['loses'] = loses
    hits = int(input(f'Number of hits by the team: '))
    team['hits'] = hits
    runs = int(input(f'Number of runs by the team: '))
    team['runs'] = runs
    errors = int(input(f'Number of errors by the team: '))
    team['errors'] = errors
    extra_inning_games = int(input(f'Number of extra inning games: '))
    team['extra_inning_games'] = extra_inning_games
    baseball_league.append(team)

# for i in baseball_league:
#     print(i['wins'])

for team in sorted(baseball_league, key=lambda t: t['wins'], reverse=True):
    print("\n")
    print(team['Team_name'], team['wins'], team['loses'], team['hits'], team['runs'], team['errors'], team['extra_inning_games'])


#Football League

print('\n')
number_of_teams_in_football_league = int(input("Enter the number of teams in the football League: "))
football_league = []
for i in range(1, number_of_teams_in_football_league+1):
    team = {}
    team_name = input(f'Enter the name of number{i} team including the city: ')
    team['Team_name'] = team_name
    wins = int(input(f'How many match was won by the team: '))
    team['wins'] = wins
    loses = int(input(f'How many match was lost by the team: '))
    team['loses'] = loses
    ties = int(input(f'Number of ties by the team: '))
    team['ties'] = ties
    touchdowns = int(input(f'Number of touchdowns by the team: '))
    team['touchdowns'] = touchdowns
    field_goals = int(input(f'Number of field_goals by the team: '))
    team['field_goals'] = field_goals
    turnovers = int(input(f'Number of turnovers games: '))
    team['turnovers'] = turnovers
    total_yards_gained = int(input(f'Number of total_yards_gained games: '))
    team['total_yards_gained'] = total_yards_gained
    total_yards_lost = int(input(f'Number of total_yards_lost games: '))
    team['total_yards_lost'] = total_yards_lost
    football_league.append(team)

# for i in football_league:
#     print(i['wins'])

for team in sorted(football_league, key=lambda t: t['wins'], reverse=True):
    print("\n")
    print(team['Team_name'], team['wins'], team['loses'], team['ties'], team['touchdowns'], team['field_goals'], team['turnovers'], team['total_yards_gained'], team['total_yards_lost'])
    
    