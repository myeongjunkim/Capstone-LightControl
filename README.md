# Capstone/Light-Control

## 1.  Purpose of project      
   
<img width="400px" height="300px" src="https://user-images.githubusercontent.com/86545130/180119061-799a947e-2b88-4531-81c1-41283fb3268b.png"/>

> * Object Detection using Deep Learning Model (YOLOv5)
> * Training YOLOv5 with custom dataset
> * Object location coordinate transformation ( image > Work space )
> * Arduino control using Object location

## 2.  Deep learning model training
> * we creating cutom dataset using roboflow

<img width="50%" height="50%" src="https://user-images.githubusercontent.com/86545130/180351159-23034bbc-d689-4661-9c87-6b7c4880634a.PNG"/>

> * Training YOLOv5-s model using colab   
> * **YOLOv5 Github Link** : <https://github.com/ultralytics/yolov5>

<pre>
%cd /content

!git clone https://github.com/ultralytics/yolov5.git
!python train.py --img 416 --batch 16 --epochs 100 --data /content/dataset/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt 
</pre>

- **real-time object detection**
<img width="40%" height="40%" src="https://user-images.githubusercontent.com/86545130/180363079-408b0d41-e3bd-465e-8cfd-f8201e7db2c5.gif"/>

## 3.  Project Process
<div align="center">
   
**[overview]**         
      <img src="https://user-images.githubusercontent.com/86545130/180368074-3b6c0839-f0ba-4509-b228-573814018591.PNG"/>
      

</div>
<hr/>

<div align="center">   
   
**[Coordinate transformation]**   
   <br/>
   <img src="https://user-images.githubusercontent.com/86545130/180369747-40332580-d8b9-4d88-8acc-f5ec72f3369d.png"/>   
   To control robot arm, we need to coordinate (theta1, theta2)   
</div>   

<br/>
<br/>
<br/>
<div align="center">   
   
   So we converted __object location coordinate(pixel)__ within the image to __(theta1, theta2)__   
  <img src="https://user-images.githubusercontent.com/86545130/180371379-e6474ba0-36c4-4b1f-9456-2b80e544f857.png"/>
   <br/>   
   <br/>   
   <br/>   
   **[Web cam to Real place]**
   <img src="https://user-images.githubusercontent.com/86545130/180373641-5f606168-2dda-45df-9eaf-833ff9bd6df6.png"/>   
   ||Web cam[px]|Real Value[cm]|Scale factor[px/cm]|
   |:---:|:---:|:---:|:---:|
   |1|(245, 270)|(26.5, 20)|(0.1082, 0.0741)|
   |2|(195, 345)|(21.5, 25)|(0.1102, 0.0724)|
   |3|(297, 198)|(31.5, 15)|(0.1060, 0.0758)|
   |4|(135, 198)|(16.5, 15)|(0.1222, 0.0758)|   
   
   So we get average **scale factor (0.1116, 0.0745)**   
   <br/>
   <br/>   
   **[ Real place to Polar]**
   <img src="https://user-images.githubusercontent.com/86545130/180377194-905cd84b-159f-46ce-abba-f8e831d4c784.png"/>
   <img src="https://user-images.githubusercontent.com/86545130/180377478-d7abe982-ebf0-4f3a-a3ee-3265579a1822.png"/>   
   <br/>
   <br/>   
   **[Polar to Arduino]**
   <img src="https://user-images.githubusercontent.com/86545130/180378242-17996de4-7915-485f-abc3-c816ff31be42.png"/>
   ||Radius(r)|Theta2(degree)|
   |:---:|:---:|:---:|
   |1|52.5|92|
   |2|48.5|93|
   |3|15.5|94|
   |4|41.5|95|
   |5|39.5|96|
   |6|35.8|97|
   |7|30.5|100|
   |8|29.5|101|
   |9|26.5|103|
   |10|23.3|106|
   |11|20.0|109|
   |12|17.7|112|
   |13|14.5|117|
   |14|11.0|125|
   |15|9.3|130|
   |16|7.4|135|
   |17|4.7|145|
   |18|2.3|155|
   |19|0.0|175|   
   
   <img src="https://user-images.githubusercontent.com/86545130/180380165-706084f0-2b5e-4301-9521-67cec4252c46.png"/>
</div>   


```python
import numpy as np

# pixel to cm
real_x = (pixel_x) * 0.11165
real_y = (pixel_y) * 0.0745

# cartesian to polar
R = (real_x**2 + real_y**2)**0.5 - 6.5
theta1 = 115 - np.degrees(np.arctan(real_y/real_x))

# r to theta2 (Regression)
if R >= 26.5:
   # 4 order polynomial regression
   theta2 = (-0.0000001)*(R**4) - (0.0004)*(R**3) + (0.0611)*(R**2) -3.1901*(R) + 152.57
else:
   # 3 order polynomial regression
   theta2 = (-0.0012)*(R**3) + (0.1378)*(R**2) -5.3419*(R) + 169.53
```
  
## 4.  Arduino control

<div align="center">
   <img src="https://user-images.githubusercontent.com/86545130/180383710-30c973bd-c989-4d94-aa18-9c4f62bed658.png"/>
</div>   
   

## 5.  Final Result

<img src="https://user-images.githubusercontent.com/86545130/180387815-93a310ba-5656-4025-b5c3-1103ff23682d.gif"/>

<img src="https://user-images.githubusercontent.com/86545130/180388117-e578a14e-d77d-4b76-8e84-605612fd7a8a.gif"/>
