from UI import Ui_MainWindow
from opencv_engine import opencv_engine
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow
import numpy as np
import cv2
import json
from scipy.spatial import distance as dist
from math import pi
import os

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.result_flag = False

        self.dir_path = './map_collection/'
        self.main_image_path = './map_collection'

        self.points = [] # save points by right clicked 
        self.set_map_combobox()
        self.point_counter = 0
        
        
        
        # setup mouse press event on the image 
        self.ui.main_image.mousePressEvent = self.mouse_press_event
        
        # setup connect 
        self.ui.map_comboBox.currentIndexChanged.connect( self.set_index_combobox )
        self.ui.index_comboBox.currentIndexChanged.connect( self.update_main_image)
        self.ui.map_back.clicked.connect(self.set_back_map)
        self.ui.map_next.clicked.connect(self.set_next_map)
        self.ui.index_back.clicked.connect(self.set_back_index)
        self.ui.index_next.clicked.connect(self.set_next_index)
        
        self.ui.save_button.clicked.connect(self.save_np)
        self.ui.clear_button.clicked.connect(self.clear_points)
        self.ui.show_result_button.clicked.connect(self.show_results)
        
    # order points 
    def order_points(self, pts):
        # sort the points based on their x-coordinates
        xSorted = pts[np.argsort(pts[:, 0]), :]

        # grab the left-most and right-most points from the sorted
        # x-roodinate points
        leftMost = xSorted[:2, :]
        rightMost = xSorted[2:, :]

        # now, sort the left-most coordinates according to their
        # y-coordinates so we can grab the top-left and bottom-left
        # points, respectively
        leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
        (tl, bl) = leftMost

        # if use Euclidean distance, it will run in error when the object
        # is trapezoid. So we should use the same simple y-coordinates order method.

        # now, sort the right-most coordinates according to their
        # y-coordinates so we can grab the top-right and bottom-right
        # points, respectively
        rightMost = rightMost[np.argsort(rightMost[:, 1]), :]
        (tr, br) = rightMost

        # return the coordinates in top-left, top-right,
        # bottom-right, and bottom-left order
            
        
        
        return np.array([self.pixel_to_carla(tl), self.pixel_to_carla(tr), self.pixel_to_carla(br), self.pixel_to_carla(bl)], dtype="float32")
        
    def mouse_press_event(self, event):

        point = [event.pos().x() -1 , event.pos().y() -1 ]

        if event.button() == 1: # right clicked
            if self.point_counter != 4:
                
                self.point_counter+=1
                self.points.append(point)
                    
                self.update_image_frame(point)
                
                if self.point_counter == 4:
                    self.points = self.order_points(np.array( self.points) )
                
        elif event.button() == 2: # left clicked
                
            if self.point_counter == 4:
                
                coor_list = []
                for point in self.points:
                    coor_list.append(self.carla_to_pixel( point ))
                
                contours = np.array(coor_list)

                cv2.fillPoly(self.current_top_img, pts = [contours], color =(255,0,0))
                
            self.set_image(self.current_top_img, self.ui.main_image)
           
    def clear_points(self):
        self.points = []
        self.set_image(self.original_top_img, self.ui.main_image)
        self.current_top_img = self.original_top_img.copy()
        self.point_counter = 0 
        # updata the image 
        
        
    def show_results(self):
        
        if self.result_flag : 
            self.result_flag  = False 
        else:
            self.result_flag  = True
        ##############################
        
        
        self.update_main_image()

    def save_np(self):
        
        # save point to np array 
        # file name format
        # Town10HD_opt_crosswalk
        
        file_name = f"./label_result/{self.ui.map_comboBox.currentText()}_crosswalk.npy"
        
        if len(self.points) == 4:
            if  not os.path.exists(file_name):
                # file not exist, create one 
                points_list = []
                points_list.append(np.array(self.points))
                np.save(file_name, np.array(points_list) )
                self.points = []
                self.set_image(self.original_top_img, self.ui.main_image)
                self.current_top_img = self.original_top_img.copy()
                self.point_counter = 0 
            else:
                # file exists, read it and append data 
                points_list = list( np.load(file_name) ) 
                points_list.append(np.array(self.points))
                np.save(file_name, np.array(points_list) )
                self.points = []
                self.set_image(self.original_top_img, self.ui.main_image)
                self.current_top_img = self.original_top_img.copy()
                self.point_counter = 0 

    def update_image_frame(self, point ):
        
        self.current_top_img = opencv_engine.draw_point(
            self.current_top_img, point=point)

        self.set_image(self.current_top_img, self.ui.main_image)

    def set_back_map(self):
        if ((self.ui.map_comboBox.currentIndex()-1) == -1):
            self.ui.map_comboBox.setCurrentIndex(
                self.ui.map_comboBox.count()-1)
        else:
            self.ui.map_comboBox.setCurrentIndex(
                self.ui.map_comboBox.currentIndex()-1)

    def set_next_map(self):
        if (((self.ui.map_comboBox.currentIndex()+1) % self.ui.map_comboBox.count()) == 0):
            self.ui.map_comboBox.setCurrentIndex(0)
        else:
            self.ui.map_comboBox.setCurrentIndex(
                self.ui.map_comboBox.currentIndex()+1)
            
    def set_back_index(self):
        if ((self.ui.index_comboBox.currentIndex()-1) == -1):
            self.ui.index_comboBox.setCurrentIndex(
                self.ui.index_comboBox.count()-1)
        else:
            self.ui.index_comboBox.setCurrentIndex(
                self.ui.index_comboBox.currentIndex()-1)
            
    def set_next_index(self):
        if (((self.ui.index_comboBox.currentIndex()+1) % self.ui.index_comboBox.count()) == 0):
            self.ui.index_comboBox.setCurrentIndex(0)
        else:
            self.ui.index_comboBox.setCurrentIndex(
                self.ui.index_comboBox.currentIndex()+1)

    def set_map_combobox(self):
        map_list = ["Town01", "Town02", "Town03_opt", "Town04_opt", "Town05_opt", "Town06_opt", "Town07_opt",  "Town10HD_opt"]

        self.init_map_combobox = True
        self.ui.map_comboBox.clear()
                
        for i, map in enumerate(map_list):
            self.ui.map_comboBox.insertItem(i, map)
        self.init_map_combobox = False
        
        self.set_index_combobox()
        
        
    def set_index_combobox(self):
        
        map_list = os.listdir(f"./map_collection/{self.ui.map_comboBox.currentText()}")
        
        self.ui.index_comboBox.clear()
        for i in range(int(len(map_list)/2 )):
            self.ui.index_comboBox.insertItem(i, str(i))
        self.ui.index_comboBox.setCurrentIndex(0)
        self.update_main_image()
        
    def update_main_image(self):
        
        if self.ui.index_comboBox.count() != 0:
        
            map_path = f"./map_collection/{self.ui.map_comboBox.currentText()}/{self.ui.index_comboBox.currentText()}.png"
            
            self.original_top_img = cv2.imread(map_path)   
            self.current_top_img = cv2.imread(map_path)  
            
            self.set_image(self.original_top_img, self.ui.main_image)
            self.update_ego_data()
            
            
            if self.result_flag :
                file_name = f"./label_result/{self.ui.map_comboBox.currentText()}_crosswalk.npy"
                
                # if file not exist, do nothing
                if  os.path.exists(file_name):
                    # file exists, read it and append data 
                    points_list = list( np.load(file_name) ) 
                    
                    for points in points_list:     
                        coor_list = []
                        for point in points:
                            coor_list.append(self.carla_to_pixel(point))
                        
                        contours = np.array(coor_list)

                        cv2.fillPoly(self.current_top_img, pts = [contours], color =(0,0,255))
                        
                    self.set_image(self.current_top_img, self.ui.main_image)
            
            
            
        
    def set_image(self, image, ui_main_image):
        
        img_size = image.shape
        qimg = QImage(image, img_size[1], img_size[0],img_size[1]*3, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(qimg)
        ui_main_image.setPixmap(self.qpixmap)

    def update_ego_data(self):
        
        # read json file 
        json_path = f"./map_collection/{self.ui.map_comboBox.currentText()}/{self.ui.index_comboBox.currentText()}.json"
        with open(json_path, 'r') as d:
            data = json.load(d)
            
        self.compass = data["compass"]
        self.x = data["x"]
        self.y = data["y"]
        
    def pixel_to_carla(self, point):
        x, y = (point[0] - 512, point[1] - 512)
        meter_per_pixel = 0.09107571 #  0.18215

        ego_x = self.x  
        ego_y = self.y  
        theta = self.compass

        theta = -theta*pi/180.0
        # clockwise
        R = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])

        u = np.array([x, y])
        target = R.T.dot(u)
        target *= meter_per_pixel

        target[0] += ego_x
        target[1] += ego_y

        return [target[0], target[1]]

    def carla_to_pixel(self, point):
        meter_per_pixel = 0.09107571 #0.18215
        ego_x = self.x  
        ego_y = self.y  
        theta = self.compass

        x = point[0] - ego_x
        y = point[1] - ego_y

        u = np.array([x, y])
        u /= meter_per_pixel
        theta = theta*pi/180.0

        # clockwise
        R = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])

        target = R.T.dot(u)
        x, y = target
        x = int(x + 512 )
        y = int(y + 512 )

        return [x, y]
        