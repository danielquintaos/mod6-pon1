import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class fishCycle(Node):
    def __init__(self):
        super().__init__('fish_cycle')
        self.velocity_publisher = self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.twist = Twist()

    def move(self , distance):
        self.twist.linear.x = 1.0 
        self.twist.angular.z = 0.0 
        self.time = distance
        self.velocity_publisher.publish(self.twist)

        time.sleep(self.time)

    def turn(self, angle, dir):
        self.twist.linear.x = 0.0
        self.twist.angular.z = dir
        self.time = angle
        self.velocity_publisher.publish(self.twist)

        time.sleep(self.time)

    def circle(self, angle, dir):
        self.twist.linear.x = 1.0
        self.twist.angular.z = dir
        self.time = angle
        self.velocity_publisher.publish(self.twist)

        time.sleep(self.time)

def main(args=None):
    rclpy.init(args=args)
    draw = fishCycle()

    right = -1.0
    left = 1.0
    turn = math.pi*2

    time.sleep(2.0)

    draw.move(2.0)
    draw.turn(turn, right)
    draw.turn(turn, right)
    draw.move(0.5)
    draw.turn(turn, right)
    draw.turn(turn, right)
    draw.move(2.0)
    draw.circle(turn, left)
    draw.turn(turn, left)
    draw.turn(turn, left)
    draw.circle(turn, left)


    draw.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()