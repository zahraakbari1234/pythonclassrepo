import os

def main():

    os.system('cls')

    print('BMI CALCULATE\n')
    
    name = input('enter your name:')
    weight = input('enter your W(kg):')
    height = input('enter your H(m):')

    bmi = int(weight) / ( float(height)**2 )

    result = ('%s BMI is %.2f '% ( name , bmi ))
    print(result)

    input('Press a Key to Exit')




if __name__ == '__main__':main()
    
