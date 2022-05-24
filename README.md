# finite-element-method
FEM

Bước 1: Vẽ hàm tuyến tính từng khúc từ [0,1] x [0,1] -> R

    Bài 1. Tạo lưới như ở https://github.com/anthule123/finite-element-method/blob/main/draw1c.ipynb
    
    Bài 2. Với mỗi điểm trong lưới, xây dựng hàm tuyến tính dạng "chóp", giống như 1 kim tự tháp nhô
           lên tại điểm đó và bằng 0 tại các điểm kề với nó.
           file : draw3.ipynb
          
 Bước 2: Xây dựng ma trận phần tử tại mỗi tam giác
      Mỗi tam giác (VD: (1,2,3)) trong lưới sẽ có 3 hàm tuyến tính tương ứng:
   
           f1: = 1 tại điểm 1 và = 0 tại điểm 2 và 3
           f2: = 1 tại điểm 2 và = 0 tại điểm 1 và 3
           f3: = 1 tại điểm 3 và = 0 tại điểm 1 và 2
          
      Tính ma trận (a(f_i,f_j))  = (f_i', f_j')   
           file: cal1.ipynb
         
 Bước 3: Nối các ma trận phần tử để được ma trận toàn cục
 
      VD: N = 3. Chia ra 9 đỉnh, 4*2   tam giác như trong hình vẽ
      
          Có 9 hàm kim tự tháp, là cơ sở của hệ phần tử hữu hạn,
           tương ứng với 9 đỉnh.
           Giả sử đỉnh 1 và đỉnh 2 cùng kề với đỉnh 3, 
            thì kim tự tháp ứng với đỉnh 1 và kim tự tháp ứng với đỉnh 2 sẽ 
            có phần tam giác(1,2,3) chung nhau, tính được ma trận phần tử tương ứng.
            
          Cuối cùng, cộng tất cả các ma trận phần tử đó lại, ta đc ma trận toàn cục. 
        
        file : draw6.ipynb
        
 Part 2: tính xấp xỉ tích phân 1 hàm số trên miền tam giác : cầu phương Gauss
 
        b1: tính trên đoạn 1D: 
        https://rosettacode.org/wiki/Numerical_integration/Gauss-Legendre_Quadrature
        file : gauss quadrature.ipynb
        
        b2: tính trên hình chữ nhật 2D: 
            tính trên tứ giác bất kì
        b3: tính trên tam giác  https://silo.tips/queue/quadrature-formulas-in-two-dimensions-math-finite-element-method-section-001-spr?&queue_id=-1&v=1653006217&u=MTIzLjE2LjUuMTkz
            Dùng luôn công thức bậc 5 vì hàm phần tử hữu hạn ta chỉ cần đến bậc 2:
            Sử dụng công thức đổi tọa độ để đưa tọa độ tam giác bất kì về tam giác (0,0), (1,0), (0,1).
            Công thức 7 điểm ở file trên bị sai nên mình chuyển sang dùng
            Công thức 14 điểm ở https://zhilin.math.ncsu.edu/TEACHING/MA587/Gaussian_Quadrature2D.pdf
        Có được thư viện tính tích phân trên đoạn [(x1,y1),(x2,y2)] và trên tam giác.
        file : gaus_quadrature_lib.py
Part 3: Thiết lập 2 loại ko gian phần tử hữu hạn:

    Loại 1: tuyến tính hình kim tự tháp
    Loại 2: dạng bậc 2

Part 4: Thiết lập điều kiện biên :

    1.Cho hình chữ nhật [0,1] x [0,1]
         Tạo 1 hàm là sự kết hợp của đa thức + sin,cos, exp
         Tính đạo hàm, Laplace và đạo hàm theo hướng tại biên để ra đk Dirichlet ở nửa trái 
         và đk Neumann ở nửa phải.
    2.Thiết lập hệ phương trình bự - toàn cục
         Rồi trừ đi các phần phụ thuộc,...
         Ra được ma trận rút gọn
         Giải ma trận rút gọn
         
     Thử nghiệm với hàm f(x,y) = x(1-x)y(2-y)
   ![output1](https://user-images.githubusercontent.com/29473579/169923469-2276d94e-d50a-49d3-a6fa-46230a442c8c.png)
   ![output_analytic1](https://user-images.githubusercontent.com/29473579/169923479-b55d0998-b561-4079-bf82-babd7fe572be.png)



 Part 5: Giải ma trận thưa
            
         
