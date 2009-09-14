=========================
Using Python with Excel
=========================

If this library set can't do this stuff already, its because no one has written it yet.
What are we going to cover::

    What is xlrd for?
    What is xlwt for?
    What is xlutils for?
    What do you still need Excel via COM for? 
  
Why not PyExcelerator?
::

    Dead in the water
    Not maintained
    xlrd, xlwt, xlutils are based on old PyExcelerator. 
 
----

Automating Excel using COM
============================

 * Slow
 * Buggy
 * License violation
 * requires windows

----

Real world example
====================

 * 100+<B Excel file needs processing
 * COM, 7 hours, Weird obscure error messages every so often
 * xlrd, xlutils, xlwt, 7 minutes, Good error handling
 
Getting Help
=============

 * Google mailing list
 
xlrd
======

Opening workbooks::

    open_workbook()
     - filename
     - file_contents
     - encoding_override
     - formatting_info
   
Navigating Workbooks::

    Book.nsheets
    Book.sheet_by_index(index)
    Lots more...
    
Some specifics::

    You can get data by cell, or values of cells.
    You can get groups of cells via the Rows commands.
    Various Utility functions
    xlrd will return unicode
    You may need to specify the encoding
        - do so with open_workbook
        
Types of cell
================

Text::

 * xlrd.XL_CELL_TEXT
 * unicode
 
----

 * Number
 * Error 
 * Empty
 * Blank (for formatting)
 
---- 
 
Date stuff::

 Be careful because Excel does dates funny
 xlrd.XL_CELL_DATE
 float
 use xldate_as_tuple
 then use datetime(*tuple)
 BEWARE dates before 1904
 
Names::

 These are variables defined in Excel by doing Insert > Name > Define
 can be a constant, absolute, has scope at different levels
 
Formatting:

 You can load formatting and modify it.
 Can be complex
 
 
Handy script
=================

 runxlrd.py lets you do introspection easily
 
---- 
 
=======================
Writing Excell Files
=======================

Workbook is a class in xlwt that is::

 Finds sheets only by index
 primarily row oriented.
 
Rows notes::

 Every 1000 rows you write, flush your rows.
 Once flushed, you can't modify them again.
 
Column notes::
 
 Only contain formatting information.
 
Cells::

 You can write a cell from the worksheet or from the row.
 Try not to overrwrite what you have for a cell and its disabled by default.
 
Unicode::

 Pass unicode to xlwt
 If you must use encoded strings, make sure the encoding is consistent
 If your encoding isn't ascii, create the workbook appropriately

----
 
Formatting
============

Formatting comes as a group of styles expressed as XF records in xlwt.
xlwt.easyxf is for creating them. What isn't handled by Styles?

----

easyxf
=======

(<element>: (<attribute value>,) +;) +
::

    Zero or more element specifications
    Follow CSS style patterns
    lots of booleans and lots of colors
    - Can specify rgb values
    - Beware the color palette
    - best just to use names and leave the palette be!
    
types of elements you can set::

    font
    alignment
    borders
    pattern
    protection
    - gotchas!
    - does actually work
    - very convoluted
    
More things about easyxf::

    lots of synonyms
    take a good look at the tables
    only use stuff you understand or are happy to experiment with!
    More synonyms coming
    maybe more coolness for borders
    
Formatting rows and columns::

    row.set_style(xfstyle)
    column.set_style(xfstyle)
    Precedence
    - cell
    - row
    - column
    Hiding
    width
    - xlwt does not support autowidth 
    - because that is a function of the application and not the file format
    height
    - very complicated rules
    - easier to set height on row style

----    

Sheets and Workbooks
=======================
    
 * Lots of attributes to play with!
 * All the ins and outs of these are beyond the scope of this class
 * Happy to try and help during the workshop session
 
---- 
 
Style compression
==================

Excel limits you to 400 fonts and 4000 XF records so be careful when generating large excel files.
::

 Specified when creating the workbook
 if its easier to create lots of styles
  - set style compression to 2
 In general
  - Create all your styles in advance
  - leave style compression off
 Run the example
  - inspect with runxlrd.py xfc *.py
 
---- 
  
Formulae
===========

 * xlwt.Formula(text)
 * Row.set_cell_formula(col_index,formula,[style])
 
What is supported?
::

    all the built-in formula functions
    All the analysis toolpak (ATP) functions
    Comma or semicolon as argument seperator
    case-insensitive matching
    - Function names
    - Sheet names
    - cell names
    
Not supported?
::

    References to external workbooks
    array formula
    references to defined Names
    data validation
    conditional formatting
    formula evaluation
    
----

Utility methods
=================

 * rowcol_to_cell(rowindex,column_index) *converts a row/col integer reference into a excel reference*
 * valid_sheet_name(string) *Checks to ensure that the name is valid for a workbook*
 
----

Other things
================

 * Hyperlinks are just another type of format
 * images can be inserted using the insert_bitmap method of the sheet class
 * only supports 24 bit bmp?
 * merged cells are groups of inserted cells. Use Worksheet.write_merge() and not Worksheet.merge()
 * Borders around groups of cells is challenging. Follow the examples!
         * Check out the outlines and zoom functions!
 
Split and freeze panes::

 Split panes do not work in xlwt
 non-frozen panes appear to be somewhat buggy
 
---- 
 
Other utilities in xlutils
============================

::
    xlutils.styles
    - Style name and information for a given cell
    xlutils.display
    - quoted_sheet_name
    - cell_display
    xlutils.copy
    - xlrd.Book -> xlwt.Workbook
    
    
Filters let you change an existing file. Is rather sophisticated
::
    Original -> filter -> filter - results
    
    start()
    workbook(rdbook,wtbook_name)
    sheet(rdsheet,wtsheet_name)
    set_rdsheet(rdsheet)
    row(rdrowx,wtrowx)
    The order
    - start
     * workbook
      - sheet
      - set_rdsheet
       * row
        - cell
      - finish
