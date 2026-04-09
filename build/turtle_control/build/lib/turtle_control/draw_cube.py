# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from turtlesim.srv import SetPen
# import time

# class DrawSquare(Node):
#     def __init__(self):
#         super().__init__('draw_square')
#         self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
#         self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')
#         self.pen_client.wait_for_service()

#     def move(self):
#         msg = Twist()

#         for i in range(4):
#             # Move forward
#             msg.linear.x = 2.0
#             msg.angular.z = 0.0
#             for _ in range(10):
#                 self.publisher_.publish(msg)
#                 time.sleep(0.1)

#             # Turn 90 degrees
#             msg.linear.x = 0.0
#             msg.angular.z = 1.57
#             for _ in range(10):
#                 self.publisher_.publish(msg)
#                 time.sleep(0.1)

#         # Stop
#         msg.linear.x = 0.0
#         msg.angular.z = 0.0
#         self.publisher_.publish(msg)
#         time.sleep(0.5)

#     def move_down(self):
#         msg = Twist()
#         req = SetPen.Request()
#         req.r = 0
#         req.g = 0
#         req.b = 0
#         req.width = 2
#         req.off = 1
#         self.pen_client.call_async(req)
#         time.sleep(0.2)

#         msg.linear.x = 0.0
#         msg.angular.z = -1.57
#         for _ in range(10):
#             self.publisher_.publish(msg)
#             time.sleep(0.1)

#         msg.linear.x = 2.0
#         msg.angular.z = 0.0
#         for _ in range(10):
#             self.publisher_.publish(msg)
#             time.sleep(0.1)

#         msg.linear.x = 0.0
#         msg.angular.z = 1.57
#         for _ in range(10):
#             self.publisher_.publish(msg)
#             time.sleep(0.1)

#         msg.linear.x = 0.0
#         msg.angular.z = 0.0
#         self.publisher_.publish(msg)

#         req = SetPen.Request()
#         req.r = 255
#         req.g = 255
#         req.b = 255
#         req.width = 2
#         req.off = 0
#         self.pen_client.call_async(req)
#         time.sleep(0.5)


#     def move_tri(self):
#         msg = Twist()

#         for j in range(3):
#             msg.linear.x = 2.0
#             msg.angular.z = 0.0
#             for _ in range(10):
#                 self.publisher_.publish(msg)
#                 time.sleep(0.1)

#             msg.linear.x = 0.0
#             msg.angular.z = 2.094
#             for _ in range(10):
#                 self.publisher_.publish(msg)
#                 time.sleep(0.1)

#         msg.linear.x = 0.0
#         msg.angular.z = 0.0
#         self.publisher_.publish(msg)

# def main(args=None):
#     rclpy.init(args=args)
#     node = DrawSquare()
#     node.move()
#     rclpy.spin_once(node)

#     node.move_down()
#     rclpy.spin_once(node)

#     node.move_tri()
#     rclpy.spin_once(node)
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()




import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class DrawCube(Node):
    def __init__(self):
        super().__init__('draw_cube')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move_forward(self, duration=2):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 0.0

        for _ in range(int(duration * 10)):
            self.pub.publish(msg)
            time.sleep(0.1)

    def turn(self, angle, duration=1):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = angle

        for _ in range(int(duration * 10)):
            self.pub.publish(msg)
            time.sleep(0.1)

    def stop(self):
        msg = Twist()
        self.pub.publish(msg)
        time.sleep(0.5)

    def draw_square(self):
        for _ in range(4):
            self.move_forward(2)
            self.turn(1.57, 1)
        self.stop()

    def draw_cube(self):
        # Front square
        self.draw_square()

        # Move diagonally (to create depth)
        self.turn(-0.785, 1)   # -45 degrees
        self.move_forward(2)
        self.turn(0.785, 1)

        # Back square
        self.draw_square()

        # Connect corners
        for _ in range(4):
            self.turn(3.14, 2)     # turn back
            self.move_forward(2)   # connect edge
            self.turn(1.57, 1)     # next corner

        self.stop()


def main(args=None):
    rclpy.init(args=args)
    node = DrawCube()
    node.draw_cube()
    rclpy.shutdown()


if __name__ == '__main__':
    main()