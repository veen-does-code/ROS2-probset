import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
import time
import threading

class DrawSquare(Node):
    def __init__(self):
        super().__init__('draw_square')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.teleport_client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        self.teleport_client.wait_for_service()

    def publish(self, linear, angular, iterations):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        for _ in range(iterations):
            self.publisher_.publish(msg)
            time.sleep(0.1)

    def draw_square(self):
        req = TeleportAbsolute.Request()
        req.x, req.y, req.theta = 2.0, 2.0, 0.0  # face right
        self.teleport_client.call_async(req)
        time.sleep(0.2)

        for _ in range(4):
            self.publish(2.0, 0.0, 20)    # forward
            self.publish(0.0, 1.5708, 10) # turn left 90

def main(args=None):
    rclpy.init(args=args)
    node = DrawSquare()
    thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    thread.start()
    node.draw_square()
    rclpy.shutdown()

if __name__ == '__main__':
    main()