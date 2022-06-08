
radius = float (input(' please enetr the circle radius : '))
if radius > 0 :
    circle_area = (radius * radius)*3.14
    circle_perimeter = 2 * 3.14 * radius
    print('circle area is : ' , circle_area )
    print('circle perimeter is : ' , circle_perimeter )
else :
    print('error : radius should  be a positive number ')
    
