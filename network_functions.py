from typing import List, Tuple, Dict, TextIO


P2F = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'],
       'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'],
       'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'],
       'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'],
       'Alex Dunphy': ['Luke Dunphy'],
       'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'],
       'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
       'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],
       'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],
       'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'],
       'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett',
                       'Phil Dunphy']}


P2N = {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado': ['Chess Club'],
       'Mitchell Pritchett': ['Law Association'],
       'Alex Dunphy': ['Chess Club', 'Orchestra'],
       'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'],
       'Phil Dunphy': ['Real Estate Association'],
       'Gloria Pritchett': ['Parent Teacher Association']}


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
                  person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """

    current_line = profiles_file.readline()
    next_line = profiles_file.readline()
    name = convert_name(current_line.rstrip())
    while next_line != '':
        if ',' in next_line:
            friend = convert_name(next_line.rstrip())
            add_to_friends(name, friend, person_to_friends)
            next_line = profiles_file.readline()
        elif next_line != '\n':
            network = next_line.rstrip()
            add_to_network(name, network, person_to_networks)
            next_line = profiles_file.readline()
        else:
            current_line = profiles_file.readline()
            next_line = profiles_file.readline()
            name = convert_name(current_line.rstrip())


def add_to_friends(name: str, friend: str, person_to_friends: \
                   Dict[str, List[str]]) -> None:
    """Add friend as a value to name in person_to_friends.

    >>> d = {'Meredith Shepherd-Grey': ['Derek Shepherd-Grey'], 'Amelia Hunt': \
['Derek Shepherd-Grey', 'Alex Michael Karev', 'Owen Hunt'], 'Alex Michael Karev': \
['Meredith Shepherd-Grey', 'Amelia Hunt']}
    >>> add_to_friends('Meredith Shepherd-Grey', 'Becky Min', d)
    >>> d
    {'Meredith Shepherd-Grey': ['Derek Shepherd-Grey', 'Becky Min'], 'Amelia Hunt': \
['Derek Shepherd-Grey', 'Alex Michael Karev', 'Owen Hunt'], 'Alex Michael Karev': \
['Meredith Shepherd-Grey', 'Amelia Hunt']}
    >>> e = {}
    >>> add_to_friends('John Smith', 'Jane Doe', e)
    >>> e
    {'John Smith': ['Jane Doe']}
    """

    if name not in person_to_friends:
        person_to_friends[name] = [friend]
    else:
        if friend not in person_to_friends[name]:
            person_to_friends[name].append(friend)


def add_to_network(name: str, network: str, person_to_networks: \
                   Dict[str, List[str]]) -> None:
    """Add network as a value to each name in person_to_networks.

    >>> TEST_NETWORK_1 = {'Meredith Shepherd-Grey': ['Parent Teacher Association'], \
'Amelia Hunt': ['Yachting Association', 'Knitting Club'], 'Alex Michael Karev': \
['Knitting Club', 'Ethics Board'], 'Owen Hunt': ['Yachting Association', \
'Parent Teacher Association', 'Knitting Club']}
    >>> TEST_NETWORK_2 = {'Blair Bass': ['Law Association'], 'Eleanor May Waldorf': \
['Photography Club'], 'Serena van-der-Woodsen': ['Debate Club', 'Law Association']}
    >>> add_to_network('Amelia Hunt', 'Ethics Board', TEST_NETWORK_1)
    >>> TEST_NETWORK_1
    {'Meredith Shepherd-Grey': ['Parent Teacher Association'], 'Amelia Hunt': \
['Yachting Association', 'Knitting Club', 'Ethics Board'], 'Alex Michael Karev': \
['Knitting Club', 'Ethics Board'], 'Owen Hunt': ['Yachting Association', \
'Parent Teacher Association', 'Knitting Club']}
    >>> add_to_network('Damien Dalegard', 'Actuarial Association', TEST_NETWORK_2)
    >>> TEST_NETWORK_2
    {'Blair Bass': ['Law Association'], 'Eleanor May Waldorf': ['Photography Club'], \
'Serena van-der-Woodsen': ['Debate Club', 'Law Association'], \
'Damien Dalegard': ['Actuarial Association']}
    """

    if name not in person_to_networks:
        person_to_networks[name] = [network]
    else:
        if network not in person_to_networks[name]:
            person_to_networks[name].append(network)


def convert_name(name: str) -> str:
    """Convert name to the format 'FirstName LastName'.

    >>> convert_name('Pritchett, Jay')
    'Jay Pritchett'
    >>> convert_name('Smith-Klein, David John')
    'David John Smith-Klein'
    """

    comma = name.find(',')
    last_name = name[0:comma]
    first_name = name[comma + 2: len(name)]
    full_name = first_name + " " + last_name
    return full_name


def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """Return the average number of friends that people who appear as keys in
    person_to_friends have.

    >>> get_average_friend_count({'Meredith Shepherd-Grey': ['Derek Shepherd-Grey'], \
'Amelia Hunt': ['Derek Shepherd-Grey', 'Alex Michael Karev', 'Owen Hunt'], \
'Alex Michael Karev': ['Meredith Shepherd-Grey', 'Amelia Hunt']})
    2.0
    >>> get_average_friend_count({})
    0
    """

    total = 0
    count = 0
    size = len(person_to_friends)

    if size != 0:
        for person in person_to_friends:
            count += len(person_to_friends[person])
        total = count / len(person_to_friends)

    return total


def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a dictionary containing all people from person_to_friends sorted
    by last name.

    >>> get_families({'Meredith Shepherd-Grey': ['Derek Shepherd-Grey'], \
'Amelia Hunt': ['Derek Shepherd-Grey', 'Alex Michael Karev', 'Owen Hunt'], \
'Alex Michael Karev': ['Meredith Shepherd-Grey', 'Amelia Hunt']})
    {'Shepherd-Grey': ['Derek', 'Meredith'], 'Hunt': ['Amelia', 'Owen'], \
'Karev': ['Alex Michael']}
    >>> get_families({})
    {}
    """

    family = {}

    for key in person_to_friends:
        last_name = get_last_name(key)
        first_name = get_first_name(key)
        if last_name not in family:
            family[last_name] = [first_name]
        else:
            if first_name not in family[last_name]:
                family[last_name].append(first_name)
        for value in person_to_friends[key]:
            family_name = get_last_name(value)
            given_name = get_first_name(value)
            if family_name not in family:
                family[family_name] = [given_name]
            else:
                if given_name not in family[family_name]:
                    family[family_name].append(given_name)

    return sort_dict_values(family)


