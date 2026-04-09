import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class DrawSquare(Node):
    def __init__(self):
        super().__init__('draw_square')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move(self, linear, angular, duration):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular

        for _ in range(int(duration * 20)):
            self.pub.publish(msg)
            time.sleep(0.05)

    def stop(self):
        msg = Twist()
        self.pub.publish(msg)
        time.sleep(0.5)

    def draw_square(self):
        for _ in range(4):
            self.move(2.0, 0.0, 2.0)   # forward
            self.move(0.0, 1.57, 1.0)  # 90° turn
        self.stop()


def main(args=None):
    rclpy.init(args=args)
    node = DrawSquare()
    node.draw_square()
    rclpy.shutdown()


if __name__ == '__main__':
    main()