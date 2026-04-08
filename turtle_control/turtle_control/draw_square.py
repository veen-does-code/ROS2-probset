import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class DrawSquare(Node):
    def __init__(self):
        super().__init__('draw_square')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move(self):
        msg = Twist()

        for i in range(4):
            # Move forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(2)

            # Turn 90 degrees
            msg.linear.x = 0.0
            msg.angular.z = 1.57
            self.publisher_.publish(msg)
            time.sleep(1)

        # Stop
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawSquare()
    node.move()
    rclpy.shutdown()

if __name__ == '__main__':
    main()