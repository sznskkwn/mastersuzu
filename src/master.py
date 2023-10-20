#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import smach
from enter_room.srv import EnterRoom



class Enterroom(smach.State):
    def __init__(self):
        smach.State.__init__(self,outcomes=['enter_finish'])
        self.enter = rospy.ServiceProxy("enter_room_server",EnterRoom)
    
    def execute(self, _):
        self.enter(1.0,0.2)
        return 'enter_finish'
class navi(smach.State):
    def __init__(self):
        smach.State.__init__(self,outocomes=['navigation'])
        self.nav = rospy.ServiceProxy("/navi_location_server",NaviLocation)
    
    def execute(self):
        self.nav('tall table2')
        return 'navigation'
def main():
    rospy.init_node('master')
    sm_top = smach.StateMachine(outcomes=['succeed'])

    with sm_top:
        smach.StateMachine.add('enterR', Enterroom(),transitions={'enter_finish':NAVI})
        smach.StateMachine.add('NAVI', navi(),transitions={'navigation':'succeed'})
if __name__ == '__main__':
    main()
