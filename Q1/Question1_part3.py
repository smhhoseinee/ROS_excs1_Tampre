"""_NOTE_
1. Your task is to complete the parts of the code denoted by '???' 
2. You need to first run this code, and then play back the rosbag file: refer to part 2 of question 1.
3. After the rosbag has been played back completely, use crtl+c (intruption keys) to see the plots.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from math import cos, sin, pi
import matplotlib.pyplot as plt
import numpy as np


class WheelSpeedSubscriber(Node):

	def __init__(self):
		super().__init__('wheelspeed_subscriber')
		self.subscriber_ = self.create_subscription(Float64MultiArray, '???', self.listener_callback, 10)
		self.publisher_ = self.create_publisher(Float64MultiArray, 'robot_odometry', 10)
		self.r_ = 0.1
		self.d_ = 0.4
		self.delta_ = 0.1
		self.t_ = [0]
		
        # The history of x, y, and \theta for "Forward" method.
		self.forw_x_ = [0]
		self.forw_y_ = [0]
		self.forw_theta_ = [0]
		
        # The history of x, y, and \theta for "Midpoint" method.
		self.mid_theta_ = [0]
		self.mid_x_ = [0]
		self.mid_y_ = [0]

	def listener_callback(self, msg):
		angular_left_vel = msg.data[0]/60*2*pi #Convert from rpm to rad/s
		angular_right_vel = msg.data[1]/60*2*pi #Convert from rpm to rad/s
		
        # Calculating the next step using TWO methods.
		next_forw_x, next_forw_y, next_forw_theta = self.calc_euler(
		angular_left_vel, angular_right_vel, "forward")
		
		next_mid_x, next_mid_y, next_mid_theta = self.calc_euler(
		angular_left_vel, angular_right_vel, "midpoint")
		
		#Storing the data for plotting.
		self.forw_x_.append(next_forw_x)
		self.forw_y_.append(next_forw_y)
		self.forw_theta_.append(next_forw_theta)
		
		self.mid_x_.append(next_mid_x)
		self.mid_y_.append(next_mid_y)
		self.mid_theta_.append(next_mid_theta)
		
        #Publishing the data
		self.t_.append(self.t_[-1]+self.delta_)
		output_forw_msg = Float64MultiArray()
		output_forw_msg.data = [self.forw_x_[-1], self.forw_y_[-1], self.forw_theta_[-1]]
		output_mid_msg = Float64MultiArray()
		output_mid_msg.data = [self.mid_x_[-1], self.mid_y_[-1], self.mid_theta_[-1]]
		self.publisher_.publish(output_forw_msg)
		self.publisher_.publish(output_mid_msg)
	
	def calc_euler(self, left_w, right_w, method):
		
		v = ??? 
		omega = ???
		curr_x = None
		curr_y = None
		curr_theta = None
		curr_hat_theta = None
		
		if method == "forward":
            ???
		elif method == "midpoint":
            ???
		
		if method == "forward":
            ???
		elif method == "midpoint":
            ???
		
		next_x = ???
		next_y = ???
		next_theta = ???
		
		return next_x, next_y, next_theta
		

def main(args=None):
	rclpy.init(args=args)
	try:
		sub_node = WheelSpeedSubscriber()
		rclpy.spin(sub_node)
	except KeyboardInterrupt:
	
		plt.figure("Robot x coordinates")
		plt.plot(np.array(sub_node.t_), np.array(sub_node.forw_x_), '-b', label="forward euler")
		plt.plot(np.array(sub_node.t_), np.array(sub_node.mid_x_), '--r', label="midpoint euler")
		plt.legend(loc="upper left")
		plt.xlabel('Time, t (s)')
		plt.ylabel('x (m)')
		
		plt.figure("Robot y coordinates")
		plt.plot(np.array(sub_node.t_), np.array(sub_node.forw_y_), '-b', label="forward euler")
		plt.plot(np.array(sub_node.t_), np.array(sub_node.mid_y_), '--r', label="midpoint euler")
		plt.legend(loc="upper left")
		plt.xlabel('Time, t (s)')
		plt.ylabel('y (m)')
		
		plt.figure("Robot theta coordinates")
		plt.plot(np.array(sub_node.t_), np.array(sub_node.forw_theta_), '-b', label="forward euler")
		plt.plot(np.array(sub_node.t_), np.array(sub_node.mid_theta_), '--r', label="midpoint euler")
		plt.legend(loc="upper left")
		plt.xlabel('Time, t (s)')
		plt.ylabel('theta (rad)')
		
		plt.figure("2D path of the robot for euler forward and -midpoint method")
		plt.plot(np.array(sub_node.forw_x_), np.array(sub_node.forw_y_), '-b', label="forward euler")
		plt.plot(np.array(sub_node.mid_x_), np.array(sub_node.mid_y_), '--r', label="midpoint euler")
		plt.legend(loc='upper left')
		plt.xlabel('x (m)')
		plt.ylabel('y (m)')
		
		plt.show()
		sub_node.destroy_node()
		rclpy.shutdown()


if __name__ == '__main__':
	main()