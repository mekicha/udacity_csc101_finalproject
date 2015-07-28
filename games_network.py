# Use this to try out anything you like. Use print to display your answer
# when you press the "Test Run" button.
# Use the "Reset" button to reset the screen 
input_string="""John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\ """

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

def create_data_structure(input_string):
    """This function parses a block of text, retrieves and stores relevant information 
       in a dictionaryof lists. The text format is like so: <user> is connected to 
       <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>. The dictionary
       data structure is like so: network={[[connections],[games liked]]} """
    
    network={}
    connections=[]
    games_liked=[]
    user=''
    pos=input_string.find('.')
    start=0
    while pos!=-1:
        line=input_string[start:pos]
        if 'is connected to' in line:
            connection=line.split('is connected to')
            user=connection[0].strip()
            connected=connection[1].strip()
            connected=connected.split(',')
            for name in connected:
                connections.append(name.strip())
            network[user]=[[],[]]
            network[user][0]=connections
            connections=[]
        else:
            if 'likes to play' in line:
                game=line.split('likes to play')
                games=game[1].split(',')
                for name in games:
                    games_liked.append(name.strip())
                network[user][1]=games_liked
                games_liked=[]
        start=pos+1
        pos=input_string.find('.',start)   
    return network

def get_user(network,user):
    """Helper function that returns a user from the network or none if user does not exist"""
    
    if user in network:
        return network[user]
    return None

def get_connections(network,user):
    data=get_user(network,user)
    connections=data[0]
    if connections:
        return connections
    return []

def get_games_liked(network,user):
    """returns a list of all the games a user likes"""
    data=get_user(network,user)
    games_liked=data[1]
    if games_liked:
        return games_liked
    return []

def add_connection(network,user_A,user_B):
    """adds a connection from user_A to user_B if both exist in network"""
    if not user_A in network or not user_B in network:
        return False
    connection=get_connections(network,user_A)
    if user_B in connection:
        return network
    else:
        connection.append(user_B)
    return network

def add_new_user(network, user, games):
    """Adds a new user to the network. User has no connections, to begin with"""
    if user in network:
        return
    network[user]=[[],[]]
    network[user][1]=games
    return network

def get_secondary_connections(network,user):
    """Finds all the secondary connections (i.e. connections of connections) of a 
    given user. """
    secondary_connections=[]
    connections=get_user(network,user)
    if not connections: return
    if connections[0]==[]: return []
    for name in connections[0]:
        secondary_connections.append(name)
        for p in network[name][0]:
            secondary_connections.append(p)
    return secondary_connections

def connections_in_common(network,user_A,user_B):
    if not user_A in network or not user_B in network:
        return False
    user1=get_user(network,user_A)[0]
    user2=get_user(network,user_B)[0]
    common=0
    for user in user1:
        if user in user2:
            common+=1
    return common
   
def path_to_friend(network,user_A,user_B):
    path=[]
    if not user_A in network or not user_B in network:
        return None
    if user_A==user_B:
        return [user_A]
    user1=get_user(network,user_A)[0]
    if user_B in user1:
        path.append([user_A,user_B])
    else:
        for node in network[user_A][0]:
            if node not in path:
                newpath = path_to_friend(network, node,user_B)
                if newpath:
                    return newpath
    
    
               
net = create_data_structure(example_input)
#print net
#print get_connections(net, "Debra")
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "Freda")
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])
#print get_secondary_connections(net, "Mercedes")   
#print connections_in_common(net, "Mercedes", "John")
print path_to_friend(net, "John", "Ollie")
