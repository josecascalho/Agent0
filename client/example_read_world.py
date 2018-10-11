import client
import ast
import random


# Calculate H
def calculate_h():

#Get initial position
def getInitialPos():
        action_value = "info position"
        s.sendall(str.encode(action_value))
        data = s.recv(2048)
        coord =ast.literal_eval(data.decode())
	# test
        print('Received info for initial position', self.coord)
	return coord
        
 #Get goal position
def getGoalPos(): 
       action_value = "info goal"
        s.sendall(str.encode(action_value))
        data = s.recv(2048)
        goal =ast.literal_eval(data.decode())
        # test
        print('Received pos of goal', self.goal_coord)
	return goal
def getMaxCoord():        
	action_value = "info maxcoord"
        s.sendall(str.encode(action_value))
        data = s.recv(2048)
        max_coord =ast.literal_eval(data.decode())
        # test
        print('Received maxcoord', max_coord)
	return max_coord   
def getMap():
        action_value = "info map"
        s.sendall(str.encode(action_value))
        data = s.recv(2048)
        w_map =ast.literal_eval(data.decode())
        # test
        print('Received map:', w_map)
	return w_map
def getObstacles():
        action_value = "info obstacles"
        s.sendall(str.encode(action_value))
        data = s.recv(2048)
        obstacles = ast.literal_eval(data.decode())
         # test
        print('Received obstacles:', obstacles)
	return obstacles
def setSteps():        
	action_value="command set_steps"
        s.sendall(str.encode(action_value))
        data = s.recv(2048)
	return True

def main():
# Get information of the world
# Print the obstacles position
# Print the position
#Print a list of possible positions from the actual position 
# Test if any position in the list is a goal
# For each element in the list, expand it for the next possible positions (don't include position already in the previous list)
# Test if any position in the list is a goal
# Etc

#STARTING PROGRAM
c = client.Client('127.0.0.1', 50000)
res = c.connect()
random.seed() #To become true random, a different seed is used! (clock time)
if res == -1:
    main()


