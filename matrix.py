
def main():
    data = [ [ 0 for i in range(3) ] for j in range(3) ]

    i = 0
    j = 0
    
    while( i < 3 ):
        while( j < 3 ):
             try:
                data[i][j] = int ( input(('Enter data[%d][%d]:' %(i,j) )) )
                j += 1
             except:
                print('Error!Enter Integer Value!')
        i += 1
        j = 0
       


    result = ( '''result:
        |  %d %d %d  |
        |  %d %d %d  |
        |  %d %d %d  |'''  %(data[0][0],data[0][1],data[0][2],
                           data[1][0],data[1][1],data[1][2],
                           data[2][0],data[2][1],data[2][2]) )
    print( )
    print( )
    print( )
    print( 20 * '-' )

    print( result )


    input('Press Enter To Exit')

                              
if __name__ == "__main__":main()
