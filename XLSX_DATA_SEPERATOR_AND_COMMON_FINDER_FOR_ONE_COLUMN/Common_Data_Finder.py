import pandas as pd

def common_file_data( path1, path2, output_path ):
    
    data1 = pd.read_excel( path1, header = None )
    data2 = pd.read_excel( path2, header = None )
    
    """
    print( data1 )
    print()
    print( data2 )
    print()
    """
    
    col_data1 = data1[1]
    col_data2 = data2[1]
    
    print( col_data1 )
    print()
    print( col_data2 )
    print()
    
    print( col_data2[1] )
    
    final = []

    if( len( col_data1 ) >= len( col_data2 ) ):
        for i in range(1, len( col_data2 ) ):
            temp = []
            
            for j in col_data2[i]:
                
                if( j in col_data1[i] ):
                    temp.append( j )
            
            final.append( temp )                
    else:
        #print( small_data[0] ) -> Show this also
        
        for i in range(1, len( col_data1 ) ):
            temp = []
            
            for j in col_data1[i]:
                
                if( j in col_data2[i] ):
                    temp.append( j )
            
            final.append( temp )
    
    print( final )
    print()
    
    for i in final:
        for j in range( i.count(',') ):
            i.remove(',')

    for i in final:
        print(i)
        
    pd.DataFrame( final ).fillna( 'nan' ).to_excel( output_path )

common_file_data( r'C:\Users\adity_000\Desktop\Python Programs\Varsha Python Coding\Task 2 - 8-12-19\Data1_xlsx_Output.xlsx',
                  r'C:\Users\adity_000\Desktop\Python Programs\Varsha Python Coding\Task 2 - 8-12-19\Data2_xlsx_Output.xlsx',
                  r'C:\Users\adity_000\Desktop\Python Programs\Varsha Python Coding\Task 2 - 8-12-19\Data3_Output.xlsx')
