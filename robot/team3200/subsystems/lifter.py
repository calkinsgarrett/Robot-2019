# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:00:27 2019

@author: Matthew McFarland
"""
from ctre.talonsrx import TalonSRX
from wpilib.command.subsystem import Subsystem
import team3200

class LifterSub(Subsystem):
    def __init__(self):
        super().__init__("LifterSub")
        self.robot = team3200.getRobot()
        self.map = self.robot.map
        self.level = 0
        self.step = 2
        self.lifterMotors = {}
        for key, motorDesc in self.map.motorsMap.lifterMotors.items():
            self.lifterMotors[key] = team3200.motorHelper.createMotor(motorDesc)
            print(key, motorDesc, self.lifterMotors[key])
            
    def SetLifter(self, position):
        '''Stops the lifter'''
        self.lifterMotors['liftMotor'].set(0)
    
        
    def RunRoller(self, speed):
        '''Toggles the roller on/off.'''
        self.lifterMotors['roller'].set(speed)
            
from wpilib import DoubleSolenoid
class PlatePiston(Subsystem):
    def __init__(self):
        super().__init__("Plate Piston")
        self.robot = team3200.getRobot()
        self.map = self.robot.map.pneumaticsMap
        self.platePiston = DoubleSolenoid(self.map.pcmCan, self.map.forwardChannel, self.map.reverseChannel)
        
    def Activate(self):
        '''Extends the piston if it is destended and vice versa.'''
        print("Piston Activated")
        if self.platePiston.get() == DoubleSolenoid.Value.kReverse:
            self.platePiston.set(DoubleSolenoid.Value.kForward)
            print("Piston Forwards")
        #wpilib.Timer.delay(1)
        elif self.platePiston.get() == DoubleSolenoid.Value.kForward:
            self.platePiston.set(DoubleSolenoid.Value.kReverse)
            print("Piston Backwards")
        else:
            self.platePiston.set(DoubleSolenoid.Value.kForward)
        #wpilib.Timer.delay(1)