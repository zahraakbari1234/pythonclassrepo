import os

def main():

    os.system('cls')

    while(1):

        print(' ')
        last_new_bmi = input('Last BMI or New BMI?(L/l=Last  N/n=New):')
    
        if( last_new_bmi . lower()== 'n' ):
            
            id_number = input('enter your number:')
            name = input('enter your name:')
            weight = input('enter your W(kg):')
            height = input('enter your H(m):')

            bmi = int(weight) / ( float(height)**2 )

            result = ('%s BMI is %.2f '% ( name , bmi ))
            print(result)

            save_result = input('Do you want to save?(Y/y=Yes  N/n=No):')

            
            if( save_result.lower() == 'y'):
                
                try:
                    
                    f = open( 'saved_results.txt','r')
                    result_saved = f.read()
                    f.close()
                    
                    try:
                        id_index = result_saved.find('id=%d'%int(id_number) )
                        if( id_index < 0 ):#قبلا سيو نشده
                            f = open( 'saved_results.txt','a')
                            f.write('id=%d %s BMI is %.2f!\n'% ( int(id_number), name , bmi ))
                            f.close()
                        elif( id_index >= 0 ):#يکبار قبلا سيو شده
                            print('This number is saved before, change number')

                    except:
                        print('unexpected error!')

                        
                except:
                    f = open( 'saved_results.txt','w')
                    f.write('id=%d %s BMI is %.2f!\n'% ( int(id_number), name , bmi ))
                    f.close()




        elif( last_new_bmi . lower()== 'l' ):
            
                try:
                    f = open( 'saved_results.txt','r')
                    id_number = input('enter your number:') 
                    result_saved = f.read()
                    id_index = result_saved.find('id=%d'%int(id_number) )
                    if(id_index < 0 ):
                        print(' there is no saved result to show!')
                    else:
                        
                        end = result_saved[id_index: ].find('!')
                        end_index = end + id_index
                        print( result_saved[id_index+5:end_index ] )
                        print(' ')
                        f.close()

                except:
                    print(' there is no saved result to show!')
                    print(' ')

  
if __name__ == '__main__':main()
    