def sort_dict_values(family_dict: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return family_dict with its values alphabetically sorted.

    >>> sort_dict_values({'Shepherd-Grey': ['Meredith', 'Derek'], 'Hunt': \
['Owen', 'Amelia'], 'Karev': ['Alex Michael']})
    {'Shepherd-Grey': ['Derek', 'Meredith'], 'Hunt': ['Amelia', 'Owen'], \
'Karev': ['Alex Michael']}
    >>> sort_dict_values({'Bass': ['Blair', 'Chuck Bartholomew'], 'Waldorf': \
['Eleanor May', 'Chrissy', 'Susan']})
    {'Bass': ['Blair', 'Chuck Bartholomew'], 'Waldorf': \
['Chrissy', 'Eleanor May', 'Susan']}
    """

    for last_name in family_dict:
        family_dict[last_name].sort()

    return family_dict


def get_last_name(name: str) -> str:
    """Return the last name of the given person. A person will always have a
    single, non-empty last name which may be hyphenated.

    Precondition: name is in format 'FirstName(s) LastName'

    >>> get_last_name('Meredith Shepherd-Grey')
    'Shepherd-Grey'
    >>> get_last_name('Alex Michael Karev')
    'Karev'
    """

    return name[name.rfind(' ') + 1:]


def get_first_name(name: str) -> str:
    """Return the first name of the given person. A person will always have a
    non-empty first name which is made of one or more words.

    Precondition: name is in format 'FirstName(s) LastName'

     >>> get_first_name('Meredith Shepherd-Grey')
     'Meredith'
     >>> get_first_name('Alex Michael Karev')
     'Alex Michael'
    """

    return name[:name.rfind(' ')]


def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a dictionary which sorts all people from person_to_networks
    by network name.

    >>> invert_network({'Meredith Shepherd-Grey': ['Parent Teacher Association'], \
'Amelia Hunt': ['Yachting Association', 'Knitting Club'], 'Alex Michael Karev': \
['Knitting Club', 'Ethics Board'], 'Owen Hunt': ['Yachting Association', \
'Parent Teacher Association', 'Knitting Club']})
    {'Parent Teacher Association': ['Meredith Shepherd-Grey', 'Owen Hunt'], \
'Yachting Association': ['Amelia Hunt', 'Owen Hunt'], 'Knitting Club': \
['Amelia Hunt', 'Alex Michael Karev', 'Owen Hunt'], \
'Ethics Board': ['Alex Michael Karev']}
    >>> invert_network({})
    {}
    """

    networks = {}

    for key in person_to_networks:
        for network in person_to_networks[key]:
            if network in networks:
                networks[network].append(key)
            else:
                networks[network] = [key]

    return networks


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
                           person: str) -> List[str]:
    """Return an alphabetically sorted list of names of people who are friends
    of person's friends.

    >>> P2F = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], \
'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], \
'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'], \
'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', \
'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', \
'Mitchell Pritchett', 'Phil Dunphy']}
    >>> get_friends_of_friends(P2F, 'Jay Pritchett')
    ['Cameron Tucker', 'Gloria Pritchett', 'Luke Dunphy', 'Manny Delgado', \
'Mitchell Pritchett', 'Phil Dunphy']
    >>> get_friends_of_friends(P2F, 'Claire Dunphy')
    ['Cameron Tucker', 'Gloria Pritchett', 'Luke Dunphy', 'Luke Dunphy', 'Manny Delgado']
    """

    list = []
    new_list = []

    if person in person_to_friends:
        list = get_friends(person_to_friends, person_to_friends[person])
    if person in list:
        for friend in list:
            if friend != person:
                new_list.append(friend)
    new_list.sort()
    return new_list


