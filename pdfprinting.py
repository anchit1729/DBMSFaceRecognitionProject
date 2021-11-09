    
    
def pdfprint(x, y):    
    
    def get_data_from_prettytable(data):
        """
        Get a list of list from pretty_data table
        Arguments:
            :param data: data table to process
            :type data: PrettyTable
        """

        def remove_space(liste):
            """
            Remove space for each word in a list
            Arguments:
                :param liste: list of strings
            """   
            list_without_space = []
            for mot in liste:                                       # For each word in list
                word_without_space = mot.replace(' ', '')           # word without space
                list_without_space.append(word_without_space)       # list of word without space
            return list_without_space

        # Get each row of the table
        string_x = str(x).split('\n')                               # Get a list of row
        header = string_x[1].split('|')[1: -1]                      # Columns names
        rows = string_x[3:len(string_x) - 1]                        # List of rows

        list_word_per_row = []
        for row in rows:                                            # For each word in a row
            row_resize = row.split('|')[1:-1]                       # Remove first and last arguments
            list_word_per_row.append(remove_space(row_resize))      # Remove spaces

        return header, list_word_per_row

    from fpdf import FPDF

    def export_to_pdf(header, data):
        """
        Create a a table in PDF file from a list of row
            :param header: columns name
            :param data: List of row (a row = a list of cells)
            :param spacing=1: 
        """
        pdf = FPDF()                                # New  pdf object
        
        pdf.set_font("Arial", size=11)              # Font style
        epw = pdf.w - 2*pdf.l_margin                # Witdh of document
        col_width = pdf.w / 6.5                   # Column width in table
        row_height = pdf.font_size * 1.5            # Row height in table
        spacing = 1.3                               # Space in each cell

        pdf.add_page()                              # add new page
        pdf.image("Images/bestbanklogo.jpg", x=pdf.w/3, y=0, w=pdf.w/3, h=pdf.w/11 )
        pdf.cell(epw, 10, txt="", ln=1, align="L")
        pdf.cell(epw, 10, txt="", ln=2, align="L")
        pdf.cell(epw, 10, 'Account Information', ln=3, align='C')   # create title cell
        pdf.cell(epw, 5, txt=f"Branch: {y.branch.address}", ln=3, align="L")
        pdf.cell(epw, 5, txt=f"Account No.: {y.account_id}", ln=4, align="L")
        pdf.cell(epw, 5, txt=f"Account Type: {y.account_type}", ln=5, align="L")
        pdf.cell(epw, 5, txt=f"Balance: {y.balance} ({y.currency})", ln=6, align="L")
        pdf.ln(row_height*spacing)                  # Define title line style

        # Add header
        for item in header:                         # for each column
            pdf.cell(col_width, row_height*spacing, # Add a new cell
                    txt=item, border=1)
        pdf.ln(row_height*spacing)                  # New line after header

        for row in data:                            # For each row of the table
            for item in row:                        # For each cell in row
                pdf.cell(col_width, row_height*spacing, # Add cell
                        txt=item, border=1)
            pdf.ln(row_height*spacing)              # Add line at the end of row

        pdf.output('simple_demo.pdf')               # Create pdf file 
        pdf.close()                                 # Close file

    header, data = get_data_from_prettytable(x)
    export_to_pdf(header, data)