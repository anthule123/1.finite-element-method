# finite-element-method

Bước 1: Vẽ hàm tuyến tính từng khúc từ [0,1] x [0,1] -> R

    Bài 1. Tạo lưới như ở https://github.com/anthule123/finite-element-method/blob/main/draw1.ipynb
    
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
          
         
