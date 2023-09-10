
def main():
    data = [ [ 0 for i in range(3) ] for j in range(3) ]
    
    for i in range(3):
        for j in range(3):
            try:
                data[i][j] = int ( input(('Enter data[%d][%d]:' %(i,j) )) )
            except:
                print('Error!Enter Integer Value!')
                data[i][j] = int ( input(('Enter data[%d][%d]:' %(i,j) )) )


    
    
    result = ( '''result: |  %d %d %d  |
        |  %d %d %d  |
        |  %d %d %d  |'''           %(data[0][0],data[0][1],data[0][2],
                                      data[1][0],data[1][1],data[1][2],
                                      data[2][0],data[2][1],data[2][2]) )
    print(20*'-')
    print( result )

    
    input()


                                
if __name__ == "__main__":main()
