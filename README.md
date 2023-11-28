## Oscillating-Cylinder-flow-prediction-Lattice-Boltzmann-method
The python code uses a single relaxation factor based Lattice  boltzmann method which solves for laminar flow regime adjust the omega value given by the equation given bellow


![image](https://github.com/Rushilrajesh1256/Oscillating-Cylinder-flow-prediction-Lattice-Boltzmann-method/assets/152313008/6c7598f1-b2bb-435f-801f-c34c2f5eab51)



MA being your desired courant number.
the contours shown bellow are that of a 100 reynolds no simulation of an oscialting  cylyndir
Note-
1)Lattice model-D2Q9

2)SRT LBM model

3)no scalar field integration

4)CD value  plot for every 1000  iterations(this cna be adjusted within the code)

5)no bounce back boundary conditons values  are abssorbed at boundary

6)velocity magnitude contour was is plotted  for every 50 iterations 



![image](https://github.com/Rushilrajesh1256/Oscillating-Cylinder-flow-prediction-Lattice-Boltzmann-method/assets/152313008/846c5f81-eeda-49b3-ba0d-f7ccc510114f)


![image](https://github.com/Rushilrajesh1256/Oscillating-Cylinder-flow-prediction-Lattice-Boltzmann-method/assets/152313008/2106190b-36a6-4bb6-86cb-cc97af708893)


instructions-
1)geomatry can be modified by changing the parametrs of  the distance function (simple shapes can be made)
2)to set boundary  conditions the following equations  are to be used
  
  
  1)
  ![image](https://github.com/Rushilrajesh1256/Oscillating-Cylinder-flow-prediction-Lattice-Boltzmann-method/assets/152313008/c3321258-1854-418f-9cad-c9e60f68ce8e)


  2)
  ![image](https://github.com/Rushilrajesh1256/Oscillating-Cylinder-flow-prediction-Lattice-Boltzmann-method/assets/152313008/22e8dab0-072c-4ace-a315-c9b465268628)


3)ensure  the  courant numberis  less  thatn 1 to predict   resutls accuratley








  