def get_friends(person_to_friends: Dict[str, List[str]], \
                           people: List[str]) -> List[str]:
    """Return a list of the friends of those in people from person_to_friends.

    >>> P2F = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], \
'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], \
'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'], \
'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', \
'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', \
'Mitchell Pritchett', 'Phil Dunphy']}
    >>> get_friends(P2F, ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'])
    ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy', 'Cameron Tucker', \
'Jay Pritchett', 'Manny Delgado', 'Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy']
    """

    list = []

    for person in people:
        if person in person_to_friends:
            for friend in person_to_friends[person]:
                list.append(friend)

    return list


def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
                         person_to_networks: Dict[str, List[str]]) -> \
                         List[Tuple[str, int]]:
    """Return a list of tuples containing the friend recommendations for the
    given person and their scores, sorted from highest to lowest score. Only
    potential friends with non-zero scores should be included.

    >>> P2F = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], \
'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], \
'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'], \
'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', \
'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', \
'Mitchell Pritchett', 'Phil Dunphy']}
    >>> P2N = {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado': \
['Chess Club'], 'Mitchell Pritchett': ['Law Association'], 'Alex Dunphy': \
['Chess Club', 'Orchestra'], 'Cameron Tucker': ['Clown School', \
'Wizard of Oz Fan Club'], 'Phil Dunphy': ['Real Estate Association'], \
'Gloria Pritchett': ['Parent Teacher Association']}
    >>> make_recommendations('Jay Pritchett', P2F, P2N)
    [('Mitchell Pritchett', 2), ('Cameron Tucker', 1), ('Luke Dunphy', 1), \
('Phil Dunphy', 1)]
    """

    my_list = get_list(person, person_to_friends, person_to_networks)
    max_score = get_max_score(my_list)
    sorted_list = []

    for i in range(max_score, 0, -1):
        temp = []
        for t in my_list:
            if t[1] == i:
                temp.append(t[0])
        temp.sort()
        sorted_list.extend(temp)

    final_list = match_score_with_name(sorted_list, my_list)
    return final_list


def match_score_with_name(names: List[str], name_score: List[Tuple[str, int]]) \
                          -> List[Tuple[str, int]]:
    """ Take in a sorted list with only names and returns a new list with
    respective scores for each name in the same order as the names list.

    >>> match_score_with_name(['Mitchell Pritchett', 'Cameron Tucker', \
'Luke Dunphy', 'Phil Dunphy'], [('Cameron Tucker', 1), ('Luke Dunphy', 1), \
('Phil Dunphy', 1), ('Mitchell Pritchett', 2)])
    [('Mitchell Pritchett', 2), ('Cameron Tucker', 1), ('Luke Dunphy', 1), \
('Phil Dunphy', 1)]
    """

    final_list = []

    for name in names:
        for t in name_score:
            if name == t[0]:
                final_list.append(t)

    return final_list


def get_max_score(friend_score_list: List[Tuple[str, int]]) -> int:
    """Return the biggest score contained in the tuples of friend_score_list.

    >>> get_max_score([('Luke Dunphy', 3), ('Gloria Pritchett', 2), \
('Cameron Tucker', 1), ('Manny Delgado', 1)])
    3
    """

    max = 0
    for t in friend_score_list:
        if t[1] > max:
            max = t[1]
    return max


