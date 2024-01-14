# -*- coding: utf-8 -*-
# from __future__ import print_function

# Importación de librerías
import rospy
import smach_ros
import math
import actionlib
import sys
from smach import State, StateMachine
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String, Int32
from geometry_msgs.msg import Twist

#ROBOTICA -11 0
#ELECTRONICA -14 -4
#RECEPCION 10 9
#ENTRADA -4 -16
#AUTOMATICA -3 10

# Renombrar tópicos para mejor visibilidad
TOPIC_VEL = "/cmd_vel"
TOPIC_SCAN = '/base_scan'

class Preguntar(State):
    def __init__(self):
        State.__init__(self, outcomes=['ROB', 'ELEC', 'ENTRADA', 'AUTO', 'REC', 'ERROR'])
        self.base = False

    def execute(self, userdata):
        llamadaVoz = input("Adonde quiere ir? ")
        if llamadaVoz == 'ROBOTICA':
            return 'ROB'
        elif llamadaVoz == 'ELECTRONICA':
            return 'ELEC'
        elif llamadaVoz == 'ENTRADA':
            return 'ENTRADA'
        elif llamadaVoz == 'AUTOMATICA':
            return 'AUTO'
        elif llamadaVoz == 'RECEPCION':
            return 'REC'
        else:
            return 'ERROR'
        
class GoToROB(State):
    def __init__(self):
        State.__init__(self, outcomes=['tROB'])
        self.base = False
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def execute(self, userdata):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.pose.position.x = 12
        goal.target_pose.pose.position.y = 0
        goal.target_pose.pose.orientation.w = 1.0

        self.client.send_goal(goal)
        state = self.client.get_state()

        while state == GoalStatus.ACTIVE or state == GoalStatus.PENDING:
            rospy.Rate(10)
            state = self.client.get_state()

        return 'tROB'

class GoToELEC(State):
    def __init__(self):
        State.__init__(self, outcomes=['tELEC'])
        self.base = False
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def execute(self, userdata):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.pose.position.x = 2.5
        goal.target_pose.pose.position.y = 0.5
        goal.target_pose.pose.orientation.w = 1.0

        self.client.send_goal(goal)
        state = self.client.get_state()

        while state == GoalStatus.ACTIVE or state == GoalStatus.PENDING:
            rospy.Rate(10)
            state = self.client.get_state()

        return 'tELEC'

class GoToENTRADA(State):
    def __init__(self):
        State.__init__(self, outcomes=['tENTRADA'])
        self.base = False
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def execute(self, userdata):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.pose.position.x = 13
        goal.target_pose.pose.position.y = -9.5
        goal.target_pose.pose.orientation.w = 1.0

        self.client.send_goal(goal)
        state = self.client.get_state()

        while state == GoalStatus.ACTIVE or state == GoalStatus.PENDING:
            rospy.Rate(10)
            state = self.client.get_state()

        return 'tENTRADA'

class GoToAUTO(State):
    def __init__(self):
        State.__init__(self, outcomes=['tAUTO'])
        self.base = False
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def execute(self, userdata):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.pose.position.x = 4
        goal.target_pose.pose.position.y = 18
        goal.target_pose.pose.orientation.w = 1.0

        self.client.send_goal(goal)
        state = self.client.get_state()

        while state == GoalStatus.ACTIVE or state == GoalStatus.PENDING:
            rospy.Rate(10)
            state = self.client.get_state()

        return 'tAUTO'

class GoToREC(State):
    def __init__(self):
        State.__init__(self, outcomes=['tREC'])
        self.base = False
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def execute(self, userdata):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.pose.position.x = 23.5
        goal.target_pose.pose.position.y = 13.5
        goal.target_pose.pose.orientation.w = 1.0

        self.client.send_goal(goal)
        state = self.client.get_state()

        while state == GoalStatus.ACTIVE or state == GoalStatus.PENDING:
            rospy.Rate(10)
            state = self.client.get_state()

        return 'tREC'

if __name__ == '__main__':
    rospy.init_node("practica3")
    sm = StateMachine(outcomes=['stop'])
    with sm:
        StateMachine.add('Preguntar', Preguntar(), transitions={'ROB': 'GoToROB', 
                                'ELEC': 'GoToELEC', 
                                'ENTRADA': 'GoToENTRADA',
                                'REC': 'GoToREC',
                                'AUTO': 'GoToAUTO',
                                'ERROR': 'stop'})
        StateMachine.add('GoToROB', GoToROB(), transitions={'tROB': 'Preguntar'})
        StateMachine.add('GoToELEC', GoToELEC(), transitions={'tELEC': 'Preguntar'})
        StateMachine.add('GoToENTRADA', GoToENTRADA(), transitions={'tENTRADA': 'Preguntar'})
        StateMachine.add('GoToAUTO', GoToAUTO(), transitions={'tAUTO': 'Preguntar'})
        StateMachine.add('GoToREC', GoToREC(), transitions={'tREC': 'Preguntar'})
    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()
    sm.execute()
    rospy.spin()
    sis.stop()
