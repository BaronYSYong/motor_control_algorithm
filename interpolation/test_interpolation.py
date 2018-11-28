import matplotlib.pyplot as plt
import interpolation

def PlotGraph(instant, disp, vel, acc):        
    plt.subplot(311)
    plt.plot(instant,disp)
    plt.title('displacement')
    plt.grid()    
    plt.subplot(312)
    plt.plot(instant,vel)
    plt.title('velocity')  
    plt.grid()      
    plt.subplot(313)
    plt.plot(instant,acc)
    plt.title('acceleration')
    plt.grid()
    plt.show()

def PlotGraph2(instant1, disp1, vel1, acc1, instant2, disp2, vel2, acc2):        
    plt.subplot(311)
    plt.plot(instant1,disp1,'g')
    plt.plot(instant2,disp2,'b')
    plt.ylabel('displacement (deg)')
    plt.grid()    
    plt.subplot(312)
    plt.plot(instant1,vel1,'g')
    plt.plot(instant2,vel2,'b')
    plt.ylabel('velocity (deg/s)')  
    plt.grid()      
    plt.subplot(313)
    plt.plot(instant1,acc1,'g')
    plt.plot(instant2,acc2,'b')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (deg/s2)')
    plt.grid()
    plt.show()
    
if __name__ == '__main__':
    instant1, disp1, vel1, acc1 = interpolation.ThirdOrderPolynomial([0,1], [10,30], [0,0]) 
    instant2, disp2, vel2, acc2 = interpolation.FifthOrderPolynomial([0,1], [10,30], [0,0], [0,0])
    PlotGraph2(instant1, disp1, vel1, acc1, instant2, disp2, vel2, acc2)       
    #~ instant, disp, vel, acc = Interpolator.ThirdOrderPolynomial([0,1], [10,30], [-20,-50])
    #~ instant, disp, vel, acc = Interpolator.ThirdOrderPolynomial([2,4], [20,0], [-10,20])
    #~ instant, disp, vel, acc = Interpolator.ThirdOrderPolynomialMultiPoints([0,2,4,8,10], [10,20,0,30,40], [0,-10,20,3,0])
    #~ instant, disp, vel, acc = Interpolator.ThirdOrderPolynomial([0,10], [10,40], [0,0])
    #~ PlotGraph(instant, disp, vel, acc)     