def get_list(person: str, person_to_friends: Dict[str, List[str]], \
             person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """Return a list of tuples containing the potential friends of person and
    their scores iff the score is greater than 0.

    >>> P2F = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], \
'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], \
'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'], \
'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', \
'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', \
'Mitchell Pritchett', 'Phil Dunphy']}
    >>> P2N = {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado': \
['Chess Club'], 'Mitchell Pritchett': ['Law Association'], 'Alex Dunphy': \
['Chess Club', 'Orchestra'], 'Cameron Tucker': ['Clown School', 'Wizard of Oz \
Fan Club'], 'Phil Dunphy': ['Real Estate Association'], \
'Gloria Pritchett': ['Parent Teacher Association']}
    >>> get_list('Claire Dunphy', P2F, P2N)
    [('Manny Delgado', 1), ('Cameron Tucker', 1), ('Gloria Pritchett', 2), \
('Luke Dunphy', 3)]
    """

    friends_and_scores = []

    for p in potential_friends(person_to_friends, person):
        if scoring(person, p, person_to_friends, person_to_networks) >= 1:
            friends_and_scores.append((p, scoring(person, p, person_to_friends, \
                                                  person_to_networks)))
    return friends_and_scores


def potential_friends(person_to_friends: Dict[str, List[str]], person: str) \
                      -> List[str]:
    """ Return a list of the potential friends of person.

    >>> TEST_FRIENDS_1 = {'Meredith Shepherd-Grey': ['Derek Shepherd-Grey'], \
'Amelia Hunt': ['Derek Shepherd-Grey', 'Alex Michael Karev', 'Owen Hunt'], \
'Alex Michael Karev': ['Meredith Shepherd-Grey', 'Amelia Hunt']}
    >>> TEST_FRIENDS_2 = {'Blair Bass': ['Eleanor May Waldorf', \
'Serena van-der-Woodsen'],'Chuck Bartholomew Bass': ['Blair Bass', 'Chrissy Waldorf', \
'Nate Archibald'], 'Serena van-der-Woodsen': ['Lily van-der-Woodsen', \
'Eleanor May Waldorf', 'Nate Archibald'], 'Nate Archibald': ['Chuck Bartholomew Bass']}
    >>> potential_friends(TEST_FRIENDS_1, 'Alex Michael Karev')
    ['Derek Shepherd-Grey', 'Owen Hunt']
    >>> potential_friends(TEST_FRIENDS_2, 'Serena van-der-Woodsen')
    ['Blair Bass', 'Chuck Bartholomew Bass', 'Chrissy Waldorf']
    """

    list = []

    for people in person_to_friends:
        if people != person and people not in list and \
           people not in person_to_friends[person]:
            list.append(people)

    for people in person_to_friends:
        for friend in person_to_friends[people]:
            if friend != person and friend not in list and \
               friend not in person_to_friends[person]:
                list.append(friend)

    return list


def get_mutual_friend_score(person1: str, person2: str, person_to_friends: \
                            Dict[str, List[str]]) -> int:
    """Return the score of person2, depending on whether they have
    mutual friend(s) with person1.

    >>> P2F = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], \
'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], \
'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'], \
'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', \
'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', \
'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', \
'Mitchell Pritchett', 'Phil Dunphy']}
    >>> get_mutual_friend_score('Haley Gwendolyn Dunphy', 'Chairman D-Cat', P2F)
    1
    >>> get_mutual_friend_score('Jay Pritchett', 'John Smith', P2F)
    0
    """

    score = 0

    if person1 in person_to_friends and person2 in person_to_friends:
            score += mutual_friend_type_3(person1, person2, person_to_friends)
    if person1 in person_to_friends and person2 not in person_to_friends:
        score += mutual_friend_type_1(person1, person2, person_to_friends)
    if person1 not in person_to_friends and person2 in person_to_friends:
        score += mutual_friend_type_2(person1, person2, person_to_friends)


    return score


def mutual_friend_type_1(person1: str, person2: str, person_to_friends: \
                            Dict[str, List[str]]) -> int:
    """Return the number of mutual friend(s) of person1 and person2. Someone is
    a mutual friend if they are in the friend list of person1 and has person2 in
    their friend list.

    >>> mutual_friend_type_1('Jay Pritchett', 'Manny Delgado', {'Jay Pritchett': \
['Gloria Pritchett'], 'Gloria Pritchett': ['Manny Delgado', 'Jay Pritchett']})
    1
    >>> mutual_friend_type_1('Jay Pritchett', 'Manny Delgado', {'Jay Pritchett': \
['Gloria Pritchett', 'Claire Dunphy'], 'Gloria Pritchett': ['Manny Delgado', \
'Jay Pritchett'], 'Claire Dunphy': ['Manny Delgado']})
    2
    """

    friends = []
    score = 0

    if person1 in person_to_friends:
        for friend in person_to_friends[person1]:
            friends.append(friend)

    for value in friends:
        if value in person_to_friends and person2 in person_to_friends[value]:
            score += 1

    return score


def mutual_friend_type_2(person1: str, person2: str, person_to_friends: \
                            Dict[str, List[str]]) -> int:
    """Return the number of mutual friend(s) of person1 and person2. Someone is
    a mutual friend if they are in the friend list of person2 and has person1 in
    their friend list.

    >>> mutual_friend_type_2('Jay Pritchett', 'Manny Delgado', {'Manny Delgado': \
['Gloria Pritchett'], 'Gloria Pritchett': ['Manny Delgado', 'Jay Pritchett']})
    1
    >>> mutual_friend_type_2('Jay Pritchett', 'Manny Delgado', {'Manny Delgado': \
['Gloria Pritchett', 'Claire Dunphy'], 'Gloria Pritchett': ['Manny Delgado', \
'Jay Pritchett'], 'Claire Dunphy': ['Jay Pritchett']})
    2
    """

    friends = []
    score = 0

    if person2 in person_to_friends:
        for friend in person_to_friends[person2]:
            friends.append(friend)

    for value in friends:
        if value in person_to_friends and person1 in person_to_friends[value]:
            score += 1

    return score


def mutual_friend_type_3(person1: str, person2: str, person_to_friends: \
                            Dict[str, List[str]]) -> int:
    """Return the number of mutual friend(s) of person1 and person2. Someone is
    a mutual friend if they are in the friend list of both person1 and person2,
    and if both person1 and person2 are in their friend list.

    >>> mutual_friend_type_3('Jay Pritchett', 'Manny Delgado', {'Jay Pritchett': \
['Gloria Pritchett'], 'Manny Delgado': ['Gloria Pritchett'], 'Gloria Pritchett': \
['Jay Pritchett', 'Manny Delgado']})
    1
    >>> mutual_friend_type_3('Jay Pritchett', 'Manny Delgado', {'Jay Pritchett': \
['Gloria Pritchett', 'Claire Dunphy'], 'Manny Delgado': ['Gloria Pritchett', 'Claire Dunphy'], \
'Gloria Pritchett': ['Jay Pritchett', 'Manny Delgado'], 'Claire Dunphy': \
['Jay Pritchett', 'Manny Delgado']})
    2
    """

    score = 0

    if person1 in person_to_friends and person2 in person_to_friends:
        for friend in person_to_friends[person1]:
            if friend in person_to_friends[person2] and friend in person_to_friends:
                if person1 in person_to_friends[friend] and \
                   person2 in person_to_friends[friend]:
                    score += 1
    return score


def get_mutual_network_score(person1: str, person2: str, person_to_networks: \
                             Dict[str, List[str]]) -> int:
    """Return the score of person2 depending on whether they have mutual
    network(s) with person1.

    >>> get_mutual_network_score('Jay Pritchett', 'Luke Dunphy', P2N)
    0
    >>> get_mutual_network_score('Claire Dunphy', 'Gloria Pritchett', P2N)
    1
    """

    score = 0

    if person1 in person_to_networks and person2 in person_to_networks:
        person1_networks = person_to_networks[person1]
        person2_networks = person_to_networks[person2]
        for i in person1_networks:
            for j in person2_networks:
                if j == i:
                    score += 1

    return score


def get_mutual_family_score(person1: str, person2: str, person_to_friends: \
                            Dict[str, List[str]], person_to_networks: \
                            Dict[str, List[str]]) -> int:
    """Return the score of person2 depending on whether they have the same
    last name and if they have a mutual friend or network.

    >>> get_mutual_family_score('Claire Dunphy', 'Luke Dunphy', P2F, P2N)
    1
    """

    score = 0

    if get_last_name(person1) == get_last_name(person2):
        if get_mutual_friend_score(person1, person2, person_to_friends) >= 1 or \
           get_mutual_network_score(person1, person2, person_to_networks) >= 1:
            score += 1

    return score


def scoring(person1: str, person2: str, person_to_friends: Dict[str, List[str]], \
            person_to_networks: Dict[str, List[str]]) -> int:
    """Return the total score of the person2, the potential friend of person1.

    >>> scoring('Claire Dunphy', 'Luke Dunphy', P2F, P2N)
    3
    >>> scoring('Jay Pritchett', 'Cameron Tucker', P2F, P2N)
    1
    """

    score = 0

    score += get_mutual_friend_score(person1, person2, person_to_friends)
    score += get_mutual_network_score(person1, person2, person_to_networks)
    score += get_mutual_family_score(person1, person2, person_to_friends, \
                                     person_to_networks)

    return score


if __name__ == '__main__':
    import doctest
    doctest.testmod()
