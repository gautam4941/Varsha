def Common_data_finder( input_path1, input_path2, output_path ):

    import pandas as pd
    import re

    data1 = pd.read_excel( input_path1, header = None )
    data2 = pd.read_excel( input_path2, header = None )

    data_list_1 = []

    for i in data1[0]:
        temp = []

        if( ',' not in str(i) ):
            temp.append( i )
        else:
            for j in re.findall( '\d+', i ):
                temp.append( j )

        data_list_1.append( temp )

    data_list_2 = []

    for i in data2[0]:
        temp = []

        if( ',' not in str(i) ):
            temp.append( i )
        else:
            for j in re.findall( '\d+', i ):
                temp.append( j )

        print( f"temp = { temp }")
        data_list_2.append( temp )


    for i in range( len( data_list_1 ) ):

        for j in range( len( data_list_1[i] ) ):
            if( data_list_1[i][j] != 'Nan' ):
                data_list_1[i][j] = float( data_list_1[i][j] )

    for i in range( len( data_list_2 ) ):

        for j in range( len( data_list_2[i] ) ):

            if( data_list_2[i][j] != 'Nan' ):
                data_list_2[i][j] = float( data_list_2[i][j] )


    common_data = []

    if( len( data_list_1 ) >= len( data_list_2 ) ):

        for i in range( len( data_list_2 ) ):
            temp = []

            if( len( data_list_1[i] ) >= len( data_list_2[2] ) ):

                for j in data_list_2[i]:

                    if( isinstance( j, float ) == False ):
                        if( j in data_list_1[i] ):
                            temp.append( "Null Data in File 1" )

                        else:
                            temp.append( "Null Data in File 2" )

                    elif( j in data_list_1[i] ):
                        temp.append( j ) 

            else:
                for j in data_list_1[i]:

                    if( isinstance( j, float ) == False ):
                        if( j in data_list_1[i] ):
                            temp.append( "Null Data in File 1" )

                        else:
                            temp.append( "Null Data in File 2" )

                    elif( j in data_list_2[i] ):
                        temp.append( j )

            print()

            common_data.append( temp )

    else:

        for i in range( len( data_list_1 ) ):
            temp = []

            if( len( data_list_1[i] ) >= len( data_list_2[2] ) ):
                for j in data_list_2[i]:

                    if( isinstance( j, float ) == False ):
                        if( j in data_list_1[i] ):
                            temp.append( "Null Data in File 1" )

                        else:
                            temp.append( "Null Data in File 2" )

                    elif( j in data_list_1[i] ):
                        temp.append( j )

            else:
                for j in data_list_1[i]:
                    if( isinstance( j, float ) == False ):
                        if( j in data_list_2[i] ):
                            temp.append( "Null Data in File 1" )

                        else:
                            temp.append( "Null Data in File 2" )

                    elif( j in data_list_2[i] ):
                        temp.append( j )

            common_data.append( temp )

    pd.DataFrame( common_data ).to_excel( output_path )


Common_data_finder( 'Book4.xlsx', 'Book5.xlsx', r'C:\Users\gauta\PycharmProjects\Varsha Task\Output_File.xlsx' )
