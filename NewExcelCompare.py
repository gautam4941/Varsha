def  Common_data_finder( input_path1, input_path2, output_path ):
    import pandas as pd
    import re

    data1 = pd.read_excel( input_path1, header = None )
    data2 = pd.read_excel( input_path2, header = None )

    print( data1 )
    print()
    print()
    print( data2 )

    for i in data2[0]:
        print( type(i) )

    for i in range( len( data1[0].index ) ):
        if( isinstance( data1[0][i], str ) == False ):
            data1[0][i] = str( data1[0][i] )

    for i in range( len( data2[0].index ) ):
        if( isinstance( data2[0][i], str ) == False ):
            data2[0][i] = str( data2[0][i] )
    print()
    print()
    
    data1_list = []
    for i in data1[0]:
        print( f"Splitting Data1 = { i.split(',') }" )
        data1_list.append( i.split( ',' ) )


    data2_list = []
    for i in data2[0]:
        print( f"Splitting Data2 = { i.split(',') }" )
        data2_list.append( i.split( ',' ) )
    common_data = []

    if( len( data1_list ) >= len( data2_list )):

        for i in range( len( data2_list) ):
            temp = []
            for j in data1_list[i]:
                if( j in data2_list[i] ):
                    temp.append( j )

            common_data.append( temp )
    else:
        for i in range( len( data1_list) ):
            temp = []
            for j in data2_list[i]:
                if( j in data1_list[i] ):
                    temp.append( j )

            common_data.append( temp )

    print()
    for i in common_data:
        print(i)
    print()

    for i in range( len(common_data) ):
        for j in range( len( common_data[i] ) ):
            value = common_data[i][j]

            if( value != 'Nan' ):
                common_data[i][j] = int( value )

    print( "After Change,")
    for i in common_data:
        print(i)

    pd.DataFrame( common_data ).to_excel( output_path )

Common_data_finder(   r'C:\Users\adity_000\Desktop\exceldata1_4.xlsx'
                    , r'C:\Users\adity_000\Desktop\exceldata2_5.xlsx'
                     , r'C:\Users\adity_000\Desktop\Output_File.xlsx' )
