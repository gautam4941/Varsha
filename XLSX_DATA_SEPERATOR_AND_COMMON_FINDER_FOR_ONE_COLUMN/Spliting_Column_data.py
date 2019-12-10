import re
import pandas as pd

def output_path( file_path ):
    pos = 0
    
    for i in range( len( file_path ) ):
        if( file_path[i] == '\\' ):
            pos = i

    folder_path = file_path[ : pos ]
    print( folder_path )
    file_name = file_path[ pos : ][ : -5 ] + '_Output.xlsx'
    return folder_path + file_name

import re
import pandas as pd

def remove_url( *datas ):
    
    for i in datas:
        
        header_flag = True
        while( True ):
            header_op = int( input("1. No Header, 2.  Header = ") )
        
            if( header_op == 1 ):
                data = pd.read_excel( i, header = None )
                header_flag = False
                break
                
            elif( header_op == 2 ):
                data = pd.read_excel( i )
                break
                
            else:
                print("Wrong Input, Try Again")
        
        output_file_path = output_path( i )
        print( data )
        
        if( header_flag ):
            col_data = data[ list( data.columns )[0] ]
        else:
            col_data = data[0]
        
        l = []

        for i in col_data:
            l.append( re.split( ',', i ) )

        for i in l:
            i.pop(0)
        

        temp = []

        for i in l :
            msg = ''
            for j in i:
                msg = msg + j +','
            temp.append( msg )

        l = temp.copy()

        temp = []

        for i in l:
            temp.append( i[ : len( i ) - 1 ] )

        l = temp.copy()
        del temp

        pd.DataFrame( l ).to_excel( output_file_path )

remove_url( r'C:\Users\adity_000\Desktop\Python Programs\Varsha Python Coding\Task 2 - 8-12-19\Data1_xlsx.xlsx',
            r'C:\Users\adity_000\Desktop\Python Programs\Varsha Python Coding\Task 2 - 8-12-19\Data2_xlsx.xlsx')
